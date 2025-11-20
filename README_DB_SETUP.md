# PostgreSQL 데이터베이스 설정 가이드

## 📋 목차
1. [사전 준비](#사전-준비)
2. [데이터 삽입](#데이터-삽입)
3. [DBeaver 연결](#dbeaver-연결)
4. [데이터 조회](#데이터-조회)
5. [유용한 쿼리](#유용한-쿼리)

---

## 🔧 사전 준비

### 1. Python 패키지 설치
```bash
pip install psycopg2-binary
```

### 2. 데이터베이스 정보 확인
- **Host**: 10.0.0.20
- **Port**: 2332
- **Database**: dde-water
- **Username**: postgres
- **Password**: postgres
- **Schema**: design_standard

---

## 📥 데이터 삽입

### 자동 실행 (권장)
```bash
cd d:\DATA\RAG_AGENT
python insert_to_postgres.py
```

이 스크립트는 자동으로:
1. ✅ 데이터베이스 연결
2. ✅ 테이블 생성 (design_standard.design_sections)
3. ✅ JSON 데이터 로드
4. ✅ 계층 구조 데이터 삽입
5. ✅ 데이터 검증

### 수동 실행
1. DBeaver에서 데이터베이스 연결
2. `sql/01_create_tables.sql` 실행
3. `insert_to_postgres.py` 실행

---

## 🔌 DBeaver 연결

### 1. 새 연결 만들기
1. DBeaver 실행
2. `Database` > `New Database Connection` 클릭
3. `PostgreSQL` 선택

### 2. 연결 정보 입력
```
Host: 10.0.0.20
Port: 2332
Database: dde-water
Username: postgres
Password: postgres
```

### 3. 연결 테스트
- `Test Connection` 버튼 클릭
- 성공 메시지 확인

### 4. 스키마 탐색
```
dde-water
  └── Schemas
      └── design_standard
          ├── Tables
          │   └── design_sections  (메인 테이블)
          └── Views
              └── v_section_tree   (계층 구조 뷰)
```

---

## 📊 데이터 조회

### 1. 전체 섹션 조회
```sql
SELECT *
FROM design_standard.design_sections
ORDER BY code;
```

### 2. 최상위 섹션만 조회
```sql
SELECT code, title, content
FROM design_standard.design_sections
WHERE parent_code IS NULL
ORDER BY code;
```

### 3. 특정 섹션과 하위 섹션 조회 (예: 섹션 1)
```sql
WITH RECURSIVE section_tree AS (
    -- 시작 섹션
    SELECT
        code,
        title,
        content,
        level,
        code as path
    FROM design_standard.design_sections
    WHERE code = '1'

    UNION ALL

    -- 하위 섹션 재귀 조회
    SELECT
        s.code,
        s.title,
        s.content,
        s.level,
        st.path || ' > ' || s.code as path
    FROM design_standard.design_sections s
    INNER JOIN section_tree st ON s.parent_code = st.code
)
SELECT * FROM section_tree
ORDER BY path;
```

### 4. 계층 구조 뷰 사용
```sql
-- 전체 트리 구조 확인
SELECT * FROM design_standard.v_section_tree;

-- 특정 코드 패턴 검색
SELECT * FROM design_standard.v_section_tree
WHERE code LIKE '3.%';
```

---

## 🔍 유용한 쿼리

### 1. 키워드 검색 (제목 + 내용)
```sql
-- '응집' 키워드로 검색
SELECT * FROM design_standard.search_sections('응집');

-- '여과' 키워드로 검색
SELECT * FROM design_standard.search_sections('여과');

-- '정수처리' 키워드로 검색
SELECT * FROM design_standard.search_sections('정수처리');
```

### 2. 레벨별 통계
```sql
SELECT
    level,
    COUNT(*) as section_count
FROM design_standard.design_sections
GROUP BY level
ORDER BY level;
```

### 3. 섹션 내용 길이 통계
```sql
SELECT
    code,
    title,
    LENGTH(content) as content_length,
    level
FROM design_standard.design_sections
WHERE content IS NOT NULL
ORDER BY content_length DESC
LIMIT 10;
```

### 4. 특정 섹션의 자식 개수
```sql
SELECT
    parent.code,
    parent.title,
    COUNT(child.id) as children_count
FROM design_standard.design_sections parent
LEFT JOIN design_standard.design_sections child
    ON child.parent_code = parent.code
GROUP BY parent.code, parent.title
HAVING COUNT(child.id) > 0
ORDER BY children_count DESC;
```

### 5. 전문 검색 (Full Text Search)
```sql
-- 제목에서 검색
SELECT code, title, level
FROM design_standard.design_sections
WHERE to_tsvector('korean', title) @@ plainto_tsquery('korean', '응집제');

-- 내용에서 검색
SELECT code, title, LEFT(content, 100) as preview
FROM design_standard.design_sections
WHERE to_tsvector('korean', content) @@ plainto_tsquery('korean', '정수처리');
```

### 6. 부모-자식 관계 확인
```sql
SELECT
    parent.code as parent_code,
    parent.title as parent_title,
    child.code as child_code,
    child.title as child_title
FROM design_standard.design_sections parent
INNER JOIN design_standard.design_sections child
    ON child.parent_code = parent.code
WHERE parent.code = '3'
ORDER BY child.code;
```

---

## 📈 테이블 구조

```sql
-- 테이블 정보 확인
\d design_standard.design_sections
```

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | SERIAL | 자동 증가 ID |
| code | VARCHAR(50) | 섹션 코드 (예: "1.1.1") |
| title | TEXT | 섹션 제목 |
| content | TEXT | 섹션 본문 |
| parent_code | VARCHAR(50) | 부모 섹션 코드 |
| level | INTEGER | 계층 레벨 (1, 2, 3, ...) |
| sort_order | INTEGER | 정렬 순서 |
| created_at | TIMESTAMP | 생성 시간 |
| updated_at | TIMESTAMP | 수정 시간 |

---

## 🎯 RAG 시스템 활용 예시

### 벡터 검색 준비 (pgvector 확장 사용)
```sql
-- pgvector 확장 설치 (필요한 경우)
CREATE EXTENSION IF NOT EXISTS vector;

-- 임베딩 컬럼 추가
ALTER TABLE design_standard.design_sections
ADD COLUMN embedding vector(1536);

-- 벡터 인덱스 생성
CREATE INDEX ON design_standard.design_sections
USING ivfflat (embedding vector_cosine_ops);
```

### 유사도 검색 쿼리 예시
```sql
-- 특정 임베딩과 유사한 섹션 찾기
SELECT
    code,
    title,
    1 - (embedding <=> '[임베딩 벡터]'::vector) as similarity
FROM design_standard.design_sections
WHERE embedding IS NOT NULL
ORDER BY embedding <=> '[임베딩 벡터]'::vector
LIMIT 5;
```

---

## 🛠️ 트러블슈팅

### 연결 실패
```
Error: Connection refused
```
**해결 방법:**
1. PostgreSQL 서버가 실행 중인지 확인
2. 방화벽 설정 확인
3. `pg_hba.conf` 파일에서 원격 접속 허용 확인

### 한글 검색 안됨
```sql
-- 한글 텍스트 검색 설정 확인
SHOW default_text_search_config;

-- 'korean' 설정이 없으면 'simple' 사용
CREATE INDEX idx_sections_content_simple
ON design_standard.design_sections
USING gin(to_tsvector('simple', content));
```

### 권한 오류
```sql
-- 스키마 권한 부여
GRANT ALL ON SCHEMA design_standard TO postgres;
GRANT ALL ON ALL TABLES IN SCHEMA design_standard TO postgres;
```

---

## 📝 추가 참고사항

- 데이터 업데이트 시: `insert_to_postgres.py` 재실행
- 백업: DBeaver에서 `Tools` > `Backup Database`
- 성능 최적화: 인덱스 재구성 `REINDEX TABLE design_standard.design_sections;`
