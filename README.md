# 설계 표준 문서 RAG 시스템

설계 표준 문서의 계층 구조를 재구성하고 PostgreSQL 데이터베이스에 저장하여 RAG 시스템에 활용하기 위한 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 다음 작업을 수행합니다:

1. **JSON 구조 재구성**: 평면 구조로 저장된 JSON 데이터를 계층 구조로 변환
2. **데이터베이스 저장**: PostgreSQL에 계층 구조 데이터 저장
3. **검색 기능**: 전문 검색 및 계층 구조 탐색 기능 제공

## 🗂️ 프로젝트 구조

```
RAG_AGENT/
├── README.md                           # 이 파일
├── README_DB_SETUP.md                  # 데이터베이스 설정 가이드
│
├── 📁 데이터 파일
│   ├── design_standards_db.json              # 원본 JSON (28개 섹션)
│   └── design_standards_db_restructured.json # 재구성된 JSON (238개 섹션)
│
├── 📁 Python 스크립트
│   ├── run_restructure.py              # JSON 재구성 스크립트 (메인)
│   ├── insert_to_postgres.py           # DB 삽입 스크립트
│   └── restructure_json.ipynb          # Jupyter 노트북 버전
│
├── 📁 sql/
│   └── 01_create_tables.sql            # 테이블 생성 SQL
│
└── 📁 archive/                         # 개발 과정 파일 보관
    ├── development/                    # 개발/테스트 스크립트
    │   ├── debug_parse.py
    │   ├── debug_parse2.py
    │   └── test_restructure.py
    └── test_data/                      # 테스트용 데이터
        ├── design_standards_db_example.json
        └── design_standards_db_example_restructured.json
```

## 🚀 빠른 시작

### 1단계: JSON 재구성 (이미 완료됨)

원본 JSON 파일을 계층 구조로 재구성합니다:

```bash
python run_restructure.py
```

**입력**: `design_standards_db.json` (28개 최상위 섹션, 일부 평면 구조)
**출력**: `design_standards_db_restructured.json` (238개 섹션, 완전한 계층 구조)

### 2단계: PostgreSQL에 데이터 삽입

```bash
python insert_to_postgres.py
```

**데이터베이스 정보**:
- Host: 10.0.0.20
- Port: 2332
- Database: dde-water
- Schema: design_standard
- Table: design_sections (238 rows)

## 📊 데이터 통계

### 재구성 결과
| 항목 | 재구성 전 | 재구성 후 |
|------|-----------|-----------|
| 총 섹션 수 | 26 | 238 |
| Level 1 | 4 | 28 |
| Level 2 | 12 | 179 |
| Level 3 | 10 | 31 |

### 문제 해결
- ✅ 섹션 3, 4번: 평면 구조 → 계층 구조 변환 (6개 + 3개 하위 섹션 생성)
- ✅ 이스케이프된 개행 문자(`\n`) 처리
- ✅ 부모-자식 관계 재구성

## 🗄️ 데이터베이스 스키마

### design_sections 테이블

| 컬럼 | 타입 | 설명 |
|------|------|------|
| id | SERIAL | 자동 증가 ID (PRIMARY KEY) |
| code | VARCHAR(50) | 섹션 코드 (예: "1.1.1") UNIQUE |
| title | TEXT | 섹션 제목 |
| content | TEXT | 섹션 본문 내용 |
| parent_code | VARCHAR(50) | 부모 섹션 코드 (FOREIGN KEY) |
| level | INTEGER | 계층 레벨 (1, 2, 3, ...) |
| sort_order | INTEGER | 정렬 순서 |
| created_at | TIMESTAMP | 생성 시간 |
| updated_at | TIMESTAMP | 수정 시간 |

### 인덱스
- `idx_sections_code`: code 컬럼
- `idx_sections_parent_code`: parent_code 컬럼
- `idx_sections_level`: level 컬럼
- `idx_sections_content_gin`: 전문 검색용 GIN 인덱스
- `idx_sections_title_gin`: 제목 검색용 GIN 인덱스

### 뷰 및 함수
- `v_section_tree`: 계층 구조 트리 뷰
- `search_sections(text)`: 키워드 검색 함수

## 🔍 사용 예시

### DBeaver에서 데이터 조회

```sql
-- 1. 전체 섹션 조회
SELECT * FROM design_standard.design_sections
ORDER BY code;

-- 2. 최상위 섹션만 조회
SELECT code, title FROM design_standard.design_sections
WHERE parent_code IS NULL
ORDER BY code;

-- 3. 계층 구조 확인 (섹션 1 하위)
SELECT * FROM design_standard.v_section_tree
WHERE code LIKE '1.%';

-- 4. 키워드 검색
SELECT * FROM design_standard.search_sections('응집');

-- 5. 특정 섹션의 자식 개수
SELECT
    parent.code,
    parent.title,
    COUNT(child.id) as children_count
FROM design_standard.design_sections parent
LEFT JOIN design_standard.design_sections child
    ON child.parent_code = parent.code
GROUP BY parent.code, parent.title
ORDER BY children_count DESC;
```

### Python에서 사용

```python
import psycopg2
import json

# 데이터베이스 연결
conn = psycopg2.connect(
    host='10.0.0.20',
    port=2332,
    database='dde-water',
    user='postgres',
    password='postgres'
)

# 섹션 조회
cursor = conn.cursor()
cursor.execute("""
    SELECT code, title, content
    FROM design_standard.design_sections
    WHERE code = %s
""", ('1.1.1',))

result = cursor.fetchone()
print(f"Code: {result[0]}")
print(f"Title: {result[1]}")
print(f"Content: {result[2][:100]}...")

cursor.close()
conn.close()
```

## 📚 상세 문서

- **[데이터베이스 설정 가이드](README_DB_SETUP.md)**: DBeaver 연결, 쿼리 예시, 트러블슈팅
- **[Jupyter 노트북](restructure_json.ipynb)**: 대화형으로 재구성 과정 실행

## 🛠️ 기술 스택

- **Python 3.11+**
- **PostgreSQL** (with psycopg2-binary)
- **JSON** (표준 라이브러리)
- **정규표현식** (re 모듈)

## 📦 의존성

```bash
pip install psycopg2-binary
```

## 🔄 워크플로우

```
원본 JSON 파일
(평면 구조)
    ↓
[run_restructure.py]
    ↓
재구성된 JSON 파일
(계층 구조)
    ↓
[insert_to_postgres.py]
    ↓
PostgreSQL 데이터베이스
(design_standard.design_sections)
    ↓
[RAG 시스템에서 활용]
- 벡터 검색
- 계층 구조 탐색
- 전문 검색
```

## 🎯 주요 기능

### 1. JSON 재구성
- ✅ 평면 구조를 계층 구조로 자동 변환
- ✅ 이스케이프된 개행 문자 처리
- ✅ 코드 기반 부모-자식 관계 재구성
- ✅ 검증 및 통계 출력

### 2. 데이터베이스 저장
- ✅ 자동 테이블 생성
- ✅ 계층 구조 보존
- ✅ 전문 검색 인덱스
- ✅ 재귀 쿼리 지원

### 3. 검색 기능
- ✅ 키워드 검색 (제목 + 내용)
- ✅ 코드 기반 검색
- ✅ 계층 구조 탐색
- ✅ 유사도 순위 (ts_rank)

## 🔮 향후 계획

- [ ] 벡터 임베딩 추가 (pgvector 확장)
- [ ] RAG 시스템 통합
- [ ] 웹 인터페이스 개발
- [ ] API 서버 구축
- [ ] 검색 성능 최적화

## 📝 라이선스

이 프로젝트는 내부 사용을 위한 것입니다.

## 👥 기여

문의사항이나 개선 제안은 프로젝트 관리자에게 연락하세요.

---

**Last Updated**: 2025-11-19
**Version**: 1.0.0
