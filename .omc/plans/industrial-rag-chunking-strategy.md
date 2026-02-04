# 산업계 RAG 청킹 전략 수립 계획

## Context

### Original Request
산업계 RAG 시스템 도입을 위한 최적의 청킹 전략 수립. 고정 크기 청킹의 한계를 극복하고, 의미론적 청킹, 멀티모달 처리, GraphRAG 통합을 포함하는 종합적인 청킹 파이프라인 설계.

### Current State
- **데이터베이스**: PostgreSQL (10.0.0.20:2332/dde-water)
- **스키마**: design_standard.design_sections
- **데이터**: 238개 계층 구조 섹션 (설계 표준 문서)
- **인덱스**: GIN 전문 검색 인덱스 구축 완료
- **향후 계획**: pgvector 확장을 통한 벡터 임베딩 추가

### Problem Statement
1. 고정 크기 청킹은 문서 구조를 파괴함 (표 분리, 제목-값 분리)
2. 멀티모달 콘텐츠(이미지, 다이어그램) 처리 부재
3. 엔티티 간 관계 정보 손실
4. 글로벌 컨텍스트 이해 부족

---

## Work Objectives

### Core Objective
산업계 문서 특성에 맞는 다층 청킹 파이프라인을 구축하여 RAG 시스템의 검색 품질과 응답 정확도를 향상시킨다.

### Deliverables
1. 문서 유형별 청킹 전략 명세서
2. 청킹 파이프라인 아키텍처 설계서
3. GraphRAG 통합 모듈 설계서
4. 멀티모달 처리 모듈 설계서
5. 구현 로드맵 및 마일스톤

### Definition of Done
- [ ] 모든 문서 유형(구조화/반구조화/비구조화)에 대한 청킹 전략 정의
- [ ] 파이프라인 각 단계의 입출력 스펙 정의
- [ ] GraphRAG 엔티티/관계 추출 스키마 정의
- [ ] 멀티모달 처리 워크플로우 정의
- [ ] 단계별 구현 일정 및 기술 스택 확정
- [ ] 평가 지표 및 벤치마크 기준 정의

---

## Guardrails

### Must Have
- 기존 PostgreSQL 인프라(design_standard 스키마) 활용
- 계층 구조 메타데이터 보존
- 한글 문서 처리 최적화
- 점진적 구현 가능한 모듈식 설계
- 롤백 가능한 단계별 마이그레이션
- **GraphRAG 논문 기준 청킹 파라미터 준수 (기본값: 600 토큰, 100 오버랩)**

### Must NOT Have
- 기존 238개 섹션 데이터 손실
- 단일 벤더 종속 아키텍처
- 실시간 처리 요구사항 (배치 처리 우선)
- 과도한 LLM API 비용 발생 구조 **(월 $100 초과 금지)**

---

## Rollback Strategy & Checkpoints

### Checkpoint 정의

```
┌─────────────────────────────────────────────────────────────┐
│                    CHECKPOINT STRATEGY                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Phase 1 완료 → CHECKPOINT 1                                │
│    - 스냅샷: design_standard 스키마 전체                     │
│    - 백업 명령: pg_dump -n design_standard > cp1.sql        │
│                                                             │
│  Phase 2 완료 → CHECKPOINT 2                                │
│    - 스냅샷: design_sections + chunks 테이블                │
│    - 백업 명령: pg_dump -t design_standard.* > cp2.sql      │
│                                                             │
│  Phase 3 완료 → CHECKPOINT 3                                │
│    - 스냅샷: entities, relationships 추가                   │
│    - 백업 명령: pg_dump -n design_standard > cp3.sql        │
│                                                             │
│  Phase 4 완료 → CHECKPOINT 4                                │
│    - 스냅샷: 멀티모달 메타데이터 포함                        │
│    - 백업 명령: pg_dump -n design_standard > cp4.sql        │
│                                                             │
│  Phase 5 완료 → CHECKPOINT 5 (FINAL)                        │
│    - 스냅샷: 전체 시스템 (인덱스 포함)                       │
│    - 백업 명령: pg_dump -n design_standard > final.sql      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Rollback 절차

```sql
-- 롤백 시 실행할 SQL 명령어 (Phase별)

-- Phase 5 → Phase 4 롤백
DROP INDEX IF EXISTS design_standard.idx_hybrid_search;
-- 검색 통합 설정 제거

-- Phase 4 → Phase 3 롤백
DROP TABLE IF EXISTS design_standard.multimodal_assets CASCADE;
-- 멀티모달 데이터 제거

-- Phase 3 → Phase 2 롤백
DROP TABLE IF EXISTS design_standard.entities CASCADE;
DROP TABLE IF EXISTS design_standard.relationships CASCADE;
DROP TABLE IF EXISTS design_standard.community_summaries CASCADE;
-- GraphRAG 데이터 제거

-- Phase 2 → Phase 1 롤백
DROP TABLE IF EXISTS design_standard.chunks CASCADE;
DROP TABLE IF EXISTS design_standard.section_chunk_mapping CASCADE;
-- 청크 데이터 제거, design_sections 원본 유지

-- Phase 1 → 초기 상태 롤백
-- design_sections 테이블 원본 복원
psql -f cp1.sql
```

### 자동 롤백 트리거 조건

| 조건 | 트리거 | 롤백 대상 |
|------|--------|-----------|
| 청크 생성 실패율 > 10% | Phase 2 | CHECKPOINT 1로 복원 |
| 엔티티 추출 비용 > $50/batch | Phase 3 | CHECKPOINT 2로 복원 |
| 데이터 무결성 검증 실패 | Any Phase | 직전 CHECKPOINT로 복원 |
| design_sections 데이터 손실 감지 | Any Phase | CHECKPOINT 1로 복원 |

---

## Task Flow

```
[Phase 1: Foundation]
    |
    +-- TODO-1: 문서 분류 체계 수립
    +-- TODO-2: 청킹 파이프라인 아키텍처 설계
    +-- TODO-2.5: design_sections → chunks 마이그레이션 설계  ← NEW
    |
    ├── ★ CHECKPOINT 1 (DB 스냅샷)
    |
[Phase 2: Core Chunking]
    |
    +-- TODO-3: 의미론적 청킹 모듈 설계 (GraphRAG 기준 적용)
    +-- TODO-4: 구조 보존 청킹 구현
    |
    ├── ★ CHECKPOINT 2 (DB 스냅샷)
    |
[Phase 3: GraphRAG Integration]
    |
    +-- TODO-5: 엔티티/관계 추출 스키마 설계
    +-- TODO-5.5: LLM 비용 검증 (50개 샘플)  ← NEW
    +-- TODO-6: 커뮤니티 탐지 및 요약 설계
    |
    ├── ★ CHECKPOINT 3 (DB 스냅샷)
    |
[Phase 4: Multimodal]
    |
    +-- TODO-7: 표/다이어그램 처리 모듈 설계
    +-- TODO-8: 이미지-텍스트 정합 전략 수립
    |
    ├── ★ CHECKPOINT 4 (DB 스냅샷)
    |
[Phase 5: Integration & Evaluation]
    |
    +-- TODO-9: 하이브리드 검색 통합 설계
    +-- TODO-10: 평가 프레임워크 구축
    |
    └── ★ CHECKPOINT 5 (FINAL)
```

---

## Detailed TODOs

### Phase 1: Foundation (Week 1-2)

#### TODO-1: 문서 분류 체계 수립
**Priority**: HIGH
**Estimated Effort**: 2일
**Dependencies**: None

**Description**:
산업계 문서를 유형별로 분류하고 각 유형의 특성을 정의한다.

**Acceptance Criteria**:
- [ ] 3가지 문서 유형 정의 및 특성 문서화
- [ ] 각 유형별 샘플 문서 식별
- [ ] 유형 자동 감지 규칙 정의

**Implementation Details**:

```
문서 유형 분류 체계
====================

1. 구조화된 문서 (Structured Documents)
   - 설계 표준, 기술 매뉴얼, 규격서
   - 특성:
     * 명확한 섹션 번호 체계 (1.1, 1.1.1)
     * 표, 수식, 도면 참조 포함
     * 용어 정의 섹션 존재
   - 청킹 전략: 섹션 경계 기반 + 표 보존

2. 반구조화 문서 (Semi-structured Documents)
   - 기술 보고서, 회의록, 검토 의견서
   - 특성:
     * 일부 섹션 구조 존재
     * 자유 텍스트와 구조화 요소 혼재
     * 시간순 또는 주제별 구성
   - 청킹 전략: 의미론적 경계 탐지 + 문맥 오버랩

3. 비구조화 문서 (Unstructured Documents)
   - 이메일, 자유 형식 메모, 일지
   - 특성:
     * 고정 구조 없음
     * 대화체 또는 서술체
     * 암묵적 참조 다수
   - 청킹 전략: 고정 크기 + 의미론적 완결성 검증
```

---

#### TODO-2: 청킹 파이프라인 아키텍처 설계
**Priority**: HIGH
**Estimated Effort**: 3일
**Dependencies**: TODO-1

**Description**:
전처리-청킹-후처리 3단계 파이프라인의 전체 아키텍처를 설계한다.

**Acceptance Criteria**:
- [ ] 파이프라인 3단계 상세 설계서 작성
- [ ] 각 단계 입출력 스키마 정의
- [ ] 에러 처리 및 롤백 전략 정의
- [ ] **pgvector 버전 호환성 검증 (PostgreSQL 15+ 확인)**

**Implementation Details**:

```
청킹 파이프라인 아키텍처
========================

┌─────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                               │
│  - Raw Documents (PDF, DOCX, JSON)                          │
│  - Existing DB Records (design_sections)                    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 1: PREPROCESSING                          │
├─────────────────────────────────────────────────────────────┤
│  1.1 Document Type Detection                                │
│      - 규칙 기반 분류 + ML 보조                              │
│      - Output: document_type enum                           │
│                                                             │
│  1.2 Layout Analysis                                        │
│      - Azure Document Intelligence / PyMuPDF                │
│      - Output: layout_elements[]                            │
│                                                             │
│  1.3 Multimodal Extraction                                  │
│      - 표: tabula-py, camelot                               │
│      - 이미지: GPT-4o vision / OCR                          │
│      - Output: extracted_elements[]                         │
│                                                             │
│  1.4 Text Normalization                                     │
│      - 한글 정규화 (자모 분리 처리)                          │
│      - 특수문자, 공백 정규화                                 │
│      - Output: normalized_text                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 2: CHUNKING                               │
├─────────────────────────────────────────────────────────────┤
│  2.1 Structural Chunking (구조화 문서)                       │
│      - 섹션 번호 경계 감지                                   │
│      - 계층 메타데이터 보존                                  │
│      - 표/이미지 참조 유지                                   │
│                                                             │
│  2.2 Semantic Chunking (반구조화 문서)                       │
│      - 문장 임베딩 유사도 기반 경계 탐지                     │
│      - 토픽 전환점 감지                                      │
│      - ★ GraphRAG 기준: 600 토큰, 100 오버랩 (기본값)       │
│                                                             │
│  2.3 Hybrid Chunking (비구조화 문서)                         │
│      - 기본 크기: 600 토큰 (GraphRAG 기준)                   │
│      - 의미론적 완결성 검증                                  │
│      - 필요시 경계 조정                                      │
│                                                             │
│  Output Schema:                                             │
│  {                                                          │
│    chunk_id: UUID,                                          │
│    content: string,                                         │
│    metadata: {                                              │
│      source_doc_id: string,                                 │
│      section_code: string,      // 계층 코드                │
│      parent_chunk_id: UUID,                                 │
│      level: int,                                            │
│      chunk_type: enum,          // text/table/image         │
│      token_count: int,                                      │
│      position: {start: int, end: int}                       │
│    },                                                       │
│    references: {                                            │
│      tables: UUID[],                                        │
│      images: UUID[],                                        │
│      related_chunks: UUID[]                                 │
│    }                                                        │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 3: POST-PROCESSING                        │
├─────────────────────────────────────────────────────────────┤
│  3.1 Chunk Validation                                       │
│      - 최소/최대 크기 검증                                   │
│      - 의미론적 완결성 점검                                  │
│      - 참조 무결성 검증                                      │
│                                                             │
│  3.2 Metadata Enrichment                                    │
│      - 키워드 추출 (TF-IDF, KeyBERT)                         │
│      - 요약 생성 (선택적)                                    │
│      - 난이도/복잡도 점수                                    │
│                                                             │
│  3.3 Embedding Generation                                   │
│      - 모델: text-embedding-3-small (OpenAI)                │
│      - 또는: multilingual-e5-large (로컬)                   │
│      - 배치 처리 (100개 단위)                                │
│                                                             │
│  3.4 Index Building                                         │
│      - pgvector 인덱스 (IVFFlat/HNSW)                        │
│      - 전문 검색 인덱스 갱신                                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                              │
│  - PostgreSQL: chunks table + vectors                       │
│  - Neo4j (optional): Knowledge Graph                        │
│  - Elasticsearch (optional): Full-text search               │
└─────────────────────────────────────────────────────────────┘
```

---

#### TODO-2.5: design_sections → chunks 마이그레이션 설계 (NEW)
**Priority**: HIGH
**Estimated Effort**: 2일
**Dependencies**: TODO-2

**Description**:
기존 238개 design_sections 데이터를 새로운 chunks 테이블로 변환하는 마이그레이션 전략을 설계한다.

**Acceptance Criteria**:
- [ ] design_sections → chunks 마이그레이션 스크립트 설계
- [ ] 기존 section_code와 chunk_id 간 매핑 테이블 정의
- [ ] 마이그레이션 검증 쿼리 작성
- [ ] 롤백 스크립트 작성

**Implementation Details**:

```
마이그레이션 흐름 다이어그램
============================

┌─────────────────────────────────────────────────────────────┐
│              EXISTING: design_sections                       │
│  - 238 rows                                                 │
│  - Fields: id, section_code, title, content, parent_id...  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Step 1: 스냅샷 생성
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              CHECKPOINT 1: BACKUP                            │
│  pg_dump -t design_standard.design_sections > backup.sql    │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Step 2: 매핑 테이블 생성
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              NEW: section_chunk_mapping                      │
│  - section_id: FK → design_sections.id                      │
│  - chunk_id: FK → chunks.id                                 │
│  - chunk_index: 섹션 내 청크 순서 (0, 1, 2...)              │
│  - is_primary: 대표 청크 여부                                │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Step 3: 청킹 실행
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              NEW: chunks                                     │
│  - 예상 ~500-800 chunks (238 sections × 2-3 avg)            │
│  - section_code 메타데이터로 원본 추적 가능                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Step 4: 검증
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              VALIDATION QUERIES                              │
│  - SELECT COUNT(*) FROM section_chunk_mapping               │
│    WHERE section_id NOT IN (SELECT id FROM design_sections) │
│    → 결과: 0 (모든 섹션 매핑됨)                              │
│                                                             │
│  - SELECT section_code, COUNT(chunk_id)                     │
│    FROM chunks GROUP BY section_code                        │
│    → 각 섹션별 청크 수 확인                                  │
└─────────────────────────────────────────────────────────────┘
```

**매핑 테이블 스키마**:

```sql
-- 섹션-청크 매핑 테이블
CREATE TABLE design_standard.section_chunk_mapping (
    id SERIAL PRIMARY KEY,
    section_id INTEGER NOT NULL REFERENCES design_standard.design_sections(id),
    chunk_id UUID NOT NULL REFERENCES design_standard.chunks(id),
    chunk_index INTEGER NOT NULL DEFAULT 0,  -- 섹션 내 순서
    is_primary BOOLEAN NOT NULL DEFAULT false,  -- 대표 청크
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(section_id, chunk_id)
);

-- 인덱스
CREATE INDEX idx_mapping_section ON design_standard.section_chunk_mapping(section_id);
CREATE INDEX idx_mapping_chunk ON design_standard.section_chunk_mapping(chunk_id);
CREATE INDEX idx_mapping_primary ON design_standard.section_chunk_mapping(is_primary) WHERE is_primary = true;
```

**마이그레이션 스크립트 구조**:

```python
class MigrationManager:
    """design_sections → chunks 마이그레이션 관리"""

    def __init__(self, db_connection):
        self.db = db_connection
        self.chunker = StructuralChunker(config=GRAPHRAG_DEFAULTS)

    def create_checkpoint(self, checkpoint_name: str):
        """Phase 시작 전 스냅샷 생성"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"checkpoints/{checkpoint_name}_{timestamp}.sql"
        subprocess.run([
            'pg_dump', '-h', HOST, '-p', PORT, '-U', USER,
            '-n', 'design_standard', '-f', backup_file, DB_NAME
        ])
        return backup_file

    def migrate_section(self, section_id: int) -> List[UUID]:
        """단일 섹션을 청크로 변환"""
        section = self.db.get_section(section_id)
        chunks = self.chunker.chunk_section(section)

        chunk_ids = []
        for i, chunk in enumerate(chunks):
            chunk_id = self.db.insert_chunk(chunk)
            chunk_ids.append(chunk_id)

            # 매핑 테이블 업데이트
            self.db.insert_mapping(
                section_id=section_id,
                chunk_id=chunk_id,
                chunk_index=i,
                is_primary=(i == 0)
            )

        return chunk_ids

    def validate_migration(self) -> dict:
        """마이그레이션 검증"""
        return {
            'total_sections': self.db.count_sections(),
            'migrated_sections': self.db.count_mapped_sections(),
            'total_chunks': self.db.count_chunks(),
            'orphan_chunks': self.db.count_orphan_chunks(),
            'missing_sections': self.db.find_missing_sections()
        }

    def rollback_to_checkpoint(self, backup_file: str):
        """체크포인트로 롤백"""
        # 현재 테이블 삭제
        self.db.execute("DROP TABLE IF EXISTS design_standard.chunks CASCADE")
        self.db.execute("DROP TABLE IF EXISTS design_standard.section_chunk_mapping CASCADE")

        # 백업 복원
        subprocess.run(['psql', '-h', HOST, '-p', PORT, '-U', USER, '-f', backup_file, DB_NAME])
```

---

### Phase 2: Core Chunking (Week 3-4)

#### TODO-3: 의미론적 청킹 모듈 설계
**Priority**: HIGH
**Estimated Effort**: 4일
**Dependencies**: TODO-2

**Description**:
문장/문단 임베딩 유사도를 기반으로 의미론적 경계를 탐지하는 청킹 모듈을 설계한다. **GraphRAG 논문 기준(600 토큰, 100 오버랩)을 기본값으로 적용한다.**

**Acceptance Criteria**:
- [ ] 유사도 기반 경계 탐지 알고리즘 명세
- [ ] **GraphRAG 논문 기준 파라미터를 기본값으로 적용 (max_tokens=600, overlap_tokens=100)**
- [ ] 한글 문장 분리기 선정 및 테스트
- [ ] **kss 문장 분리기의 설계 표준 문서 적합성 테스트 (20개 샘플)**
- [ ] **대안 문장 분리기 비교 평가 (koalanlp, kiwipiepy)**
- [ ] 최적 청크 크기 파라미터 실험 결과

**Implementation Details**:

```python
# 의미론적 청킹 알고리즘 설계

# ========================================
# GraphRAG 논문 기준 기본값 (CRITICAL)
# ========================================
GRAPHRAG_DEFAULTS = {
    'max_tokens': 600,      # 논문 기준
    'overlap_tokens': 100,  # 논문 기준
    'min_tokens': 100,      # 최소 청크 크기
    'similarity_threshold': 0.5
}

class SemanticChunker:
    """
    문장 임베딩 유사도 기반 의미론적 청킹

    ★ GraphRAG 논문 기준: max_tokens=600, overlap_tokens=100

    알고리즘:
    1. 문장 분리 (kss 라이브러리 - 한국어 특화)
    2. 각 문장 임베딩 생성
    3. 연속 문장 간 코사인 유사도 계산
    4. 유사도 급감 지점을 경계로 설정
    5. 최소/최대 크기 제약 적용
    """

    def __init__(self, config: ChunkingConfig = None):
        # GraphRAG 논문 기준을 기본값으로 사용
        config = config or ChunkingConfig(**GRAPHRAG_DEFAULTS)

        self.min_chunk_tokens = config.min_tokens      # 100
        self.max_chunk_tokens = config.max_tokens      # 600 (GraphRAG 기준)
        self.similarity_threshold = config.threshold   # 0.5
        self.overlap_tokens = config.overlap           # 100 (GraphRAG 기준)

        # 문장 분리기 (테스트 후 선정)
        self.sentence_splitter = self._init_splitter(config.splitter)

    def _init_splitter(self, splitter_name: str):
        """문장 분리기 초기화 (테스트 결과에 따라 선정)"""
        splitters = {
            'kss': KssSplitter(),           # 기본
            'koalanlp': KoalaNLPSplitter(),  # 대안 1
            'kiwipiepy': KiwiSplitter()      # 대안 2
        }
        return splitters.get(splitter_name, splitters['kss'])

    def chunk(self, text: str) -> List[Chunk]:
        # 1. 문장 분리
        sentences = self.sentence_splitter.split(text)

        # 2. 문장 임베딩
        embeddings = self.embed_sentences(sentences)

        # 3. 경계 탐지
        boundaries = self.detect_boundaries(embeddings)

        # 4. 청크 생성 (max_tokens=600 기준)
        chunks = self.create_chunks(sentences, boundaries)

        # 5. 오버랩 추가 (overlap_tokens=100 기준)
        chunks = self.add_overlap(chunks)

        return chunks

    def detect_boundaries(self, embeddings: np.ndarray) -> List[int]:
        """
        유사도 급감 지점 탐지
        - 이전 문장과의 유사도가 threshold 이하로 떨어지는 지점
        - Percentile 기반 동적 threshold도 고려
        """
        similarities = []
        for i in range(1, len(embeddings)):
            sim = cosine_similarity(embeddings[i-1], embeddings[i])
            similarities.append(sim)

        # 급감 지점 탐지 (threshold 기반)
        boundaries = [0]
        for i, sim in enumerate(similarities):
            if sim < self.similarity_threshold:
                boundaries.append(i + 1)
        boundaries.append(len(embeddings))

        return boundaries
```

**한글 문장 분리기 비교 평가**:

```
문장 분리기 비교 테스트 프로토콜
================================

테스트 샘플: design_sections에서 무작위 20개 섹션 선택
평가 기준:
  1. 정확도: 수동 라벨링 대비 F1 score
  2. 속도: 1000문장 처리 시간
  3. 특수 케이스 처리:
     - 숫자+마침표 (3.1, 제4조.)
     - 괄호 내 마침표 (예: 참조.)
     - 표/수식 경계

| 분리기    | 예상 장점           | 예상 단점           | 테스트 우선순위 |
|-----------|---------------------|---------------------|-----------------|
| kss       | 한국어 특화, 빠름   | 기술 문서 미검증    | 1               |
| kiwipiepy | 형태소 분석 통합    | 설치 복잡           | 2               |
| koalanlp  | 다양한 분석기 지원  | Java 의존성         | 3               |

테스트 결과 기록:
  - 각 분리기별 20개 샘플 결과 저장
  - 실패 케이스 분석
  - 최종 선정 근거 문서화
```

**청크 크기 가이드라인 (GraphRAG 기준 변형)**:

| 문서 유형 | 기본값 | 최소 토큰 | 최대 토큰 | 오버랩 | 근거 |
|-----------|--------|-----------|-----------|--------|------|
| **기준 (GraphRAG)** | **적용** | **100** | **600** | **100** | **논문 기준** |
| 구조화 문서 | 변형 | 200 | 800 | 50 | 섹션 완결성 우선 |
| 반구조화 문서 | 기준 | 100 | 600 | 100 | GraphRAG 기준 적용 |
| 비구조화 문서 | 변형 | 100 | 500 | 150 | 의미 완결성 보장 |

---

#### TODO-4: 구조 보존 청킹 구현
**Priority**: HIGH
**Estimated Effort**: 4일
**Dependencies**: TODO-3

**Description**:
설계 표준 문서의 계층 구조와 표/수식 참조를 보존하는 청킹 로직을 설계한다.

**Acceptance Criteria**:
- [ ] 섹션 코드 기반 청킹 알고리즘 명세
- [ ] 표/수식 청크 분리 및 참조 연결 전략
- [ ] 기존 design_sections 테이블과의 매핑 전략 (TODO-2.5 연계)

**Implementation Details**:

```python
# 구조 보존 청킹 설계

class StructuralChunker:
    """
    계층 구조 보존 청킹

    원칙:
    1. 섹션 경계 존중 - 섹션을 넘어가는 청크 생성 금지
    2. 표/이미지 독립 청크화 - 별도 청크로 분리 후 참조 연결
    3. 제목-내용 동반 - 제목과 첫 문단은 항상 같은 청크
    4. 계층 메타데이터 보존 - parent_code, level 정보 유지
    5. ★ GraphRAG 기준 적용 - max_tokens=600 (구조화 문서는 800까지 허용)
    """

    def __init__(self, config: ChunkingConfig = None):
        config = config or ChunkingConfig(**GRAPHRAG_DEFAULTS)
        # 구조화 문서는 섹션 완결성을 위해 최대 토큰 확장
        self.max_tokens = min(config.max_tokens * 1.33, 800)  # 600 → 800
        self.overlap_tokens = config.overlap // 2  # 100 → 50

    def chunk_section(self, section: Section) -> List[Chunk]:
        chunks = []

        # 1. 표/이미지 추출 및 별도 청킹
        tables, images, clean_content = self.extract_elements(
            section.content
        )

        for table in tables:
            chunks.append(Chunk(
                content=table.to_markdown(),
                chunk_type='table',
                metadata={
                    'section_code': section.code,
                    'table_id': table.id,
                    'caption': table.caption
                }
            ))

        # 2. 텍스트 청킹 (섹션 경계 내에서)
        if len(clean_content) <= self.max_tokens:
            # 섹션 전체가 하나의 청크
            chunks.append(Chunk(
                content=f"## {section.title}\n\n{clean_content}",
                chunk_type='text',
                metadata={
                    'section_code': section.code,
                    'parent_code': section.parent_code,
                    'level': section.level
                },
                references={
                    'tables': [t.id for t in tables],
                    'images': [i.id for i in images]
                }
            ))
        else:
            # 섹션 내 의미론적 분할
            sub_chunks = self.semantic_split(clean_content)
            for i, sub in enumerate(sub_chunks):
                prefix = f"## {section.title}\n\n" if i == 0 else ""
                chunks.append(Chunk(
                    content=prefix + sub,
                    chunk_type='text',
                    metadata={
                        'section_code': section.code,
                        'sub_index': i,
                        'parent_code': section.parent_code,
                        'level': section.level
                    }
                ))

        return chunks
```

**표 처리 전략**:

```
표 청킹 전략
============

1. 표 감지
   - Markdown 표: |로 시작하는 연속 라인
   - HTML 표: <table> 태그
   - ASCII 표: +-+로 구성된 패턴

2. 표 독립 청킹
   - 표 전체를 하나의 청크로 유지
   - 캡션/제목을 표 청크에 포함
   - 표가 너무 크면 행 단위로 분할

3. 참조 연결
   - 원본 텍스트에 "[표 참조: table_chunk_id]" 삽입
   - 검색 시 관련 표 청크도 함께 반환

예시:
-----
원본: "다음 표 3.1은 응집 기준을 보여준다. [표 3.1]"

청크 1 (텍스트):
  content: "다음 표 3.1은 응집 기준을 보여준다. [표 참조: chunk_uuid_123]"
  references: {tables: ["chunk_uuid_123"]}

청크 2 (표):
  chunk_id: "chunk_uuid_123"
  content: "| 구분 | 기준 | 비고 |\n|---|---|---|\n| 응집1 | ... |"
  chunk_type: "table"
  metadata: {caption: "표 3.1 응집 기준"}
```

---

### Phase 3: GraphRAG Integration (Week 5-6)

#### TODO-5: 엔티티/관계 추출 스키마 설계
**Priority**: MEDIUM
**Estimated Effort**: 4일
**Dependencies**: TODO-4

**Description**:
설계 표준 도메인에 특화된 엔티티 유형과 관계 유형을 정의하고, LLM 기반 추출 프롬프트를 설계한다.

**Acceptance Criteria**:
- [ ] 도메인 특화 엔티티 타입 정의 (최소 10개)
- [ ] 관계 타입 정의 (최소 8개)
- [ ] 엔티티/관계 추출 프롬프트 템플릿
- [ ] PostgreSQL 스키마 확장안

**Implementation Details**:

```
엔티티 유형 정의 (설계 표준 도메인)
====================================

1. STANDARD (표준/규격)
   - 설계 기준, KS 표준, 해외 표준
   - 속성: code, name, version, issuing_body

2. PARAMETER (설계 파라미터)
   - 수치 기준값, 허용 범위
   - 속성: name, value, unit, min, max

3. EQUIPMENT (설비/장비)
   - 펌프, 밸브, 배관 등
   - 속성: name, type, specification

4. MATERIAL (재료)
   - 콘크리트, 철근, 배관재
   - 속성: name, grade, properties

5. PROCESS (공정/프로세스)
   - 응집, 침전, 여과 등
   - 속성: name, type, conditions

6. FORMULA (수식/계산식)
   - 설계 계산식
   - 속성: name, expression, variables

7. CONDITION (조건/제약)
   - 설계 조건, 환경 조건
   - 속성: name, type, value

8. REFERENCE (참조 문서)
   - 다른 섹션, 외부 문서 참조
   - 속성: code, title, type

9. TERM (용어 정의)
   - 전문 용어
   - 속성: term, definition, domain

10. LOCATION (위치/구역)
    - 시설 위치, 설치 구역
    - 속성: name, type, coordinates


관계 유형 정의
==============

1. REFERENCES (참조)
   - A가 B를 참조함
   - 예: "섹션 3.1" → REFERENCES → "KS F 4009"

2. SPECIFIES (명세)
   - A가 B의 값을 명세함
   - 예: "응집지 기준" → SPECIFIES → "체류시간 30분"

3. REQUIRES (요구)
   - A가 B를 요구함
   - 예: "고속응집" → REQUIRES → "급속교반기"

4. CONTAINS (포함)
   - A가 B를 포함함
   - 예: "정수처리공정" → CONTAINS → "응집"

5. FOLLOWS (후속)
   - A가 B 다음에 수행됨
   - 예: "침전" → FOLLOWS → "응집"

6. CALCULATES (계산)
   - A로 B를 계산함
   - 예: "체류시간 공식" → CALCULATES → "체류시간"

7. APPLIES_TO (적용 대상)
   - A가 B에 적용됨
   - 예: "내진 설계 기준" → APPLIES_TO → "콘크리트 구조물"

8. CONSTRAINED_BY (제약)
   - A가 B에 의해 제약됨
   - 예: "밸브 설치" → CONSTRAINED_BY → "최소 이격거리"
```

**PostgreSQL 스키마 확장**:

```sql
-- 엔티티 테이블
CREATE TABLE design_standard.entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    properties JSONB,
    source_chunk_id UUID REFERENCES design_standard.chunks(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 관계 테이블
CREATE TABLE design_standard.relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_entity_id UUID REFERENCES design_standard.entities(id),
    target_entity_id UUID REFERENCES design_standard.entities(id),
    relationship_type VARCHAR(50) NOT NULL,
    properties JSONB,
    source_chunk_id UUID REFERENCES design_standard.chunks(id),
    confidence REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 인덱스
CREATE INDEX idx_entities_type ON design_standard.entities(entity_type);
CREATE INDEX idx_entities_name_gin ON design_standard.entities USING gin(name gin_trgm_ops);
CREATE INDEX idx_relationships_type ON design_standard.relationships(relationship_type);
```

**LLM 추출 프롬프트**:

```
엔티티/관계 추출 프롬프트
=========================

시스템 프롬프트:
"""
당신은 설계 표준 문서에서 기술 엔티티와 관계를 추출하는 전문가입니다.

엔티티 유형:
- STANDARD: 표준/규격 (KS, ISO 등)
- PARAMETER: 설계 파라미터 (수치 기준)
- EQUIPMENT: 설비/장비
- MATERIAL: 재료
- PROCESS: 공정/프로세스
- FORMULA: 수식/계산식
- CONDITION: 조건/제약
- REFERENCE: 참조 문서
- TERM: 용어 정의

관계 유형:
- REFERENCES, SPECIFIES, REQUIRES, CONTAINS
- FOLLOWS, CALCULATES, APPLIES_TO, CONSTRAINED_BY

JSON 형식으로 출력하세요.
"""

사용자 프롬프트:
"""
다음 텍스트에서 엔티티와 관계를 추출하세요:

---
{chunk_content}
---

출력 형식:
{
  "entities": [
    {"name": "...", "type": "...", "properties": {...}}
  ],
  "relationships": [
    {"source": "...", "target": "...", "type": "...", "evidence": "..."}
  ]
}
"""
```

---

#### TODO-5.5: LLM 비용 검증 - 50개 샘플 테스트 (NEW)
**Priority**: HIGH
**Estimated Effort**: 1일
**Dependencies**: TODO-5

**Description**:
Phase 3 전체 적용 전 50개 청크 샘플로 LLM API 비용을 검증하고, 비용 임계값 초과 시 대안 전략을 결정한다.

**Acceptance Criteria**:
- [ ] 50개 샘플 청크로 엔티티 추출 실행
- [ ] 실제 API 호출 횟수 및 비용 측정
- [ ] 전체 적용 시 예상 비용 추정
- [ ] 비용 임계값 ($100/월) 초과 여부 판단
- [ ] 초과 시 대안 전략 결정 (로컬 모델 전환 등)

**Implementation Details**:

```
LLM 비용 검증 프로토콜
======================

1. 샘플 선정
   - design_sections에서 무작위 50개 섹션 선택
   - 청킹 후 약 100-150개 청크 예상
   - 다양한 길이/복잡도 포함

2. 비용 추정 공식

   예상 총 청크 수: ~600개 (238 sections × 2.5 avg)

   GPT-4o 비용 (2024 기준):
   - Input: $2.50 / 1M tokens
   - Output: $10.00 / 1M tokens

   청크당 예상:
   - Input: ~800 tokens (프롬프트 + 청크)
   - Output: ~200 tokens (엔티티/관계 JSON)

   50개 샘플 예상 비용:
   - Input: 50 × 800 = 40,000 tokens → $0.10
   - Output: 50 × 200 = 10,000 tokens → $0.10
   - 총: ~$0.20

   전체 600 청크 예상:
   - Input: 600 × 800 = 480,000 tokens → $1.20
   - Output: 600 × 200 = 120,000 tokens → $1.20
   - 총: ~$2.40 (1회 실행)

   월간 예상 (주 2회 업데이트):
   - $2.40 × 8 = $19.20/월

3. 비용 임계값 및 대응

   | 예상 비용 | 판정 | 대응 |
   |-----------|------|------|
   | < $50/월  | GREEN | 전체 적용 진행 |
   | $50-100/월| YELLOW| 배치 최적화 후 진행 |
   | > $100/월 | RED   | 로컬 모델 전환 검토 |

4. 대안 전략 (비용 초과 시)

   Option A: 로컬 모델 전환
   - Llama 3.1 70B (ollama)
   - 비용: GPU 서버 비용만 (기존 인프라 활용 시 $0)
   - 품질: GPT-4o 대비 ~85% 예상

   Option B: 하이브리드 접근
   - 1차: 로컬 모델로 기본 추출
   - 2차: 복잡한 케이스만 GPT-4o 사용
   - 예상 비용 절감: 70%

   Option C: 배치 최적화
   - 변경된 섹션만 재처리
   - 캐싱 적극 활용
   - 예상 비용 절감: 50%

5. 검증 스크립트

   def verify_llm_cost(sample_size: int = 50) -> CostReport:
       # 샘플 선정
       sample_chunks = select_random_chunks(sample_size)

       # API 호출 (비용 추적)
       total_input_tokens = 0
       total_output_tokens = 0

       for chunk in sample_chunks:
           response = extract_entities(chunk)
           total_input_tokens += response.usage.input_tokens
           total_output_tokens += response.usage.output_tokens

       # 비용 계산
       sample_cost = calculate_cost(total_input_tokens, total_output_tokens)
       projected_cost = sample_cost * (TOTAL_CHUNKS / sample_size)
       monthly_cost = projected_cost * UPDATES_PER_MONTH

       return CostReport(
           sample_cost=sample_cost,
           projected_cost=projected_cost,
           monthly_cost=monthly_cost,
           recommendation=get_recommendation(monthly_cost)
       )
```

---

#### TODO-6: 커뮤니티 탐지 및 요약 설계
**Priority**: MEDIUM
**Estimated Effort**: 3일
**Dependencies**: TODO-5, TODO-5.5

**Description**:
Knowledge Graph에서 Leiden 알고리즘을 사용한 커뮤니티 탐지와 계층적 요약 생성 전략을 설계한다.

**Acceptance Criteria**:
- [ ] 커뮤니티 탐지 알고리즘 선택 및 파라미터 설정
- [ ] 커뮤니티 요약 생성 프롬프트 (Map-Reduce 전략 포함)
- [ ] 계층적 요약 인덱스 구조 설계

**Implementation Details**:

```
GraphRAG 커뮤니티 설계
======================

1. 커뮤니티 탐지
   - 알고리즘: Leiden (igraph 구현)
   - Resolution: 1.0 (기본값, 조정 가능)
   - 최소 커뮤니티 크기: 5 엔티티

2. 계층적 커뮤니티 구조
   Level 0: 전체 그래프 (Root)
   Level 1: 대분류 커뮤니티 (10-20개)
   Level 2: 중분류 커뮤니티 (50-100개)
   Level 3: 소분류 커뮤니티 (개별 토픽)

3. 커뮤니티 요약 생성
   - 각 커뮤니티의 엔티티/관계 수집
   - LLM으로 200-300단어 요약 생성
   - 상위 레벨은 하위 요약을 입력으로 사용

4. Map-Reduce 쿼리 처리
   Map: 관련 커뮤니티 요약에서 부분 답변 생성
   Reduce: 부분 답변들을 통합하여 최종 답변

커뮤니티 요약 테이블
-------------------
CREATE TABLE design_standard.community_summaries (
    id UUID PRIMARY KEY,
    community_id INTEGER NOT NULL,
    level INTEGER NOT NULL,
    entity_count INTEGER,
    summary TEXT NOT NULL,
    key_entities TEXT[],
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Map-Reduce 요약 전략 상세**:

```
Map-Reduce 요약 프롬프트 템플릿
==============================

1. MAP 단계 프롬프트 (커뮤니티별 부분 요약)

시스템:
"""
당신은 설계 표준 문서의 기술 내용을 요약하는 전문가입니다.
주어진 엔티티와 관계 정보를 바탕으로 핵심 내용을 요약하세요.
"""

사용자:
"""
다음은 '{community_name}' 커뮤니티의 엔티티와 관계입니다:

엔티티:
{entities_list}

관계:
{relationships_list}

질문: {user_query}

이 커뮤니티 관점에서 질문에 대한 부분 답변을 200단어 이내로 작성하세요.
관련 없으면 "해당 없음"이라고 답하세요.

출력 형식:
{
  "relevance_score": 0.0-1.0,
  "partial_answer": "...",
  "key_entities_used": ["...", "..."],
  "confidence": 0.0-1.0
}
"""

2. REDUCE 단계 프롬프트 (부분 답변 통합)

시스템:
"""
당신은 여러 출처의 정보를 통합하여 종합적인 답변을 생성하는 전문가입니다.
중복을 제거하고 일관된 답변을 작성하세요.
"""

사용자:
"""
다음은 여러 커뮤니티에서 수집한 부분 답변들입니다:

{partial_answers}

원본 질문: {user_query}

위 부분 답변들을 통합하여 종합적인 최종 답변을 작성하세요.
- 중복 정보는 한 번만 포함
- 상충되는 정보는 신뢰도 높은 것 우선
- 출처 커뮤니티 명시

출력 형식:
{
  "final_answer": "...",
  "sources": ["community_1", "community_2"],
  "confidence": 0.0-1.0,
  "limitations": "..."
}
"""

3. 커뮤니티 요약 생성 프롬프트 (배치 처리용)

시스템:
"""
설계 표준 도메인의 Knowledge Graph 커뮤니티를 요약합니다.
"""

사용자:
"""
커뮤니티 ID: {community_id}
레벨: {level}
엔티티 수: {entity_count}

주요 엔티티:
{top_entities}

주요 관계:
{top_relationships}

이 커뮤니티의 핵심 주제와 내용을 200-300단어로 요약하세요.
포함할 내용:
1. 커뮤니티의 주요 주제
2. 핵심 엔티티와 그 역할
3. 엔티티 간 주요 관계
4. 설계 표준에서의 의미

출력:
{
  "title": "커뮤니티 제목",
  "summary": "...",
  "key_topics": ["...", "..."],
  "key_entities": ["...", "..."]
}
"""
```

---

### Phase 4: Multimodal Processing (Week 7-8)

#### TODO-7: 표/다이어그램 처리 모듈 설계
**Priority**: MEDIUM
**Estimated Effort**: 4일
**Dependencies**: TODO-2

**Description**:
PDF/문서 내 표와 다이어그램을 추출하고 텍스트화하는 모듈을 설계한다.

**Acceptance Criteria**:
- [ ] 표 추출 도구 선정 및 비교 평가
- [ ] 다이어그램 텍스트화 전략 (Vision LLM 활용)
- [ ] 추출 결과 품질 검증 방안

**Implementation Details**:

```
멀티모달 처리 파이프라인
========================

1. 표 추출 및 처리

   도구 선정:
   - PDF 표: camelot-py (정확도 우선) 또는 tabula-py (속도 우선)
   - 스캔 문서: Azure Document Intelligence
   - 복잡한 표: GPT-4o vision

   처리 흐름:
   PDF → 표 영역 감지 → 표 추출 → Markdown 변환 → 청크 생성

   표 품질 검증:
   - 열/행 수 일관성 검사
   - 셀 병합 처리 확인
   - 한글 OCR 정확도 검증

2. 다이어그램 처리

   처리 흐름:
   이미지 추출 → 유형 분류 → 텍스트화 → 청크 생성

   유형별 처리:
   - 흐름도: GPT-4o로 프로세스 설명 생성
   - 구조도: 구성 요소 및 관계 설명
   - 수식 이미지: LaTeX 변환 (Mathpix API)

   프롬프트 예시 (다이어그램 → 텍스트):
   """
   이 다이어그램을 분석하여 다음을 설명하세요:
   1. 다이어그램의 유형과 목적
   2. 주요 구성 요소
   3. 구성 요소 간의 관계/흐름
   4. 핵심 정보 요약

   기술 문서 맥락: {section_title}
   """

3. 이미지-텍스트 정합

   - 이미지 캡션과 본문 참조 연결
   - "그림 3.1 참조"와 실제 이미지 매칭
   - 캡션을 이미지 청크의 메타데이터로 저장
```

**표 처리 코드 구조**:

```python
class TableProcessor:
    def __init__(self, strategy: str = 'camelot'):
        self.strategy = strategy
        self.vision_model = None  # 필요시 초기화

    def extract_tables(self, pdf_path: str) -> List[Table]:
        if self.strategy == 'camelot':
            return self._extract_with_camelot(pdf_path)
        elif self.strategy == 'vision':
            return self._extract_with_vision(pdf_path)

    def table_to_chunk(self, table: Table, context: dict) -> Chunk:
        return Chunk(
            content=table.to_markdown(),
            chunk_type='table',
            metadata={
                'page': table.page,
                'caption': self._find_caption(table, context),
                'rows': table.row_count,
                'cols': table.col_count
            }
        )
```

---

#### TODO-8: 이미지-텍스트 정합 전략 수립
**Priority**: LOW
**Estimated Effort**: 2일
**Dependencies**: TODO-7

**Description**:
이미지 캡션과 본문 참조를 연결하고, 이미지 콘텐츠를 텍스트로 변환하는 전략을 수립한다.

**Acceptance Criteria**:
- [ ] 캡션-이미지 매칭 알고리즘
- [ ] 본문 내 이미지 참조 패턴 정의
- [ ] 이미지 설명 생성 품질 기준

---

### Phase 5: Integration & Evaluation (Week 9-10)

#### TODO-9: 하이브리드 검색 통합 설계
**Priority**: HIGH
**Estimated Effort**: 4일
**Dependencies**: TODO-4, TODO-6

**Description**:
벡터 검색 + 전문 검색 + 그래프 검색을 통합한 하이브리드 검색 시스템을 설계한다.

**Acceptance Criteria**:
- [ ] 3가지 검색 방식 통합 아키텍처
- [ ] 검색 결과 융합(Fusion) 알고리즘
- [ ] 쿼리 유형별 라우팅 전략

**Implementation Details**:

```
하이브리드 검색 아키텍처
========================

┌─────────────────────────────────────────────────────────────┐
│                      QUERY INPUT                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  QUERY ANALYZER                              │
│  - 쿼리 유형 분류 (사실형/분석형/탐색형)                      │
│  - 키워드 추출                                               │
│  - 쿼리 임베딩 생성                                          │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  VECTOR SEARCH  │ │ KEYWORD SEARCH  │ │  GRAPH SEARCH   │
│                 │ │                 │ │                 │
│  pgvector       │ │  PostgreSQL     │ │  Community      │
│  cosine sim     │ │  ts_rank        │ │  Summaries      │
│                 │ │                 │ │                 │
│  top_k: 20      │ │  top_k: 20      │ │  top_k: 5       │
└─────────────────┘ └─────────────────┘ └─────────────────┘
            │               │               │
            └───────────────┼───────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  RESULT FUSION                               │
│                                                             │
│  Reciprocal Rank Fusion (RRF):                              │
│  score(d) = Σ 1/(k + rank_i(d))                             │
│                                                             │
│  가중치 (쿼리 유형별):                                       │
│  - 사실형: vector=0.5, keyword=0.4, graph=0.1               │
│  - 분석형: vector=0.3, keyword=0.2, graph=0.5               │
│  - 탐색형: vector=0.4, keyword=0.3, graph=0.3               │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  POST-PROCESSING                             │
│  - 중복 제거 (동일 섹션)                                     │
│  - 계층 컨텍스트 확장 (부모/자식 청크 포함)                   │
│  - 참조 청크 포함 (표/이미지)                                │
│  - 최종 top_k 선택                                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    SEARCH RESULTS                            │
│  - chunks: List[Chunk]                                      │
│  - graph_context: List[CommunitySummary]                    │
│  - metadata: {search_type, scores, latency}                 │
└─────────────────────────────────────────────────────────────┘
```

**쿼리 유형 분류**:

| 쿼리 유형 | 예시 | 최적 검색 |
|-----------|------|-----------|
| 사실형 (Factual) | "응집지 체류시간 기준은?" | Vector + Keyword |
| 분석형 (Analytical) | "정수처리 공정의 전체 흐름은?" | Graph + Vector |
| 탐색형 (Exploratory) | "응집 관련 설계 기준 알려줘" | Hybrid (균등) |

---

#### TODO-10: 평가 프레임워크 구축
**Priority**: HIGH
**Estimated Effort**: 3일
**Dependencies**: TODO-9
**담당자**: TBD (Week 9 시작 전 지정)

**Description**:
청킹 품질 및 검색 성능을 측정하는 평가 프레임워크를 설계한다.

**Acceptance Criteria**:
- [ ] 청킹 품질 평가 지표 정의
- [ ] 검색 성능 평가 지표 정의
- [ ] 테스트 데이터셋 구성 방안
- [ ] 자동화된 평가 파이프라인 설계

**Implementation Details**:

```
평가 프레임워크
==============

1. 청킹 품질 지표

   a) 구조 보존율 (Structure Preservation)
      - 정의: 원본 구조(섹션, 표)가 청크에서 유지된 비율
      - 측정: (보존된 구조 요소 수) / (전체 구조 요소 수)
      - 목표: > 95%

   b) 의미 완결성 (Semantic Completeness)
      - 정의: 청크가 독립적으로 의미를 전달하는 정도
      - 측정: LLM 기반 자동 평가 (1-5점)
      - 목표: 평균 > 4.0

   c) 참조 무결성 (Reference Integrity)
      - 정의: 청크 간 참조가 올바르게 연결된 비율
      - 측정: (유효한 참조 수) / (전체 참조 수)
      - 목표: 100%

2. 검색 성능 지표

   a) Recall@K
      - 정의: 상위 K개 결과 중 관련 문서 비율
      - K = [5, 10, 20]
      - 목표: Recall@10 > 0.85

   b) MRR (Mean Reciprocal Rank)
      - 정의: 첫 번째 관련 결과의 역순위 평균
      - 목표: > 0.7

   c) Comprehensiveness (GraphRAG)
      - 정의: 응답이 질문의 모든 측면을 다루는 정도
      - 측정: LLM 쌍대 비교 (win rate)
      - 목표: 기존 RAG 대비 > 70% win rate

   d) Diversity (GraphRAG)
      - 정의: 응답에 포함된 관점/정보의 다양성
      - 측정: LLM 쌍대 비교 (win rate)
      - 목표: 기존 RAG 대비 > 75% win rate

3. 테스트 데이터셋

   a) 골든 QA 세트
      - 설계 표준 도메인 전문가가 작성
      - 50개 질문-답변 쌍
      - 난이도: Easy(20), Medium(20), Hard(10)
      - ★ 일정: Week 7-8 (Phase 4와 병행)
      - ★ 담당자: 도메인 전문가 + 데이터팀

   b) 관련성 레이블
      - 각 질문에 대해 관련 청크 레이블링
      - 관련도: 0(무관), 1(부분 관련), 2(직접 관련)

4. 평가 파이프라인

   def evaluate_pipeline(config: EvalConfig) -> EvalResults:
       # 1. 테스트 데이터 로드
       test_data = load_golden_qa_set()

       # 2. 청킹 수행
       chunks = run_chunking_pipeline(config.chunking_config)

       # 3. 검색 수행
       for query, expected in test_data:
           results = hybrid_search(query, config.search_config)

           # 4. 지표 계산
           recall = calculate_recall(results, expected)
           mrr = calculate_mrr(results, expected)

       # 5. 종합 리포트 생성
       return EvalResults(
           chunking_metrics=chunking_eval,
           search_metrics=search_eval,
           comparison=baseline_comparison
       )
```

---

## Commit Strategy

| Phase | Commit Message | Files |
|-------|----------------|-------|
| Phase 1 | `feat: add document classification and pipeline architecture` | chunking/classifier.py, chunking/pipeline.py |
| Phase 1 | `feat: add migration scripts for design_sections` | migration/migrate.py, migration/mapping.py |
| Phase 2 | `feat: implement semantic and structural chunking modules` | chunking/semantic.py, chunking/structural.py |
| Phase 3 | `feat: add GraphRAG entity extraction and community detection` | graphrag/extractor.py, graphrag/community.py |
| Phase 4 | `feat: implement multimodal table and diagram processing` | multimodal/table.py, multimodal/diagram.py |
| Phase 5 | `feat: integrate hybrid search and evaluation framework` | search/hybrid.py, evaluation/framework.py |

---

## Success Criteria

### Quantitative Metrics
- [ ] 청킹 구조 보존율 > 95%
- [ ] 검색 Recall@10 > 0.85
- [ ] 검색 MRR > 0.7
- [ ] GraphRAG Comprehensiveness win rate > 70%
- [ ] 표/이미지 추출 정확도 > 90%
- [ ] **LLM API 비용 < $100/월**

### Qualitative Criteria
- [ ] 설계 표준 도메인 전문가 검토 통과
- [ ] 기존 전문 검색 대비 체감 품질 향상
- [ ] 문서 구조 파괴 없이 검색 가능

---

## Implementation Roadmap

```
Week 1-2: Foundation
├── TODO-1: 문서 분류 체계 수립
├── TODO-2: 파이프라인 아키텍처 설계
├── TODO-2.5: 마이그레이션 설계 (NEW)
└── ★ CHECKPOINT 1

Week 3-4: Core Chunking
├── TODO-3: 의미론적 청킹 모듈 (GraphRAG 기준 적용)
├── TODO-4: 구조 보존 청킹 모듈
└── ★ CHECKPOINT 2

Week 5-6: GraphRAG
├── TODO-5: 엔티티/관계 추출
├── TODO-5.5: LLM 비용 검증 (50개 샘플) (NEW)
├── TODO-6: 커뮤니티 탐지 및 요약
└── ★ CHECKPOINT 3

Week 7-8: Multimodal + 평가 데이터 구축
├── TODO-7: 표/다이어그램 처리
├── TODO-8: 이미지-텍스트 정합
├── [병행] 골든 QA 세트 구축 (50개)
└── ★ CHECKPOINT 4

Week 9-10: Integration
├── TODO-9: 하이브리드 검색 통합
├── TODO-10: 평가 프레임워크
└── ★ CHECKPOINT 5 (FINAL)

Week 11-12: Testing & Refinement
├── 성능 튜닝
├── 버그 수정
└── 문서화
```

---

## Technology Stack

### Core
| Component | Technology | Rationale | 사전 검증 항목 |
|-----------|------------|-----------|----------------|
| Database | PostgreSQL + pgvector | 기존 인프라 활용, 벡터 검색 지원 | **PostgreSQL 버전 15+ 확인 필수** |
| Embedding | OpenAI text-embedding-3-small | 성능/비용 균형 | - |
| LLM | GPT-4o / Claude 3.5 Sonnet | 엔티티 추출, 요약 생성 | **비용 임계값 $100/월** |
| Graph | NetworkX + igraph | 커뮤니티 탐지, 경량 그래프 처리 | - |

### Python Libraries
| Library | Purpose | 검증 상태 |
|---------|---------|-----------|
| kss | 한국어 문장 분리 | **설계 표준 문서 적합성 테스트 필요** |
| kiwipiepy | 한국어 문장 분리 (대안 1) | 비교 평가 대상 |
| koalanlp | 한국어 문장 분리 (대안 2) | 비교 평가 대상 |
| camelot-py | PDF 표 추출 | - |
| sentence-transformers | 로컬 임베딩 (대안) | - |
| langchain | RAG 파이프라인 통합 | - |
| psycopg2 | PostgreSQL 연결 | - |

### Optional (확장) - 도입 기준 정량화
| Component | Technology | 도입 조건 |
|-----------|------------|-----------|
| Graph DB | Neo4j | 엔티티 > 10,000개 또는 관계 탐색 latency > 100ms |
| Search | Elasticsearch | 전문 검색 QPS > 100 또는 고급 분석 쿼리 필요 |
| Vision | Azure Document Intelligence | 스캔 문서 비율 > 30% 또는 표 추출 정확도 < 85% |

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM API 비용 초과 | HIGH | **50개 샘플 사전 검증 (TODO-5.5), 월 $100 임계값, 로컬 모델 대안** |
| 한글 처리 품질 저하 | MEDIUM | **kss/kiwipiepy/koalanlp 비교 테스트 (20개 샘플)** |
| 표 추출 실패 | MEDIUM | 다중 도구 폴백 (camelot → vision) |
| GraphRAG 복잡성 | HIGH | 단계적 도입, 최소 기능 먼저 |
| 기존 데이터 호환성 | MEDIUM | **마이그레이션 스크립트 (TODO-2.5), 체크포인트 롤백** |
| pgvector 호환성 | MEDIUM | **PostgreSQL 15+ 사전 검증** |

---

## Notes

- 이 계획은 현재 프로젝트의 238개 설계 표준 섹션을 기반으로 작성됨
- pgvector 확장은 PostgreSQL 15+ 권장 → **사전 검증 필수**
- GraphRAG는 선택적 기능으로, Phase 3-4는 순서 조정 가능
- 평가 프레임워크는 지속적 개선을 위해 필수
- **GraphRAG 논문 기준 (600 토큰, 100 오버랩)이 기본값으로 적용됨**
- **LLM 비용은 월 $100 이하로 관리 (초과 시 로컬 모델 전환)**

---

**Plan Created**: 2026-02-04
**Plan Revised**: 2026-02-04 (Critic 피드백 반영)
**Estimated Duration**: 10-12 weeks
**Primary Author**: Prometheus (Planning Consultant)

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-04 | v1.0 | 초기 계획 수립 |
| 2026-02-04 | v2.0 | Critic 피드백 반영 - 5 Critical Issues 해결 |

### v2.0 변경 사항

1. **Critical Issue 1**: GraphRAG 논문 기준 (600 토큰, 100 오버랩)을 기본값으로 명시
2. **Critical Issue 2**: LLM 비용 관리 - TODO-5.5 추가 (50개 샘플 검증), 월 $100 임계값
3. **Critical Issue 3**: kss 적합성 테스트 + 대안 분리기 비교 평가 추가
4. **Critical Issue 4**: TODO-2.5 추가 - 마이그레이션 설계 및 매핑 테이블
5. **Critical Issue 5**: 롤백 전략 섹션 추가 - 5개 체크포인트 정의

### Minor Issues 반영

- Map-Reduce 요약 프롬프트 템플릿 상세화
- 평가 데이터셋 구축 일정 (Week 7-8) 및 담당자 명시
- pgvector 버전 호환성 검증 항목 추가
- Optional 기술 스택 도입 기준 정량화
