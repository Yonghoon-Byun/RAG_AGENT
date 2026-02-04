# 단기 청킹 전략 계획 (1-2주)

> 토목설계 기준/지침 RAG 도입을 위한 빠른 검증 프로토타입

## 개요

### 목표
- **1-2주 내** 벡터 검색 기반 RAG 프로토타입 구축
- 현재 238개 섹션 데이터로 검색 품질 검증
- 최소 비용으로 실용성 확인

### 현재 상태
| 항목 | 상태 | 비고 |
|------|------|------|
| 데이터 | ✅ 완료 | 238개 섹션, 계층 구조 |
| PostgreSQL | ✅ 완료 | GIN 인덱스, 전문 검색 |
| 벡터 임베딩 | ❌ 미구현 | pgvector 필요 |
| 의미론적 청킹 | ❌ 미구현 | 긴 섹션 미분할 |

### 제약 조건
- 예산: 최소화 (무료/저비용 우선)
- 기간: 1-2주 (10 영업일)
- 인프라: 기존 PostgreSQL 활용

---

## Phase 0: 사전 검증 (Day 1 오전)

### TODO-0.1: PostgreSQL 버전 확인
```sql
-- 먼저 PostgreSQL 버전 확인 (pgvector는 PostgreSQL 11+ 필요, 권장 15+)
SELECT version();

-- 예상 출력: PostgreSQL 15.x 또는 그 이상
-- 만약 버전이 11 미만이면 업그레이드 필요
```

**검증 기준**: PostgreSQL 버전 11 이상 확인
**실패 시 대응**: Docker로 PostgreSQL 15 + pgvector 컨테이너 실행

### TODO-0.2: .env 파일 생성
```bash
# 프로젝트 루트에 .env 파일 생성
# D:\DATA\RAG_AGENT\.env

OPENAI_API_KEY=sk-your-api-key-here
DB_HOST=10.0.0.20
DB_PORT=2332
DB_NAME=dde-water
DB_USER=postgres
DB_PASSWORD=postgres
```

**검증 기준**: `.env` 파일 존재 및 OPENAI_API_KEY 유효성 확인
```python
import os
from dotenv import load_dotenv
load_dotenv()
assert os.getenv('OPENAI_API_KEY'), "OPENAI_API_KEY not set"
print("Environment OK")
```

---

## Phase 1: 환경 구축 (Day 1 오후 - Day 2)

### TODO-1.1: pgvector 확장 설치

**Windows 설치 방법**:
```bash
# 옵션 1: 미리 빌드된 바이너리 (권장)
# https://github.com/pgvector/pgvector/releases 에서 Windows 바이너리 다운로드

# 옵션 2: Docker 사용 (가장 안전)
docker run -d --name pgvector-db \
  -e POSTGRES_PASSWORD=postgres \
  -p 5433:5432 \
  pgvector/pgvector:pg16
```

```sql
-- pgvector 확장 설치
CREATE EXTENSION IF NOT EXISTS vector;

-- 임베딩 컬럼 추가
ALTER TABLE design_standard.design_sections
ADD COLUMN IF NOT EXISTS embedding vector(1536);

-- HNSW 인덱스 생성 (검색 속도 최적화)
CREATE INDEX IF NOT EXISTS idx_sections_embedding
ON design_standard.design_sections
USING hnsw (embedding vector_cosine_ops);
```

**검증 기준**: `SELECT * FROM pg_extension WHERE extname = 'vector';` 성공

### TODO-1.2: Python 환경 구성
```bash
pip install openai tiktoken psycopg2-binary python-dotenv
```

**필요 패키지**:
| 패키지 | 용도 | 비용 |
|--------|------|------|
| openai | 임베딩 생성 | $0.02/1M tokens |
| tiktoken | 토큰 수 계산 | 무료 |
| psycopg2-binary | PostgreSQL 연결 | 무료 |

**검증 기준**: `python -c "import openai; print('OK')"` 성공

---

## Phase 2: 토큰 분석 및 청킹 (Day 3-5)

### TODO-2.1: 섹션별 토큰 수 분석
```python
# analyze_tokens.py
import json
import tiktoken
import os

enc = tiktoken.get_encoding("cl100k_base")

# 절대 경로 사용 (Windows 호환)
DATA_PATH = r'D:\DATA\RAG_AGENT\design_standards_db_restructured.json'

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

def analyze_section(section, results):
    content = f"{section['title']}\n\n{section['content']}"
    tokens = len(enc.encode(content))
    results.append({
        'code': section['code'],
        'title': section['title'][:50],
        'tokens': tokens,
        'needs_split': tokens > 600
    })
    for child in section.get('children', []):
        analyze_section(child, results)

results = []
for section in data:
    analyze_section(section, results)

# 통계 출력
over_600 = [r for r in results if r['needs_split']]
print(f"총 섹션: {len(results)}")
print(f"600 토큰 초과: {len(over_600)} ({len(over_600)/len(results)*100:.1f}%)")
print(f"최대 토큰: {max(r['tokens'] for r in results)}")
```

**검증 기준**: 600 토큰 초과 섹션 목록 확보

### TODO-2.2: 간단한 청킹 전략 구현
```python
# simple_chunker.py
import tiktoken

MAX_TOKENS = 600
OVERLAP_TOKENS = 100

enc = tiktoken.get_encoding("cl100k_base")

def chunk_section(section):
    """섹션을 600 토큰 단위로 분할 (100 토큰 오버랩)"""
    content = f"## {section['title']}\n\n{section['content']}"
    tokens = enc.encode(content)

    if len(tokens) <= MAX_TOKENS:
        return [{
            'content': content,
            'section_code': section['code'],
            'chunk_index': 0,
            'is_complete': True
        }]

    chunks = []
    start = 0
    chunk_index = 0

    while start < len(tokens):
        end = min(start + MAX_TOKENS, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = enc.decode(chunk_tokens)

        # 메타데이터 포함
        if chunk_index > 0:
            chunk_text = f"[계속] {section['title']} (Part {chunk_index + 1})\n\n{chunk_text}"

        chunks.append({
            'content': chunk_text,
            'section_code': section['code'],
            'chunk_index': chunk_index,
            'is_complete': False
        })

        start = end - OVERLAP_TOKENS
        chunk_index += 1

    return chunks
```

**검증 기준**: 모든 청크가 600 토큰 이하

### TODO-2.3: 청크 테이블 생성
```sql
-- 청크 테이블
CREATE TABLE IF NOT EXISTS design_standard.chunks (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    section_code VARCHAR(50) REFERENCES design_standard.design_sections(code),
    chunk_index INTEGER DEFAULT 0,
    is_complete BOOLEAN DEFAULT true,
    token_count INTEGER,
    embedding vector(1536),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 인덱스
CREATE INDEX idx_chunks_section ON design_standard.chunks(section_code);
CREATE INDEX idx_chunks_embedding ON design_standard.chunks
    USING hnsw (embedding vector_cosine_ops);
```

**검증 기준**: 테이블 생성 및 청크 삽입 성공

---

## Phase 3: 임베딩 생성 (Day 6-7)

### TODO-3.1: OpenAI 임베딩 생성
```python
# generate_embeddings.py
import os
from openai import OpenAI
import psycopg2
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",  # $0.02/1M tokens
        input=text
    )
    return response.data[0].embedding

# DB 연결
conn = psycopg2.connect(
    host='10.0.0.20',
    port=2332,
    database='dde-water',
    user='postgres',
    password='postgres'
)
cursor = conn.cursor()

# 청크별 임베딩 생성
cursor.execute("SELECT id, content FROM design_standard.chunks WHERE embedding IS NULL")
chunks = cursor.fetchall()

for chunk_id, content in chunks:
    embedding = get_embedding(content)
    cursor.execute(
        "UPDATE design_standard.chunks SET embedding = %s WHERE id = %s",
        (embedding, chunk_id)
    )
    conn.commit()
    print(f"Embedded chunk {chunk_id}")

cursor.close()
conn.close()
```

**예상 비용**:
- 238개 섹션 × 평균 400 토큰 ≈ 95,200 토큰
- text-embedding-3-small: $0.02/1M tokens
- **예상 비용: ~$0.002 (거의 무료)**

**검증 기준**: 모든 청크에 embedding 값 존재

### TODO-3.2: 무료 대안 - 로컬 임베딩 (옵션)
```python
# local_embeddings.py (무료 대안)
from sentence_transformers import SentenceTransformer

# 다국어 지원 모델 (한글 OK)
model = SentenceTransformer('intfloat/multilingual-e5-small')

def get_local_embedding(text):
    return model.encode(f"passage: {text}").tolist()
```

**장점**: 완전 무료, 오프라인 사용 가능
**단점**: 품질이 OpenAI보다 낮을 수 있음

---

## Phase 4: 검색 구현 (Day 8-9)

### TODO-4.1: 벡터 유사도 검색 함수
```sql
-- 벡터 검색 함수
CREATE OR REPLACE FUNCTION design_standard.search_similar(
    query_embedding vector(1536),
    match_count INT DEFAULT 5
)
RETURNS TABLE (
    chunk_id INT,
    section_code VARCHAR(50),
    content TEXT,
    similarity FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.section_code,
        c.content,
        1 - (c.embedding <=> query_embedding) as similarity
    FROM design_standard.chunks c
    WHERE c.embedding IS NOT NULL
    ORDER BY c.embedding <=> query_embedding
    LIMIT match_count;
END;
$$ LANGUAGE plpgsql;
```

### TODO-4.2: 하이브리드 검색 (키워드 + 벡터)
```sql
-- 하이브리드 검색 함수
CREATE OR REPLACE FUNCTION design_standard.hybrid_search(
    query_text TEXT,
    query_embedding vector(1536),
    match_count INT DEFAULT 5,
    keyword_weight FLOAT DEFAULT 0.3,
    vector_weight FLOAT DEFAULT 0.7
)
RETURNS TABLE (
    chunk_id INT,
    section_code VARCHAR(50),
    content TEXT,
    combined_score FLOAT
) AS $$
BEGIN
    RETURN QUERY
    WITH keyword_results AS (
        SELECT
            c.id,
            c.section_code,
            c.content,
            ts_rank(to_tsvector('simple', c.content),
                    plainto_tsquery('simple', query_text)) as keyword_score
        FROM design_standard.chunks c
        WHERE to_tsvector('simple', c.content) @@ plainto_tsquery('simple', query_text)
    ),
    vector_results AS (
        SELECT
            c.id,
            c.section_code,
            c.content,
            1 - (c.embedding <=> query_embedding) as vector_score
        FROM design_standard.chunks c
        WHERE c.embedding IS NOT NULL
    )
    SELECT
        COALESCE(k.id, v.id) as chunk_id,
        COALESCE(k.section_code, v.section_code) as section_code,
        COALESCE(k.content, v.content) as content,
        (COALESCE(k.keyword_score, 0) * keyword_weight +
         COALESCE(v.vector_score, 0) * vector_weight) as combined_score
    FROM keyword_results k
    FULL OUTER JOIN vector_results v ON k.id = v.id
    ORDER BY combined_score DESC
    LIMIT match_count;
END;
$$ LANGUAGE plpgsql;
```

**검증 기준**: 테스트 쿼리 5개 이상에서 관련 결과 반환

### TODO-4.3: Python 검색 래퍼
```python
# search.py
import os
from openai import OpenAI
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """환경변수에서 DB 연결 정보 로드"""
    return psycopg2.connect(
        host=os.getenv('DB_HOST', '10.0.0.20'),
        port=int(os.getenv('DB_PORT', 2332)),
        database=os.getenv('DB_NAME', 'dde-water'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )

def search_rag(query: str, top_k: int = 5):
    """RAG 검색 수행"""
    # 1. 쿼리 임베딩 생성
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    # 2. 하이브리드 검색
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM design_standard.hybrid_search(%s, %s, %s)
    """, (query, query_embedding, top_k))

    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results

# 사용 예시
results = search_rag("침전지 설계 기준")
for r in results:
    print(f"[{r[1]}] Score: {r[3]:.3f}")
    print(f"  {r[2][:100]}...")
```

---

## Phase 5: 검증 및 평가 (Day 10)

### TODO-5.0: Ground Truth 데이터셋 생성 (필수 선행 작업)

테스트 질의의 정답(expected_sections)이 실제 데이터와 일치하는지 검증해야 합니다.

```python
# create_ground_truth.py
"""
Ground Truth 생성 프로세스:
1. 각 질의에 대해 실제 섹션 내용을 검토
2. 관련 키워드가 포함된 섹션 확인
3. 도메인 전문가 검토 (가능한 경우)
"""
import json
import re

DATA_PATH = r'D:\DATA\RAG_AGENT\design_standards_db_restructured.json'

def search_keyword_in_sections(keyword, data, results=None):
    """특정 키워드가 포함된 섹션 찾기"""
    if results is None:
        results = []

    for section in data:
        content = f"{section.get('title', '')} {section.get('content', '')}"
        if keyword in content:
            results.append({
                'code': section['code'],
                'title': section['title'],
                'snippet': content[:200] + '...'
            })
        if section.get('children'):
            search_keyword_in_sections(keyword, section['children'], results)

    return results

# 키워드별 섹션 검색으로 Ground Truth 검증
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 검증할 키워드 목록
keywords = ['체류시간', '침전지', '응집제', '여과속도', '슬러지']

for kw in keywords:
    matches = search_keyword_in_sections(kw, data)
    print(f"\n=== '{kw}' 포함 섹션 ({len(matches)}개) ===")
    for m in matches[:5]:
        print(f"  [{m['code']}] {m['title']}")
```

**실행 결과를 바탕으로 아래 TEST_QUERIES 수정 필요**

### TODO-5.1: 테스트 질의 세트 작성 (검증된 Ground Truth)

```python
# 아래는 실제 데이터 검토 후 확정해야 하는 예시입니다.
# TODO-5.0 실행 결과에 따라 expected_sections를 수정하세요.

TEST_QUERIES = [
    # === Local 질의 (특정 정보 검색) ===
    # 키워드 "침전지"가 포함된 섹션: 5, 5.1, 5.2, 5.3 등 (TODO-5.0에서 확인)
    {
        "query": "침전지 체류시간 기준",
        "expected_sections": ["5.1", "5.2"],  # TODO-5.0 결과로 검증 필요
        "keywords": ["침전지", "체류시간"],
        "verified": False  # Ground Truth 검증 완료 시 True로 변경
    },
    {
        "query": "응집제 주입량 계산",
        "expected_sections": ["3.1", "3.2"],  # TODO-5.0 결과로 검증 필요
        "keywords": ["응집제", "주입량"],
        "verified": False
    },
    {
        "query": "여과속도 설계기준",
        "expected_sections": ["7.1", "7.2"],  # TODO-5.0 결과로 검증 필요
        "keywords": ["여과속도", "여과지"],
        "verified": False
    },

    # === Semi-Global 질의 (관련 정보 종합) ===
    {
        "query": "정수처리 공정 순서",
        "expected_sections": ["1", "1.1", "1.4"],
        "keywords": ["정수처리", "공정", "순서"],
        "verified": False
    },
    {
        "query": "슬러지 처리 방법",
        "expected_sections": ["23", "23.1"],  # 섹션 23: 배출수 및 슬러지 처리시설
        "keywords": ["슬러지", "처리"],
        "verified": False
    },

    # === Global 질의 (전체 이해 필요) ===
    {
        "query": "정수시설 설계시 고려사항",
        "expected_sections": ["1.1", "1.1.1", "1.1.4", "1.1.5"],
        "keywords": ["설계", "고려사항"],
        "verified": False
    },
]

def validate_ground_truth(test_queries, data_path):
    """Ground Truth 검증: expected_sections이 실제 데이터에 존재하는지 확인"""
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 모든 섹션 코드 수집
    all_codes = set()
    def collect_codes(sections):
        for s in sections:
            all_codes.add(s['code'])
            if s.get('children'):
                collect_codes(s['children'])
    collect_codes(data)

    # 검증
    for test in test_queries:
        for code in test['expected_sections']:
            if code not in all_codes:
                print(f"WARNING: Section '{code}' not found for query '{test['query']}'")
            else:
                print(f"OK: Section '{code}' exists")

    return all_codes

# 사용 예시
# all_codes = validate_ground_truth(TEST_QUERIES, DATA_PATH)
```

**검증 절차**:
1. `create_ground_truth.py` 실행하여 키워드별 섹션 매핑 확인
2. `TEST_QUERIES`의 `expected_sections` 수정
3. `validate_ground_truth()` 실행하여 섹션 코드 존재 확인
4. 모든 테스트 케이스의 `verified: True`로 변경 후 평가 진행

### TODO-5.2: 평가 스크립트
```python
# evaluate.py
def evaluate_search(test_queries):
    results = []

    for test in test_queries:
        search_results = search_rag(test['query'], top_k=5)
        retrieved_sections = [r[1] for r in search_results]

        # Recall@5 계산
        expected = set(test['expected_sections'])
        retrieved = set(retrieved_sections)
        recall = len(expected & retrieved) / len(expected) if expected else 0

        results.append({
            'query': test['query'],
            'recall': recall,
            'retrieved': retrieved_sections
        })

    avg_recall = sum(r['recall'] for r in results) / len(results)
    print(f"Average Recall@5: {avg_recall:.2%}")
    return results
```

**성공 기준**:
- Recall@5 ≥ 60%
- Local 질의 정확도 ≥ 80%

### TODO-5.3: 비교 평가 (키워드 vs 벡터 vs 하이브리드)
```python
def compare_methods():
    methods = ['keyword', 'vector', 'hybrid']
    results = {m: [] for m in methods}

    for test in TEST_QUERIES:
        # 각 방법별 검색 수행
        for method in methods:
            recall = search_and_evaluate(test, method)
            results[method].append(recall)

    # 결과 비교
    for method in methods:
        avg = sum(results[method]) / len(results[method])
        print(f"{method}: {avg:.2%}")
```

---

## 일정 요약

| Day | 작업 | 산출물 |
|-----|------|--------|
| 1-2 | 환경 구축 | pgvector 설치, Python 환경 |
| 3-5 | 토큰 분석 & 청킹 | 청크 테이블, 분할된 데이터 |
| 6-7 | 임베딩 생성 | 벡터 임베딩 완료 |
| 8-9 | 검색 구현 | 하이브리드 검색 함수 |
| 10 | 검증 & 평가 | 성능 평가 보고서 |

---

## 예상 비용

| 항목 | 비용 | 비고 |
|------|------|------|
| OpenAI 임베딩 | ~$0.01 | 238 섹션 × 400 토큰 |
| 검색 쿼리 | ~$0.001/쿼리 | 테스트용 |
| **총 예상 비용** | **< $1** | |

### 무료 대안 옵션
- 로컬 임베딩 (sentence-transformers): **$0**
- PostgreSQL + pgvector: **$0** (기존 인프라)

---

## 리스크 및 대응

| 리스크 | 확률 | 대응 |
|--------|------|------|
| pgvector 설치 실패 | 낮음 | PostgreSQL 버전 업그레이드 또는 Docker 사용 |
| 임베딩 품질 부족 | 중간 | 모델 변경 (text-embedding-3-large) |
| 검색 정확도 미달 | 중간 | 하이브리드 가중치 조정, 리랭킹 추가 |
| 한글 처리 문제 | 낮음 | multilingual 모델 사용 |

---

## 다음 단계 (Phase 2 이후)

이 프로토타입 검증 후:

1. **청킹 고도화**: 의미론적 청킹, 문장 경계 인식
2. **GraphRAG 적용**: 엔티티 추출, 관계 그래프 구축
3. **멀티모달**: 표/그림 처리, OCR 통합
4. **프로덕션**: API 서버, 웹 UI 개발

---

## Acceptance Criteria

### Phase 0: 사전 검증
- [ ] PostgreSQL 버전 11+ 확인 (`SELECT version();`)
- [ ] `.env` 파일 생성 및 OPENAI_API_KEY 설정

### Phase 1: 환경 구축
- [ ] pgvector 확장 설치 완료 (`SELECT * FROM pg_extension WHERE extname = 'vector';`)
- [ ] Python 패키지 설치 완료

### Phase 2: 청킹
- [ ] 토큰 분석 완료 (600 토큰 초과 섹션 목록 확보)
- [ ] 238개 섹션 → 청크 분할 완료 (모든 청크 ≤ 600 토큰)
- [ ] 청크 테이블 생성 및 데이터 삽입 완료

### Phase 3: 임베딩
- [ ] 모든 청크 임베딩 생성 완료 (`SELECT COUNT(*) FROM design_standard.chunks WHERE embedding IS NULL` = 0)

### Phase 4: 검색
- [ ] 벡터 검색 함수 동작 확인
- [ ] 하이브리드 검색 함수 동작 확인

### Phase 5: 검증
- [ ] Ground Truth 검증 완료 (모든 TEST_QUERIES의 `verified: True`)
- [ ] 테스트 질의 Recall@5 ≥ 60%
- [ ] 키워드 vs 벡터 vs 하이브리드 비교 완료

### 비용
- [ ] 총 비용 < $1

---

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-02-04 | 초기 계획 작성 |
| v2.0 | 2026-02-04 | Critic 피드백 반영: PostgreSQL 버전 확인 추가, .env 설정 추가, 절대 경로 사용, Ground Truth 검증 프로세스 추가 |

---

**PLAN_READY: .omc/plans/short-term-chunking-strategy.md**
