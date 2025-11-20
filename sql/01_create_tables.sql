-- ============================================================================
-- PostgreSQL 테이블 생성 스크립트
-- 설계 표준 문서 계층 구조 저장
-- ============================================================================

-- 스키마 생성 (이미 있으면 skip)
CREATE SCHEMA IF NOT EXISTS design_standard;

-- 기존 테이블 삭제 (재생성할 경우)
DROP TABLE IF EXISTS design_standard.design_sections CASCADE;

-- 설계 표준 섹션 테이블 생성
CREATE TABLE design_standard.design_sections (
    -- 기본 키
    id SERIAL PRIMARY KEY,

    -- 섹션 정보
    code VARCHAR(50) NOT NULL UNIQUE,           -- 섹션 코드 (예: "1", "1.1", "1.1.1")
    title TEXT NOT NULL,                         -- 섹션 제목
    content TEXT,                                -- 섹션 본문 내용

    -- 계층 구조
    parent_code VARCHAR(50),                     -- 부모 섹션 코드
    level INTEGER NOT NULL,                      -- 계층 레벨 (1, 2, 3, ...)

    -- 순서 정보
    sort_order INTEGER,                          -- 같은 부모 내에서의 정렬 순서

    -- 메타 데이터
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- 외래 키 제약
    CONSTRAINT fk_parent
        FOREIGN KEY (parent_code)
        REFERENCES design_standard.design_sections(code)
        ON DELETE CASCADE
);

-- 인덱스 생성
CREATE INDEX idx_sections_code ON design_standard.design_sections(code);
CREATE INDEX idx_sections_parent_code ON design_standard.design_sections(parent_code);
CREATE INDEX idx_sections_level ON design_standard.design_sections(level);
CREATE INDEX idx_sections_sort_order ON design_standard.design_sections(sort_order);

-- 전문 검색을 위한 GIN 인덱스
-- 'korean' 설정이 없으면 'simple' 사용
CREATE INDEX idx_sections_content_gin ON design_standard.design_sections
    USING gin(to_tsvector('simple', coalesce(content, '')));
CREATE INDEX idx_sections_title_gin ON design_standard.design_sections
    USING gin(to_tsvector('simple', title));

-- 코멘트 추가
COMMENT ON TABLE design_standard.design_sections IS '설계 표준 문서 계층 구조';
COMMENT ON COLUMN design_standard.design_sections.code IS '섹션 코드 (예: 1.1.1)';
COMMENT ON COLUMN design_standard.design_sections.title IS '섹션 제목';
COMMENT ON COLUMN design_standard.design_sections.content IS '섹션 본문 내용';
COMMENT ON COLUMN design_standard.design_sections.parent_code IS '부모 섹션 코드';
COMMENT ON COLUMN design_standard.design_sections.level IS '계층 레벨 (1=최상위)';
COMMENT ON COLUMN design_standard.design_sections.sort_order IS '정렬 순서';

-- ============================================================================
-- 유용한 뷰 생성
-- ============================================================================

-- 계층 구조 전체 트리 뷰
CREATE OR REPLACE VIEW design_standard.v_section_tree AS
WITH RECURSIVE section_tree AS (
    -- 최상위 레벨 (부모가 없는 섹션)
    SELECT
        id,
        code,
        title,
        content,
        parent_code,
        level,
        sort_order,
        code::TEXT AS path,
        title::TEXT AS full_title
    FROM design_standard.design_sections
    WHERE parent_code IS NULL

    UNION ALL

    -- 하위 레벨 재귀 조회
    SELECT
        s.id,
        s.code,
        s.title,
        s.content,
        s.parent_code,
        s.level,
        s.sort_order,
        (st.path || ' > ' || s.code)::TEXT AS path,
        (st.full_title || ' > ' || s.title)::TEXT AS full_title
    FROM design_standard.design_sections s
    INNER JOIN section_tree st ON s.parent_code = st.code
)
SELECT * FROM section_tree
ORDER BY path;

COMMENT ON VIEW design_standard.v_section_tree IS '섹션 계층 구조 트리 뷰';

-- ============================================================================
-- 검색 함수
-- ============================================================================

-- 키워드로 섹션 검색 (제목 + 내용)
CREATE OR REPLACE FUNCTION design_standard.search_sections(
    search_query TEXT
)
RETURNS TABLE (
    id INTEGER,
    code VARCHAR(50),
    title TEXT,
    content_preview TEXT,
    level INTEGER,
    relevance REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.code,
        s.title,
        LEFT(s.content, 200) AS content_preview,
        s.level,
        ts_rank(
            to_tsvector('simple', s.title || ' ' || COALESCE(s.content, '')),
            plainto_tsquery('simple', search_query)
        ) AS relevance
    FROM design_standard.design_sections s
    WHERE
        to_tsvector('simple', s.title || ' ' || COALESCE(s.content, ''))
        @@ plainto_tsquery('simple', search_query)
    ORDER BY relevance DESC, s.code;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION design_standard.search_sections(TEXT) IS '키워드로 섹션 검색';

-- ============================================================================
-- 완료 메시지
-- ============================================================================

DO $$
BEGIN
    RAISE NOTICE '========================================';
    RAISE NOTICE '테이블 생성 완료!';
    RAISE NOTICE 'Schema: design_standard';
    RAISE NOTICE 'Table: design_sections';
    RAISE NOTICE '========================================';
END $$;
