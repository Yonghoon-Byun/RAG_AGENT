"""
Excel 파일 구조 분석 스크립트
KCI 논문 데이터의 구조와 기본 통계를 확인합니다.
"""

import pandas as pd
import sys

# Windows 콘솔 인코딩 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

EXCEL_FILE = r'd:\DATA\RAG_AGENT\KCI_excel_2025482411536.xlsx'

def analyze_excel():
    """Excel 파일의 구조와 내용을 분석합니다."""

    print("=" * 80)
    print("Excel 파일 구조 분석")
    print("=" * 80)

    try:
        # Excel 파일 로드
        print(f"\n[1단계] Excel 파일 로드 중...")
        print(f"  파일: {EXCEL_FILE}")

        # 시트 목록 확인
        xl_file = pd.ExcelFile(EXCEL_FILE)
        print(f"\n  발견된 시트: {xl_file.sheet_names}")

        # 첫 번째 시트 로드 (또는 모든 시트)
        sheet_name = xl_file.sheet_names[0]
        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)

        print(f"\n[OK] 데이터 로드 완료!")
        print(f"  시트명: {sheet_name}")
        print(f"  전체 행 수: {len(df):,}개")
        print(f"  전체 컬럼 수: {len(df.columns)}개")

        # 컬럼 정보
        print("\n" + "=" * 80)
        print("[2단계] 컬럼 구조")
        print("=" * 80)
        print("\n컬럼명 목록:")
        for idx, col in enumerate(df.columns, 1):
            null_count = df[col].isna().sum()
            null_pct = (null_count / len(df)) * 100
            dtype = df[col].dtype
            print(f"  {idx:2d}. {col:30s} (타입: {dtype}, 결측: {null_count}/{len(df)} = {null_pct:.1f}%)")

        # 기본 통계
        print("\n" + "=" * 80)
        print("[3단계] 기본 통계")
        print("=" * 80)

        # 연도 관련 컬럼 찾기
        year_cols = [col for col in df.columns if '년' in col or 'year' in col.lower() or '발행' in col]
        if year_cols:
            print(f"\n연도 관련 컬럼: {year_cols}")
            for col in year_cols:
                print(f"\n  [{col}] 분포:")
                year_dist = df[col].value_counts().sort_index()
                for year, count in year_dist.items():
                    print(f"    {year}: {count}개")

        # 샘플 데이터
        print("\n" + "=" * 80)
        print("[4단계] 샘플 데이터 (첫 5개 행)")
        print("=" * 80)
        print("\n" + df.head(5).to_string())

        # 데이터 타입별 요약
        print("\n" + "=" * 80)
        print("[5단계] 데이터 요약")
        print("=" * 80)

        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_cols) > 0:
            print("\n숫자형 컬럼 통계:")
            print(df[numeric_cols].describe())

        text_cols = df.select_dtypes(include=['object']).columns
        if len(text_cols) > 0:
            print(f"\n텍스트형 컬럼: {len(text_cols)}개")
            for col in text_cols[:5]:  # 처음 5개만
                unique_count = df[col].nunique()
                print(f"  - {col}: {unique_count}개 고유값")

        # 키워드 관련 컬럼 찾기
        keyword_cols = [col for col in df.columns if '키워드' in col or 'keyword' in col.lower()]
        if keyword_cols:
            print(f"\n키워드 관련 컬럼: {keyword_cols}")
            for col in keyword_cols:
                print(f"\n  [{col}] 샘플:")
                sample_keywords = df[col].dropna().head(3)
                for idx, kw in enumerate(sample_keywords, 1):
                    print(f"    {idx}. {kw}")

        print("\n" + "=" * 80)
        print("[완료] 분석 완료!")
        print("=" * 80)

        # 다음 단계 제안
        print("\n[분석 결과 기반 추천]")
        print(f"  • 총 {len(df):,}개 논문 데이터")

        if len(df) < 100:
            print("  → 추천: Claude Desktop에 직접 업로드 (소량 데이터)")
        elif len(df) < 1000:
            print("  → 추천: Python pandas로 분석 (중간 규모)")
        else:
            print("  → 추천: PostgreSQL DB 구축 (대량 데이터)")

        return df

    except Exception as e:
        print(f"\n[ERROR] 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    df = analyze_excel()

    if df is not None:
        print("\n[다음 작업]")
        print("  1. DB 저장이 필요하면: create_paper_db_schema.py 실행")
        print("  2. pandas 분석이 필요하면: analyze_trend.py 실행")
        print("  3. Claude Desktop 사용: Excel 파일 직접 업로드")
