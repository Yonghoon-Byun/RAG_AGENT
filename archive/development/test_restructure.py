import json
import re
from typing import Dict, List, Any
import sys

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 1. 원본 파일 로드
input_file = r'd:\DATA\RAG_AGENT\design_standards_db_example.json'
output_file = r'd:\DATA\RAG_AGENT\design_standards_db_example_restructured.json'

print("=" * 80)
print("JSON 구조 재구성 테스트")
print("=" * 80)

# 파일 로드
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"\n[OK] 총 {len(data)}개의 최상위 섹션 로드됨")
for item in data[:5]:
    print(f"  - Code: {item['code']}, Title: {item['title'][:50]}...")

# 2. 구조 분석 함수
def analyze_section_structure(section: Dict) -> Dict[str, Any]:
    """섹션의 구조를 분석합니다."""
    has_children = len(section.get('children', [])) > 0
    title = section.get('title', '')
    content = section.get('content', '')

    # title에 하위 섹션 코드 패턴이 있는지 확인 (예: 3.1, 3.2)
    code = section.get('code', '')
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

# 전체 데이터 분석
print("\n" + "=" * 80)
print("섹션별 구조 분석:")
print("=" * 80)
for section in data:
    analysis = analyze_section_structure(section)
    if analysis['needs_restructure']:
        print(f"[WARNING] Code {analysis['code']}: 재구성 필요!")
    else:
        print(f"[OK] Code {analysis['code']}: 정상 구조")
    print(f"   - Children: {analysis['has_children']}, "
          f"Content in Title: {analysis['content_in_title']}, "
          f"Title Length: {analysis['title_length']}")

print("\n테스트 완료!")
