# ⚡ Quick Start Guide

프로젝트를 빠르게 시작하기 위한 간단한 가이드입니다.

## 📂 프로젝트 구조

```
RAG_AGENT/
├── 📄 문서
│   ├── README.md              ← 시작은 여기서!
│   ├── README_DB_SETUP.md     ← 데이터베이스 상세 가이드
│   ├── PROJECT_SUMMARY.md     ← 프로젝트 완료 요약
│   └── QUICK_START.md         ← 이 문서
│
├── 🚀 실행 파일 (메인)
│   ├── run_restructure.py          ← JSON 재구성
│   └── insert_to_postgres.py       ← DB 삽입
│
├── 📊 데이터
│   ├── design_standards_db.json               ← 원본
│   └── design_standards_db_restructured.json  ← 재구성 완료
│
├── 📁 sql/
│   └── 01_create_tables.sql
│
└── 📁 archive/              ← 개발 과정 보관
```

## 🎯 3가지 주요 작업

### 1️⃣ JSON 재구성 (이미 완료됨 ✅)
```bash
python run_restructure.py
```
- **입력**: design_standards_db.json
- **출력**: design_standards_db_restructured.json
- **결과**: 28개 → 238개 섹션

### 2️⃣ PostgreSQL에 데이터 삽입 (이미 완료됨 ✅)
```bash
python insert_to_postgres.py
```
- **연결**: 10.0.0.20:2332/dde-water
- **테이블**: design_standard.design_sections
- **결과**: 238 rows 삽입 완료

### 3️⃣ DBeaver에서 확인
```sql
-- 전체 조회
SELECT * FROM design_standard.design_sections;

-- 검색
SELECT * FROM design_standard.search_sections('응집');

-- 계층 구조
SELECT * FROM design_standard.v_section_tree WHERE code LIKE '1.%';
```

## 🔗 DBeaver 연결 정보

```
Host: 10.0.0.20
Port: 2332
Database: dde-water
Schema: design_standard
Username: postgres
Password: postgres
```

## 📚 더 알아보기

| 문서 | 내용 |
|------|------|
| [README.md](README.md) | 전체 프로젝트 가이드 |
| [README_DB_SETUP.md](README_DB_SETUP.md) | DB 설정 및 쿼리 예시 |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | 완료 요약 및 통계 |

## ⚡ 5분 안에 시작하기

1. **DBeaver 연결** (위 정보 사용)
2. **데이터 확인**: `SELECT * FROM design_standard.design_sections LIMIT 10;`
3. **검색 테스트**: `SELECT * FROM design_standard.search_sections('응집');`
4. **완료!** 🎉

## 🆘 문제 발생시

1. **DB 연결 안됨**: README_DB_SETUP.md의 "트러블슈팅" 섹션 참고
2. **한글 검색 안됨**: 'simple' 텍스트 검색 설정 사용 중
3. **데이터 재삽입 필요**: `python insert_to_postgres.py` 재실행

---

**Tip**: Jupyter Notebook을 선호한다면 `restructure_json.ipynb`를 사용하세요!
