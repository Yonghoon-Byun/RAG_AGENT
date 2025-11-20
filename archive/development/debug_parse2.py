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

    print("=" * 80)
    print("원본 텍스트 분석")
    print("=" * 80)
    print(f"텍스트 길이: {len(title_text)}")
    print(f"\n첫 200자:")
    print(repr(title_text[:200]))

    print(f"\n개행 문자열 확인:")
    newline_in = '\n' in title_text
    escaped_newline_in = '\\n' in title_text
    print(f"  단일 개행(\\n)포함: {newline_in}")
    print(f"  이스케이프 개행(\\\\n) 포함: {escaped_newline_in}")

    # replace 테스트
    print(f"\n개행문자 변환 테스트:")
    converted = title_text.replace('\\n', '\n')
    print(f"  변환 후 줄 수: {len(converted.split(chr(10)))}")

    lines = converted.split('\n')
    print(f"\n첫 10줄:")
    for i, line in enumerate(lines[:10]):
        print(f"  {i}: {repr(line[:60])}")

    # 패턴 매칭
    pattern = r'^(3\.\d+(?:\.\d+)*)\s+(.+?)$'
    print(f"\n패턴: {pattern}")
    print(f"매칭 결과:")
    for i, line in enumerate(lines[:20]):
        line = line.strip()
        if line.startswith('3.'):
            match = re.match(pattern, line)
            if match:
                print(f"  [OK] 줄 {i}: code={match.group(1)}, title={match.group(2)[:30]}")
            else:
                print(f"  [FAIL] 줄 {i}: {repr(line[:60])}")
