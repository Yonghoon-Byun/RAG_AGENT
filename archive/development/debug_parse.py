import json
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 파일 로드
with open(r'd:\DATA\RAG_AGENT\design_standards_db_example.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 섹션 3 가져오기
section_3 = next((s for s in data if s['code'] == '3'), None)

if section_3:
    title_text = section_3['title']
    lines = title_text.split('\n')

    print("=" * 80)
    print("섹션 3 디버깅")
    print("=" * 80)
    print(f"\n전체 길이: {len(title_text)} chars")
    print(f"줄 수: {len(lines)}")
    print(f"\n첫 10줄:")
    for i, line in enumerate(lines[:10]):
        print(f"  {i}: '{line}'")

    # 패턴 테스트
    parent_code = '3'
    pattern = rf'^({re.escape(parent_code)}\.\d+(?:\.\d+)*)\s+(.+?)$'

    print(f"\n정규표현식 패턴: {pattern}")
    print("\n매칭 테스트:")

    match_count = 0
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue

        match = re.match(pattern, line_stripped)
        if match:
            match_count += 1
            print(f"  [매칭 {match_count}] 줄 {i}: '{line_stripped[:60]}'")
            print(f"    -> Code: {match.group(1)}, Title: {match.group(2)[:40]}")
        elif line_stripped.startswith('3.'):
            print(f"  [불일치] 줄 {i}: '{line_stripped[:60]}'")

    print(f"\n총 {match_count}개 매칭됨")
