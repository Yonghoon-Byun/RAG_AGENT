# RAG Agent Project

토목설계 기준/지침 문서를 위한 RAG(Retrieval-Augmented Generation) 시스템 프로젝트

## 프로젝트 개요

정수시설 설계기준 문서를 계층 구조로 재구성하고, PostgreSQL 데이터베이스에 저장하여 RAG 시스템에서 활용할 수 있도록 구성하는 프로젝트입니다.

## 핵심 파일

### 데이터
- `data/design_standards_db.json` - 원본 설계기준 데이터 (28개 최상위 섹션)
- `data/design_standards_db_restructured.json` - 재구성된 데이터 (238개 섹션, 계층 구조)

### 스크립트
- `scripts/run_restructure.py` - JSON 계층 구조 재구성
- `scripts/insert_to_postgres.py` - PostgreSQL 데이터 삽입
- `scripts/analyze_excel.py` - KCI 엑셀 데이터 분석

### 노트북
- `notebooks/restructure_json.ipynb` - JSON 재구성 실험 노트북

### SQL
- `sql/01_create_tables.sql` - 테이블, 인덱스, 함수 정의

### 문서
- `docs/DB_SETUP.md` - 데이터베이스 설정 가이드
- `docs/QUICK_START.md` - 빠른 시작 가이드
- `docs/PROJECT_SUMMARY.md` - 프로젝트 요약
- `docs/GIT_SETUP_GUIDE.md` - Git/GitHub 설정 가이드

### 참고 자료
- `references/GraphRAG_paper.pdf` - GraphRAG 논문
- `references/KCI_*.json|xlsx` - KCI 논문 데이터

## 데이터베이스 정보

```
Host: 10.0.0.20
Port: 2332
Database: dde-water
Schema: design_standard
Table: design_sections (238 rows)
```

## 청킹 전략 계획

### 단기 계획 (1-2주)
- `.omc/plans/short-term-chunking-strategy.md` - 벡터 검색 프로토타입

### 장기 계획 (10주)
- `.omc/plans/industrial-rag-chunking-strategy.md` - GraphRAG 통합 전략

## 기술 스택

- Python 3.11+
- PostgreSQL 15+ (pgvector)
- OpenAI API (text-embedding-3-small)

## 개발 명령어

```bash
# JSON 재구성
python scripts/run_restructure.py

# DB 삽입
python scripts/insert_to_postgres.py

# 토큰 분석 (향후)
python scripts/analyze_tokens.py
```

## 참고 문서

- GraphRAG 논문: `references/GraphRAG_paper.pdf` ("From Local to Global: A GraphRAG Approach to Query-Focused Summarization")
- 핵심 파라미터: 600 토큰 청크, 100 토큰 오버랩
