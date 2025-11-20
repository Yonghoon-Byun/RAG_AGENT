# Archive 폴더

이 폴더는 프로젝트 개발 과정에서 생성된 테스트 및 디버깅 파일들을 보관합니다.

## 📁 폴더 구조

```
archive/
├── development/          # 개발 과정 스크립트
│   ├── debug_parse.py        # JSON 파싱 디버깅 스크립트 #1
│   ├── debug_parse2.py       # JSON 파싱 디버깅 스크립트 #2
│   └── test_restructure.py   # 재구성 테스트 스크립트
│
└── test_data/           # 테스트용 샘플 데이터
    ├── design_standards_db_example.json                # 샘플 원본 (4개 섹션)
    └── design_standards_db_example_restructured.json   # 샘플 재구성 결과
```

## 📄 파일 설명

### development/

#### debug_parse.py
- **목적**: JSON 파싱 문제 디버깅
- **이슈**: title 필드에 `\n`이 이스케이프된 문자열로 저장됨
- **결과**: 개행 문자 변환 로직 개발

#### debug_parse2.py
- **목적**: 개행 문자 처리 검증
- **테스트**: `replace('\\n', '\n')` 변환 확인
- **결과**: 파싱 로직 수정 완료

#### test_restructure.py
- **목적**: Lab-scale 테스트 (샘플 데이터)
- **기능**: 구조 분석 및 재구성 필요 섹션 감지
- **결과**: 코드 3, 4번 섹션 재구성 필요 확인

### test_data/

#### design_standards_db_example.json
- **크기**: 38,587 bytes
- **섹션 수**: 4개 (코드 1, 2, 3, 4)
- **용도**: Lab-scale 테스트용 샘플 데이터
- **특징**: 코드 3, 4번이 평면 구조

#### design_standards_db_example_restructured.json
- **크기**: 39,678 bytes (+2.8%)
- **섹션 수**: 35개
- **용도**: 재구성 결과 검증
- **결과**: 성공적으로 계층 구조로 변환됨

## 🔬 개발 과정

### 문제 1: JSON 파싱 실패
**증상**: 하위 섹션이 0개로 파싱됨
**원인**: title 필드에 `\\n\\n`이 문자열로 저장됨
**해결**: `text.replace('\\n', '\n')` 추가

### 문제 2: 정규표현식 매칭 실패
**증상**: 섹션 헤더 패턴 매칭 안됨
**원인**: 개행 문자 변환 전에 split() 실행
**해결**: 변환 순서 조정

### 문제 3: 재귀 쿼리 타입 오류
**증상**: PostgreSQL 재귀 CTE에서 타입 불일치
**원인**: VARCHAR(50)과 TEXT 타입 혼용
**해결**: 명시적 타입 캐스팅 (`::TEXT`)

### 문제 4: 한글 전문 검색 설정 없음
**증상**: `text search configuration "korean" does not exist`
**원인**: PostgreSQL에 한글 검색 설정 미설치
**해결**: `'simple'` 설정 사용으로 대체

## 📊 테스트 결과

### Lab-scale 테스트 (example 데이터)
- ✅ 4개 섹션 → 35개 섹션 변환
- ✅ 코드 3번: 6개 하위 섹션 생성
- ✅ 코드 4번: 3개 하위 섹션 생성
- ✅ 파일 크기: +2.8% 증가

### Pilot-scale 테스트 (전체 데이터)
- ✅ 28개 섹션 → 238개 섹션 변환
- ✅ PostgreSQL 삽입 성공
- ✅ 계층 구조 보존 확인
- ✅ 검색 기능 작동 확인

## 🎓 교훈

1. **Lab-scale → Pilot-scale 접근**: 작은 샘플로 먼저 테스트
2. **점진적 디버깅**: 단계별로 문제 해결
3. **타입 명시**: PostgreSQL에서 명시적 타입 캐스팅 중요
4. **환경 차이 고려**: 한글 검색 설정 등 환경 의존성 처리

## 🗑️ 보관 기준

이 폴더의 파일들은:
- ✅ 개발 과정 기록
- ✅ 디버깅 참고자료
- ✅ 테스트 케이스 보존
- ❌ 최종 배포 비포함

## 🔄 최종 버전

프로덕션 사용을 위한 최종 버전은 상위 폴더의 다음 파일들을 사용하세요:

- **run_restructure.py**: JSON 재구성
- **insert_to_postgres.py**: DB 삽입
- **design_standards_db_restructured.json**: 재구성된 데이터

---

**Note**: 이 파일들은 삭제하지 마세요. 향후 유사한 문제 발생 시 참고자료로 활용됩니다.
