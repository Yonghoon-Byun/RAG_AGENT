"""
JSON 구조 재구성 스크립트
평면 구조(title에 모든 내용)를 계층 구조로 변환
"""

import json
import re
from typing import Dict, List, Any
import sys

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ============================================================================
# 설정
# ============================================================================
INPUT_FILE = r'd:\DATA\RAG_AGENT\design_standards_db.json'
OUTPUT_FILE = r'd:\DATA\RAG_AGENT\design_standards_db_restructured.json'

# ============================================================================
# 함수 정의
# ============================================================================

def analyze_section_structure(section: Dict) -> Dict[str, Any]:
    """섹션의 구조를 분석합니다."""
    has_children = len(section.get('children', [])) > 0
    title = section.get('title', '')
    content = section.get('content', '')
    code = section.get('code', '')

    # title에 하위 섹션 코드 패턴이 있는지 확인 (예: 3.1, 3.2)
    pattern = rf'{re.escape(code)}\.\d+'
    content_in_title = bool(re.search(pattern, title))

    return {
        'code': code,
        'has_children': has_children,
        'content_in_title': content_in_title,
        'content_length': len(content),
        'title_length': len(title),
        'needs_restructure': content_in_title and not has_children
    }


def parse_hierarchical_content(text: str, parent_code: str) -> List[Dict[str, Any]]:
    """
    평면 텍스트를 계층 구조로 파싱합니다.
    """
    # 섹션 헤더 패턴: "3.1 제목" 형태
    pattern = rf'^({re.escape(parent_code)}\.\d+(?:\.\d+)*)\s+(.+?)$'

    lines = text.split('\n')
    sections = []
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 섹션 헤더 매칭
        match = re.match(pattern, line)
        if match:
            # 이전 섹션 저장
            if current_section:
                sections.append(current_section)

            # 새 섹션 시작
            code = match.group(1)
            title = match.group(2).strip()
            current_section = {
                'code': code,
                'title': title,
                'content': '',
                'children': []
            }
        elif current_section:
            # 현재 섹션의 내용에 추가
            if current_section['content']:
                current_section['content'] += '\n' + line
            else:
                current_section['content'] = line

    # 마지막 섹션 저장
    if current_section:
        sections.append(current_section)

    return sections


def build_hierarchy(sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    평면 섹션 리스트를 계층 구조로 변환합니다.
    """
    if not sections:
        return []

    # 코드 레벨 계산 (점의 개수)
    def get_level(code: str) -> int:
        return code.count('.')

    # 부모 코드 찾기
    def get_parent_code(code: str) -> str:
        parts = code.rsplit('.', 1)
        return parts[0] if len(parts) > 1 else None

    # 섹션 딕셔너리 생성 (빠른 검색용)
    section_dict = {s['code']: s for s in sections}

    # 최상위 레벨 찾기
    root_level = min(get_level(s['code']) for s in sections)
    root_sections = [s for s in sections if get_level(s['code']) == root_level]

    # 각 섹션을 부모에 연결
    for section in sections:
        parent_code = get_parent_code(section['code'])
        if parent_code and parent_code in section_dict:
            parent = section_dict[parent_code]
            if section not in parent['children']:
                parent['children'].append(section)

    return root_sections


def restructure_section(section: Dict[str, Any]) -> Dict[str, Any]:
    """단일 섹션을 재구성합니다."""
    analysis = analyze_section_structure(section)

    if not analysis['needs_restructure']:
        # 재구성 불필요 - 원본 반환 (하위 섹션은 재귀적으로 처리)
        return {
            'code': section['code'],
            'title': section['title'],
            'content': section['content'],
            'children': [restructure_section(child) for child in section.get('children', [])]
        }

    # 재구성 필요
    print(f"  [재구성] Code {section['code']}")

    # title에서 실제 제목과 본문 분리
    title_text = section['title']
    # 이스케이프된 개행문자를 실제 개행문자로 변환
    title_text = title_text.replace('\\n', '\n')
    lines = title_text.split('\n')

    # 첫 번째 줄이 제목
    actual_title = lines[0].strip()

    # 나머지는 본문
    remaining_text = '\n'.join(lines[1:]).strip()

    # 하위 섹션 파싱
    parsed_children = parse_hierarchical_content(remaining_text, section['code'])

    # 계층 구조 빌드
    hierarchical_children = build_hierarchy(parsed_children)

    # 본문 내용 추출 (하위 섹션 전 내용)
    if parsed_children:
        first_child_pattern = rf'{re.escape(parsed_children[0]["code"])}\s+{re.escape(parsed_children[0]["title"])}'
        match = re.search(first_child_pattern, remaining_text)
        if match:
            main_content = remaining_text[:match.start()].strip()
        else:
            main_content = section.get('content', '')
    else:
        main_content = remaining_text

    print(f"    -> {len(hierarchical_children)}개의 하위 섹션 생성됨")

    return {
        'code': section['code'],
        'title': actual_title,
        'content': main_content,
        'children': hierarchical_children
    }


def restructure_all(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """전체 데이터를 재구성합니다."""
    print("\n재구성 시작...")
    print("=" * 80)

    restructured = []
    for section in data:
        restructured_section = restructure_section(section)
        restructured.append(restructured_section)

    print("=" * 80)
    print("재구성 완료!\n")

    return restructured


def print_structure(section: Dict[str, Any], indent: int = 0):
    """섹션 구조를 트리 형태로 출력합니다."""
    prefix = "  " * indent
    title_preview = section['title'][:40] + "..." if len(section['title']) > 40 else section['title']
    content_len = len(section['content'])
    children_count = len(section['children'])

    print(f"{prefix}[{section['code']}] {title_preview}")
    print(f"{prefix}    (Content: {content_len} chars, Children: {children_count})")

    for child in section['children']:
        print_structure(child, indent + 1)


def count_sections(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """전체 섹션 수를 재귀적으로 계산합니다."""
    total = 0
    by_level = {}

    def count_recursive(sections, level=1):
        nonlocal total
        count = len(sections)
        total += count
        by_level[level] = by_level.get(level, 0) + count

        for section in sections:
            if section['children']:
                count_recursive(section['children'], level + 1)

    count_recursive(data)
    return {'total': total, 'by_level': by_level}


# ============================================================================
# 메인 실행
# ============================================================================

def main():
    print("=" * 80)
    print("JSON 구조 재구성 - Lab Scale")
    print("=" * 80)

    # 1. 파일 로드
    print(f"\n[1단계] 파일 로드: {INPUT_FILE}")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"  -> {len(data)}개의 최상위 섹션 로드됨")

    # 2. 구조 분석
    print(f"\n[2단계] 구조 분석")
    needs_restructure = []
    for section in data:
        analysis = analyze_section_structure(section)
        if analysis['needs_restructure']:
            print(f"  [WARNING] Code {analysis['code']}: 재구성 필요 (Title: {analysis['title_length']} chars)")
            needs_restructure.append(analysis['code'])
        else:
            print(f"  [OK] Code {analysis['code']}: 정상 구조")

    print(f"\n  총 {len(needs_restructure)}개 섹션이 재구성 필요")

    # 3. 재구성 실행
    print(f"\n[3단계] 재구성 실행")
    restructured_data = restructure_all(data)

    # 4. 결과 검증
    print(f"\n[4단계] 결과 검증")
    print("재구성된 데이터 구조:")
    print("-" * 80)
    for section in restructured_data:
        print_structure(section)
        print()

    # 5. 통계
    print(f"\n[5단계] 통계")
    original_stats = count_sections(data)
    restructured_stats = count_sections(restructured_data)

    print("=" * 80)
    print(f"원본 섹션 수: {original_stats['total']}")
    print(f"재구성 섹션 수: {restructured_stats['total']}")
    print(f"\n레벨별 섹션 수 (재구성 후):")
    for level, count in sorted(restructured_stats['by_level'].items()):
        print(f"  Level {level}: {count}개")

    # 6. 파일 저장
    print(f"\n[6단계] 파일 저장: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(restructured_data, f, ensure_ascii=False, indent=4)

    import os
    original_size = os.path.getsize(INPUT_FILE)
    new_size = os.path.getsize(OUTPUT_FILE)

    print(f"  원본 크기: {original_size:,} bytes")
    print(f"  재구성 크기: {new_size:,} bytes")
    print(f"  차이: {new_size - original_size:+,} bytes ({(new_size/original_size - 1)*100:+.1f}%)")

    print("\n" + "=" * 80)
    print("[완료] Lab scale 테스트 성공!")
    print("=" * 80)
    print("\nPilot scale 적용:")
    print("  1. 코드가 잘 작동하는지 확인")
    print("  2. INPUT_FILE을 'design_standards_db.json'로 변경")
    print("  3. 다시 실행")


if __name__ == "__main__":
    main()
