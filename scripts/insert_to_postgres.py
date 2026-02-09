"""
JSON 데이터를 PostgreSQL에 삽입하는 스크립트
재구성된 design_standards_db_restructured.json을 DB에 저장
"""

import json
import sys
from typing import Dict, List, Any

# psycopg2가 없으면 설치 안내
try:
    import psycopg2
    from psycopg2 import sql
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
except ImportError:
    print("=" * 80)
    print("ERROR: psycopg2 패키지가 설치되지 않았습니다.")
    print("다음 명령어로 설치하세요:")
    print("  pip install psycopg2-binary")
    print("=" * 80)
    sys.exit(1)

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ============================================================================
# 데이터베이스 연결 설정
# ============================================================================

DB_CONFIG = {
    'host': '10.0.0.20',
    'port': 2332,
    'database': 'dde-water',
    'user': 'postgres',
    'password': 'postgres'
}

JSON_FILE = r'd:\DATA\RAG_AGENT\design_standards_db_restructured.json'

# ============================================================================
# 함수 정의
# ============================================================================

def connect_db():
    """PostgreSQL 데이터베이스에 연결합니다."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print(f"[OK] 데이터베이스 연결 성공: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")
        return conn
    except Exception as e:
        print(f"[ERROR] 데이터베이스 연결 실패: {e}")
        sys.exit(1)


def execute_sql_file(conn, sql_file: str):
    """SQL 파일을 실행합니다."""
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()

        cursor = conn.cursor()
        cursor.execute(sql_content)
        conn.commit()
        cursor.close()

        print(f"[OK] SQL 파일 실행 완료: {sql_file}")
        return True
    except Exception as e:
        print(f"[ERROR] SQL 파일 실행 실패: {e}")
        conn.rollback()
        return False


def get_level_from_code(code: str) -> int:
    """코드에서 레벨을 계산합니다. (예: "1.1.1" -> 3)"""
    return code.count('.') + 1


def get_parent_code(code: str) -> str:
    """부모 코드를 반환합니다. (예: "1.1.1" -> "1.1")"""
    parts = code.rsplit('.', 1)
    return parts[0] if len(parts) > 1 else None


def flatten_sections(sections: List[Dict[str, Any]], parent_code: str = None) -> List[Dict[str, Any]]:
    """
    계층 구조 JSON을 평면 리스트로 변환합니다.
    """
    result = []

    for idx, section in enumerate(sections):
        code = section['code']
        title = section['title']
        content = section.get('content', '')
        children = section.get('children', [])

        # 현재 섹션 추가
        result.append({
            'code': code,
            'title': title,
            'content': content,
            'parent_code': parent_code,
            'level': get_level_from_code(code),
            'sort_order': idx + 1
        })

        # 하위 섹션 재귀 처리
        if children:
            result.extend(flatten_sections(children, parent_code=code))

    return result


def insert_sections(conn, sections: List[Dict[str, Any]]):
    """섹션 데이터를 데이터베이스에 삽입합니다."""
    cursor = conn.cursor()

    # 기존 데이터 삭제
    print("\n[작업] 기존 데이터 삭제 중...")
    cursor.execute("DELETE FROM design_standard.design_sections")
    conn.commit()
    print(f"  -> 삭제 완료")

    # 데이터 삽입
    print(f"\n[작업] {len(sections)}개 섹션 삽입 중...")

    insert_query = """
    INSERT INTO design_standard.design_sections
        (code, title, content, parent_code, level, sort_order)
    VALUES
        (%s, %s, %s, %s, %s, %s)
    """

    success_count = 0
    error_count = 0

    for section in sections:
        try:
            cursor.execute(insert_query, (
                section['code'],
                section['title'],
                section['content'],
                section['parent_code'],
                section['level'],
                section['sort_order']
            ))
            success_count += 1

            if success_count % 10 == 0:
                print(f"  -> {success_count}/{len(sections)} 삽입됨...", end='\r')

        except Exception as e:
            error_count += 1
            print(f"\n[ERROR] 섹션 '{section['code']}' 삽입 실패: {e}")

    conn.commit()
    cursor.close()

    print(f"\n[완료] 삽입 성공: {success_count}개, 실패: {error_count}개")
    return success_count, error_count


def verify_data(conn):
    """삽입된 데이터를 검증합니다."""
    cursor = conn.cursor()

    print("\n" + "=" * 80)
    print("데이터 검증")
    print("=" * 80)

    # 전체 섹션 수
    cursor.execute("SELECT COUNT(*) FROM design_standard.design_sections")
    total_count = cursor.fetchone()[0]
    print(f"\n총 섹션 수: {total_count}")

    # 레벨별 섹션 수
    cursor.execute("""
        SELECT level, COUNT(*) as count
        FROM design_standard.design_sections
        GROUP BY level
        ORDER BY level
    """)

    print("\n레벨별 섹션 수:")
    for row in cursor.fetchall():
        level, count = row
        print(f"  Level {level}: {count}개")

    # 최상위 섹션 목록
    cursor.execute("""
        SELECT code, title
        FROM design_standard.design_sections
        WHERE parent_code IS NULL
        ORDER BY code
    """)

    print("\n최상위 섹션 목록:")
    for row in cursor.fetchall():
        code, title = row
        print(f"  [{code}] {title}")

    # 샘플 계층 구조 확인 (코드 1번 섹션)
    cursor.execute("""
        WITH RECURSIVE section_tree AS (
            SELECT
                code,
                title,
                level,
                code::TEXT as path
            FROM design_standard.design_sections
            WHERE code = '1'

            UNION ALL

            SELECT
                s.code,
                s.title,
                s.level,
                (st.path || ' > ' || s.code)::TEXT as path
            FROM design_standard.design_sections s
            INNER JOIN section_tree st ON s.parent_code = st.code
        )
        SELECT code, title, level, path
        FROM section_tree
        ORDER BY path
        LIMIT 10
    """)

    print("\n계층 구조 샘플 (섹션 1 하위, 최대 10개):")
    for row in cursor.fetchall():
        code, title, level, path = row
        indent = "  " * (level - 1)
        print(f"  {indent}[{code}] {title}")

    cursor.close()


# ============================================================================
# 메인 실행
# ============================================================================

def main():
    print("=" * 80)
    print("PostgreSQL 데이터 삽입 스크립트")
    print("=" * 80)

    # 1. 데이터베이스 연결
    print(f"\n[1단계] 데이터베이스 연결")
    conn = connect_db()

    # 2. 테이블 생성 (SQL 파일 실행)
    print(f"\n[2단계] 테이블 생성")
    sql_file = r'd:\DATA\RAG_AGENT\sql\01_create_tables.sql'
    if not execute_sql_file(conn, sql_file):
        print("[ERROR] 테이블 생성 실패. 종료합니다.")
        conn.close()
        return

    # 3. JSON 파일 로드
    print(f"\n[3단계] JSON 파일 로드: {JSON_FILE}")
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"  -> {len(data)}개의 최상위 섹션 로드됨")
    except Exception as e:
        print(f"[ERROR] JSON 파일 로드 실패: {e}")
        conn.close()
        return

    # 4. 계층 구조를 평면 리스트로 변환
    print(f"\n[4단계] 데이터 변환 (계층 구조 -> 평면 리스트)")
    sections = flatten_sections(data)
    print(f"  -> 총 {len(sections)}개 섹션으로 변환됨")

    # 5. 데이터베이스에 삽입
    print(f"\n[5단계] 데이터베이스에 삽입")
    success, error = insert_sections(conn, sections)

    # 6. 데이터 검증
    print(f"\n[6단계] 데이터 검증")
    verify_data(conn)

    # 7. 연결 종료
    conn.close()
    print("\n" + "=" * 80)
    print("[완료] 모든 작업이 완료되었습니다!")
    print("=" * 80)

    print("\n[다음 단계]")
    print("  1. DBeaver에서 데이터베이스에 연결")
    print("  2. design_standard 스키마 확인")
    print("  3. design_sections 테이블 조회")
    print("  4. v_section_tree 뷰로 계층 구조 확인")
    print("\n[검색 예시]")
    print("  SELECT * FROM design_standard.search_sections('응집');")
    print("  SELECT * FROM design_standard.v_section_tree WHERE code LIKE '1.%';")


if __name__ == "__main__":
    main()
