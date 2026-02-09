# KCI 논문 목록 (머신러닝/딥러닝 관련)

총 74편의 논문

---

## 1. 머신러닝&딥러닝 모델을 활용한 댐 일유입량 예측시 융적설을 고려하기 위한 데이터 전처리에 대한 방법 연구

**저자명**: 조영식;정관수

**주저자 소속기관**: Department of Civil Engineering, Chungnam National University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 머신러닝, 딥러닝, 일유입량예측, 데이터전처리, 융적설

**초록**: 댐유입량 예측에 대하여 데이터 기반 머신러닝 및 딥러닝(Machine Learning & Deep Learning, ML&DL) 분석도구들이 공개되어 다양한 분야에서 ML&DL의 적용연구가 활발히 진행되고 있으며, 모델의 자체 성능향상 뿐만 아니라 모델의 특성을 고려한 데이터의 전처리도 댐유입량을 정확하게 예측하게 하는 중요한 모델성능 향상의 요소라고 할 수 있다. 특히 기존 강우자료는 적설량을 열선 설비를 통하여 녹여 강우량으로 환산되어 있으므로, 융적설에 따른 강우와 유입량의 상관관계를 왜곡하게 된다. 따라서 본연구에서는 소양강댐과 같이 융적설의 영향을 받는 댐유역에 대한 댐일유입량 예측시 겨울에 강설량이 적설이 되어 적게 유출되는 현상과, 봄에 융설로 인하여 무강우나 적은 비에도 많은 유출이 일어나는 물리적 현상을 ML& DL모델로 적용하기 위하여 필요한 강우 데이터의 전처리에 대한 연구를 수행 하였다. 강우계열, 유입량계열을 조합하여 3가지 머신러닝(SVM, RF, LGBM)과 2가지 딥러닝(LSTM, TCN) 모델을 구축하고, 최적 하이퍼파라메터 튜닝을 통하여 적합 모델을 적용하고 한 결과, NSE 0.842~0.894로 높은 수준의 예측성능을 나타내었다. 또한 융적설을 반영한 강우보정 데이터를 만들기 위하여 융적설 모의 알고리즘을 개발하고, 이를 통하여 산정된 보정강우를 머신러닝 및 딥러닝 모델에 적용한 결과 NSE 0.841~0.896 으로 융적설 적용전과 비슷한 높은 수준의 예측 성능을 나타내었으나, 융적설 기간에는 조정된 강우로 학습되어 예측되었을 때 실측유입량에 근접하는 모의결과를 나타내었다. 결론적으로, 융적설이 영향을 미치는 유역에서의 데이터 모델 적용시에는 입력자료 구축시 적설 및 융설이 물리적으로 타당한 강우-유출 반응에 적합하도록 전처리과정이 중요함을 밝혔다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 2. XGBoost 머신러닝 기반 쉴드 TBM 지반침하 예측

**저자명**: 신재우;김윤희;이소이;김범주

**주저자 소속기관**: 동국대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: 쉴드 TBM, XGBoost, 머신러닝, 지반침하

**초록**: 본 연구에서는 도심지 쉴드 TBM (tunnel boring machine) 터널 시공 중 발생하는 지반침하를 예측하기 위한 XGBoost (eXtreme Gradient Boosting) 머신러닝 모델을 개발하고, 그 성능을 평가하였다. 기존 연구들에서 주로 터널 후방의 침하를 예측하는 연구가 많았던 반면, 본 연구에서는 실시간 쉴드 TBM 시공 데이터를 활용하여 터널의 후방 침하뿐 아니라 전방 침하에 대한 예측도 시도하였다. 이를 위해 이수가압식 쉴드 TBM으로 시공한 터널 현장 데이터를 제공받아 지반 조건, TBM 굴진자료 , 터널 기하 조건 등을 분석하고 17개의 머신러닝 모델 입력변수를 선정하였다. 선정된 17개의 입력변수에 대해 쉴드 TBM 본체를 기준으로 전방 예측 범위(세그먼트 25링 전방, CASE 1), 중앙부(TBM 본체 상부, CASE 2), 후방 예측 범위(세그먼트 25링 후방, CASE 3) 등 세 범위로 구분하고 각 범위에 대하여 입력변수와 침하량 간의 상관관계를 분석하였다. 그리고 각 CASE별로, 즉 터널 전방(CASE 1), 중앙(CASE 2), 후방(CASE 3) 위치에 대해서 XGBoost 머신러닝 알고리즘을 적용한 지반침하 예측 모델을 구축하고 베이지안 최적화와 5겹 교차 검증을 통해 하이퍼파라미터를 최적화하였다. 모델 평가결과, 후방 침하 예측 모델은 결정계수(R2)값이 0.82로 가장 높은 성능을 보인 반면, 전방 침하 예측 모델의 결정계수는 0.52로 상대적으로 낮은 성능을 나타내었다. 이러한 결과는 후방 침하 예측 정확도가 전방 예측보다 우수하고, 전방 예측의 경우 지반의 불확실성과 굴착 변수의 영향을 더 많이 받아 정확도가 낮아질 수 있음을 시사한다. 머신러닝 모델이 TBM 터널 시공 중 발생하는 지반침하, 특히 막장면 후방의 침하를 예측하는 데 효과적인 도구이나 아직 전방 침하의 예측 정확도를 높이기 위해서는 많은 추가 연구가 이루어져야 함을 확인하였다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 3. 머신러닝 기반 초음파 속도법을 활용한 고온 이력을 받은 콘크리트의 강도저하 회귀 예측 모델 개발

**저자명**: 김원창;김원창;이태규

**주저자 소속기관**: 세명대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 콘크리트, 고온, 머신러닝, 비파괴, 통계

**초록**: 본 연구에서는 고온 노출 후 UPV를 이용한 콘크리트 강도 예측에 관한 선행 연구 데이터를 활용하여 통계 분석 및 머신러닝 기반의 콘크리트 강도저하 예측 모델을 구축하고 평가하였다. 총 22개의 고온이력을 받은 콘크리트에 대한 UPV를 평가한 실험적 연구 데이터를 수집하고, W/C 비율을 4수준(W/C50, W/C40, W/C30, W/C20)로 분류했다. 상대적으로 W/C 비율이 낮을수록 높은 강도 저하의 범위의 영향에 의해 압축강도는 높은 평균과 표준편차를 보였으며 UPV는 유의미한 차이를 보이지 않았다. 4단계로 분류된 데이터에 대해 분산분석(ANOVA)을 실시한 결과, 압축강도 집단 간에는 p-value가 0.05 이상으로서 통계적으로 유의미한 차이를 보였으나 압축강도 잔존율은 유의미한 차이를 보이지 않았기 때문에 배합적 요소에 의해 민감한 영향을 적게 받을 수 있는 성능저하 모델을 구축하기 위해서는 종속 변수를 압축강도 잔존율로 설정할 필요가 있다. 기존 연구와 같이 단순･다중 선형회귀 분석을 수행한 결과에서 p값이 유의 수준인 0.05 미만으로서 통계적으로 유의한 결과를 보였으나 설명력(R2)은 약 0.47로 매우 낮았으며 잔차 검정에서 등분산성을 만족하지 못하였기 때문에 통계적으로 만족하지 못한 결과가 나타났다. 그러나, 머신러닝 기반 회귀 알고리즘을 이용한 모델 구축 및 평가 결과, ‘Randomforest’와 ‘XGBoost’는 R2 값이 0.92 이상, RMSE가 0.1 이하로 매우 우수한 성능을 보였다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2025

**주제분야**: 재료학

---

## 4. 데이터 증강 기법을 적용한 개선된 머신러닝 기반 TBM 디스크 커터 마모 예측

**저자명**: 염유리;최항석;양예림;권기범

**주저자 소속기관**: 고려대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: TBM, 디스크 커터, 마모, 데이터 증강, 머신러닝

**초록**: TBM (tunnel boring machine) 시공 중 디스크 커터의 과다 마모는 굴진 성능 저하를 유발할 수 있어, 이를 적시에 탐지하는 것이 중요하다. 디스크 커터 마모량 예측에 대한 다양한 연구가 수행되었으나, 과다 마모 탐지 성능 향상에 중점을 둔 연구는 부족한 실정이다. 본 연구에서는 데이터 증강 및 머신러닝 기반 디스크 커터 마모 등급 예측 모델을 구축하고, 데이터 증강 기법 적용에 따른 과다 마모 탐지 개선 효과를 분석하였다. 먼저, 토압식 쉴드 TBM 현장의 디스크 커터 교체 이력을 바탕으로 통계 분석을 수행하여, 링 당 마모량을 양호 등급(0.337 mm 미만)과 경고 등급(0.337 mm 이상)을 구분하였다. 두 가지 등급 간 데이터 불균형 문제를 해결하기 위해 SMOTE (synthetic minority oversampling technique)를 적용하였으며, 증강 데이터와 머신러닝 기법(Random Forest, eXtreme Gradient Boosting)을 활용하여 예측 모델을 개발하였다. 데이터 증강 적용 결과, 정확도와 F1 score가 향상되었고 양호 등급-경고 등급 간 예측 성능 불균형 수준이 감소하였다. 이는 과다 마모 데이터의 증강이 과다 마모 발생 메커니즘 학습에 효과적으로 기여한 결과로 판단된다. 특성 중요도 분석을 통해 커터 회전 거리 커터 마모 예측에 가장 영향도가 높음을 확인하였고, 이는 커터헤드 외측에 상대적으로 좁은 커터 배치 간격 설계의 필요성을 보여준다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 5. 머신러닝 알고리즘을 이용한 콘크리트 슬럼프 플로 기반의 콘크리트 레올로지 정수 예측 모델 개발

**저자명**: 이유정;김인태;한동엽

**주저자 소속기관**: 경상국립대학교 건축공학과

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 레올로지, 콘크리트, 머신러닝, 인공신경망

**초록**: 본 연구에서는 머신러닝 알고리즘을 활용한 기존의 콘크리트 슬럼프 플로 시험 결과를 바탕으로 콘크리트 레올로지 정수 예측 모델을 개발하는 것을 목표로 한다. 본 연구에서는 연구 목적을 달성하기 위해 데이터 전처리, 품질, 훈련 데이터 개수에 따른 예측 모델의 성능을 분석하였다. 분석 결과, Data Cleaning과 데이터 정규화를 모두 적용하는 데이터 전처리 방식이 모델의 성능 개선에 가장 효과적이었다. 또한 예측 모델의 학습 데이터의 품질이 높고 훈련 데이터의 수가 많을수록 예측 모델의 성능이 향상됨을 확인하였다. 본 연구를 통해 굳지않은 콘크리트의 슬럼프 플로 데이터를 기반으로 레올로지 정수 예측 모델을 개발하는 데 기여할 것으로 판단된다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2024

**주제분야**: 재료학

---

## 6. 머신러닝 기반의 제수밸브 누수 진단 및 압력차를 활용한 유량 예측 방법론의 개발

**저자명**: 이수민;정광준;김현준

**주저자 소속기관**: 주식회사 플로워크연구소 연구개발팀

**학술지명**: 상하수도학회지

**저자키워드**: 누수 진단, 제수밸브, 머신러닝, 유량 예측

**초록**: Gate valves are hydraulic components used to shut-off the water flow in water distribution systems. Gate valves may fail owing to various aspects such as leakage through seats, wearing of packing, and corrosion. Because it is considerably challenging to detect valve malfunctioning until the operator identifies a significant fault, failure of the gate valve may lead to a severe accident event associated with water distribution systems. In this study, we proposed a methodology to diagnose the faults of gate valves. To measure the pressure difference across a gate valve, two pressure transducers were installed before and after the gate valve in a pilot-scaled water distribution system. The obtained time-series pressure difference data were analyzed using a machine learning algorithm to diagnose faults. The validation of whether the flow rate of the pipeline can be predicted based on the pressure difference between the upstream and downstream sides of the valve was also performed.

**발행기관명**: 대한상하수도학회

**발행연도**: 2023

**주제분야**: 상하수도공학

---

## 7. 터널 세그먼트 라이닝의 뒤채움 그라우트 결함 탐지를 위한 딥러닝 기반 GPR 철근 클러터 제거 모델

**저자명**: 김윤서;황채민;김형주;최항석

**주저자 소속기관**: 고려대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: TBM 터널, GPR 탐사, 결함 탐지, 머신 러닝, 이미지 분할

**초록**: 지표투과 레이더(ground penetrating radar, GPR)는 고주파 전자기파를 이용하여 지중의 결함을 탐지하는 비파괴 탐사 기법이다. GPR은 넓은 탐지 범위와 짧은 데이터 획득 시간을 제공하므로, 쉴드 TBM 세그먼트 라이닝 배면의 뒤채움 그라우트에 대한 상태 평가에 적합하다. 그러나 철근이 포함된 세그먼트 라이닝에서는 철근의 차폐 효과로 인해 GPR 이미지에 클러터(clutter)가 발생하며, 이로 인해 그라우트 내 결함 신호가 가려져 신뢰성 있는 평가를 어렵게 한다. 본 연구에서는 이러한 한계를 극복하기 위해 딥러닝 기반 이미지 분할 기법을 적용한 철근 클러터 제거 모델을 개발하여 결함 신호의 가시성을 개선하였다. 이를 위해 유한차분 시간영역(finite-difference time-domain, FDTD) 기반 GPR 수치해석 모델을 통해 데이터베이스를 구축하고, FCN (fully convolutional networks)과 Deeplab V3+ 등의 이미지 분할 기법을 적용하여 모델을 학습하였다. 각 기법의 성능은 PSNR, SSIM, MS-SSIM의 세 가지 이미지 유사도 지표를 활용해 평가하였다. 그 결과, Deeplab V3+가 FCN보다 우수한 클러터 제거 성능을 보였으며 결함 신호의 가시성을 효과적으로 향상시키는 것으로 확인되었다. 제안된 모델은 세그먼트 라이닝 뒤채움 그라우트의 결함 식별률을 개선하고 세그먼트 유지관리의 효율성을 높여, TBM 터널의 내구성 확보와 사용 수명 연장 등에 기여할 수 있을 것으로 기대된다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 8. SCM 함량에 따른 고온 노출 콘크리트 강도 예측을 위한 앙상블모델 적용

**저자명**: 민하은;김희선

**주저자 소속기관**: 이화여자대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 콘크리트, 고온, 혼화재, 압축강도, 머신러닝 기법

**초록**: 콘크리트는 화재와 같은 고온에 노출되는 경우 물리적, 화학적 변화가 발생하여 압축강도가 현저히 저하된다. 고온에 노출된 콘크리트의 강도를 평가하기 위해 전통적인 실험 방법을 사용하는 것은 시간과 비용이 많이 소요될 뿐만 아니라, 콘크리트 배합비와 같은 다양한 변수의 영향을 종합적으로 고려하기 어렵다는 한계가 있다. 이러한 문제를 해결하고자 최근 머신러닝(ML) 기법 중 앙상블 모델을 활용하여 화재 시 콘크리트의 압축강도를 예측하려는 시도가 다수 이루어졌으나, 앙상블 모델 간의 예측 성능을 비교 평가한 연구는 상대적으로 부족한 실정이다. 이에 본 연구는 Gradient Boosting Regressor (GBR), Extreme Gradient Boosting Regressor (XGBR), Categorical Gradient Boosting (CatBoost), Random Forest (RF), Extra Trees, 5가지 앙상블 모델을 비교 평가하여 혼화재가 혼입된 콘크리트의 고온 노출 시 압축강도를 예측하는 데 적합한 모델을 제안하고자 하였다. 각 모델의 예측 성능을 결정계수(R²), 평균제곱근오차(RMSE), 평균절대오차(MAE) 지표를 기준으로 평가한 결과, CatBoost 모델이 가장 높은 예측 정확도를 보였으며, 변수 중요도 분석을 통해 물-결합재 비율과 가열 온도가 주요 영향 변수임을 확인하였다. 또한, 모델의 학습 과정에 사용되지 않은 새로운 데이터를 활용하여 CatBoost 및 ET 모델의 예측 성능을 검증한 결과, CatBoost가 실험 결과와 더 높은 일치를 보임으로써 우수한 예측 성능을 입증하였다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2025

**주제분야**: 재료학

---

## 9. 디스크커터 개별 굴착 거리를 고려한 마모량 예측 머신러닝 모델

**저자명**: 김동구;신영진;권기범;이철희;김동규;최항석

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: 디스크커터 마모도 예측, 머신러닝, 쉴드 TBM 최적 운영 기법

**초록**: 쉴드 TBM을 활용한 터널 굴착 사례가 증가하면서, 공기 단축 및 경제성 향상을 위한 연구가 활발히 진행되고 있다. 정확한 디스크커터 교체(cutter head intervention, CHI) 주기 예측은 TBM 다운타임 감소와 디스크커터 사용 효율 증대를통해 TBM을 활용한 터널 공사의 경제성을 높일 수 있다. 특히, 계획된 교체 주기와 실제 교체 횟수 또는 수량 간의 차이를 최소화함으로써 예상보다 잦은 교체로 인한 다운타임 증가와 비용 상승을 방지하는 데 기여한다. 본 연구에서는 쉴드TBM 막장면에 설치된 각 커터의 굴착 이동 거리를 고려하여 디스크 커터 마모량을 예측하는 머신러닝 모델을 개발하였다. 머신러닝 모델의 디스크커터 마모량 예측 정확도를 검증하기 위하여 국내 터널현장 경암지반 구간에서 수집된 TBM운영데이터 및 CHI 기록을 활용하였으며, 디스크커터의 마모를 유발하는 9가지 영향인자의 마모 영향도를 평가하였다. 본 연구에서 제시된 디스크커터 마모 예측 모델은 교체 주기의 정확도를 높여 기존 예측 방법론을 개선하고, 과도한 교체로 인한 다운타임과 비용 상승을 줄여 국내 쉴드 TBM의 공사비용 저감에 기여할 것으로 기대된다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 10. LSTM을 이용한 상수도 시스템 실시간 데이터 예측

**저자명**: 조은영;최선홍;정한나;장동우

**주저자 소속기관**: Department of Civil and Environmental Engineering, Incheon National University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 데이터 예측, LSTM, 머신러닝, 실시간 데이터, 상수도

**초록**: 국내 수도관의 보급률은 99% 이상이며, 이에 노후 수도관이 증가하고 있고, 상수관로 내 수리 및 수질 사고의 발생 위험을 높여 대책 마련이 시급한 실정이다. 적수 및 유충 사고 등 상수도에서 발생할 수 있는 다양한 사고에 대비하기 위하여 최근 실시간 모니터링 계측기가 관로에 설치되고 있고, 계측된 데이터를 활용한 연구의 중요성이 점차 증가하고 있다. 본 연구에서는 LSTM (Long Short-Term Memory) 방법을 이용하여 미래 상수도관 내 수리 및 수질 데이터를 예측하고자 하였다. 인천광역시 서구 소블럭의 유량, 수압, 잔류염소, pH 등 2개월의 시 단위 실시간 계측 데이터를 수집하였고, 결정계수와 RMSE (Root Mean Square Error)를 이용하여 LSTM 기법의 예측 정확도를 평가하였다. 장래 7일간의 상수도 인자별 데이터를 예측한 결과, 유량의 경우 R2가 최대 0.91로 높은 상관성을 보이는 것으로 나타났으며, 전기전도도, 수온, 잔류염소의 경우 0.8 이상의 값으로 높은 정확도를 보여주었다. 반면 수압의 경우 0.019의 낮은 값을 보여주었는데, 이는 LSTM 모델은 활용하는 데이터의 연속성 유무에 따라 예측 정확도에 영향을 받는 것으로 시사된다. LSTM을 통한 실시간 계측 데이터의 예측 결과는 상수도 관리와 사고 예방에 중요한 정보로 활용될 수 있으며, 사고 발생 시 대응 능력을 향상시키는 데 도움이 될 것으로 기대된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 11. TBM 디스크 커터 비정상 마모 예측을 위한 데이터 증강 기반 머신러닝 연구

**저자명**: 염유리;최항석;양예림;박진수;권기범

**주저자 소속기관**: 고려대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: Tunnel boring machine, 디스크 커터, 비정상 마모, 머신러닝, 데이터증강

**초록**: 디스크 커터의 마모 예측에 관한 연구는 지속적으로 이루어져 왔으나, 정상 마모와 비정상 마모 간 발생 빈도 차이로 인해 대부분 정상 마모 예측에 초점을 두고 있으며, 비정상 마모에 대한 연구는 상대적으로 부족한 실정이다. 본 연구에서는 데이터 증강을 활용하여 비정상 마모 예측을 위한 머신러닝 모델을 구축하고, 모델 내 특성 중요도 및 그 영향 양상을 분석하였다. 토압식 쉴드 TBM 현장에서 수집된 데이터를 기반으로 마모 유형을 정상 마모와 비정상 마모로 분류하여 데이터세트를 구축하였다. Synthetic Minority Oversampling Technique (SMOTE)와 BorderlineSMOTE의 2가지 데이터 증강 기법을 도입하여 마모 유형 간의 불균형이 해소된 증강 데이터세트를 구축하였다. Random Forest (RF)와 eXtreme Gradient Boosting (XGB)의 머신러닝 기법을 기존 데이터세트와 2가지 증강 데이터세트에 각각 적용하여 총 6가지의 예측 모델을 개발하였다. 예측 성능을 비교한 결과, 증강 데이터 기반 모델은 기존 불균형 데이터 기반 모델에 비해 비정상 마모 탐지 성능이 약 18%에서 38%까지 크게 향상되었으며, 정상 마모와 비정상 마모 간의 성능 차이 또한 감소하는 경향을 보였다. 특히, 최적 모델인 RF-BorderlineSMOTE 모델의 경우에는 정상 마모와 비정상 마모에 대한 재현율이 각각 0.842와 0.836으로 유사하게 나타났으며, 이는 두 마모 유형 간의 결정 경계 인근 데이터를 중심으로 한 증강 방식이 비정상 마모 탐지에 효과적임을 시사한다. 또한, SHapley Additive exPlanation (SHAP) 분석에 따라 챔버압, 추력, 탄성계수가 예측 모델 내 주요 특성으로 식별되었으며, 챔버압과 추력은 비정상 마모 발생 가능성과 양의 상관성을, 탄성계수는 음의 상관성을 보였다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 12. 머신러닝 기법을 이용한 재해강도 분류모형 개발

**저자명**: 이승민;백선욱;이준학;김경탁;김수전;김형수

**주저자 소속기관**: 인하대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 자연재난, 표준 경보 기준, 머신러닝, 재해강도 분류모형

**초록**: 최근 급격한 도시화와 기후변화에 따라 재난에 의한 피해가 증가하고 있다. 국내 기상청에서는 표준 경보(주의보, 경보)를 전국적으로 통일된 표준 경보 기준(3시간 및 12시간 최대 누적강우량)에 따라 발령하여 재해에 따른 지역별, 재난 사상별 특성이 고려되지 않은 문제점이 있다. 따라서 본 연구에서는 서울특별시, 인천광역시, 경기도의 호우･태풍에 대한 재해 피해액 및 누적강우량을 활용하여 대상지역별 재해강도에 따른 단계별 기준을 설정하고, 강우에 따라 발생할 수 있는 재해의 강도를 분류하는 모형을 개발하고자 하였다. 즉, 본 연구에서는 호우･태풍에 의한 재해 피해액 누적 분포 함수의 분위별로 재해강도의 범주(관심, 주의, 경계, 심각 단계)를 분류하였고, 재해강도의 범주에 따른 누적강우량 기준을 대상 지자체별로 제시하였다. 그리고 지자체별 재해강도 분류모형 개발을 위해 4가지(의사결정나무, 서포트 벡터 머신, 랜덤 포레스트, XGBoost)의 머신러닝 모형을 활용하였는데 강우량, 누적강우량, 지속시간 최대 강우량(3시간, 12시간), 선행강우량을 독립변수로 이용하여 종속변수인 지자체별 재해강도를 분류하였다. 각 모형별 F1 점수를 이용한 정확도 평가 결과, 의사결정나무의 F1 점수가 0.56으로 가장 우수한 정확도를 보였다. 본 연구에서 제시한 머신러닝 기반 재해강도 분류모형을 활용하면 호우･태풍에 의한 재해에 대한 지자체별 위험 상태를 단계별로 파악할 수 있어, 재난 담당자들의 신속한 의사결정을 위한 기초 자료로 활용될 수 있을 것으로 판단된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 13. 불균형 데이터 처리를 통한 머신러닝 기반 TBM 굴진율 이상탐지 개선

**저자명**: 권기범;황병현;박현태;오주영;최항석

**주저자 소속기관**: 고려대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: 불균형 데이터, 머신러닝, 굴진율, SMOTE, TBM

**초록**: TBM (tunnel boring machine) 터널 프로젝트의 리스크 관리 측면에서 굴진율 예측은 중요하며, 이를 위한 머신러닝 기 반 TBM 굴진율 예측 연구가 지속적으로 진행되어 왔다. 그러나, 기존 연구의 머신러닝 예측 모델은 정상 굴진율과 이상 굴진율 간의 불균형 데이터를 고려하는 데 한계가 있다. 본 연구에서는 데이터 증강 기법을 통해 불균형 데이터를 처리하 여 머신러닝 기반 TBM 굴진율 이상탐지 성능을 개선하였다. 먼저, 상관관계 분석을 통해 유사 변수를 제거하여 6가지 입력특성을 선정하였다. 또한, 하위 10%와 상위 10%의 굴진율을 각각 이상 등급으로, 그 외 범위의 굴진율을 정상 등급 으로 굴진율 등급을 구분하였다. 기존 학습 데이터와 SMOTE (synthetic minority oversampling technique)를 통해 증 강된 학습 데이터를 각각 XGB (extreme gradient boosting)에 적용한 XGB 모델과 XGB-SMOTE 모델을 구축하였다. 굴진율 등급 예측 성능을 비교한 결과, XGB 모델은 정상 굴진율에 대한 예측 성능은 우수하나 이상 굴진율 예측 성능은 상대적으로 낮게 도출되었다. 반면, XGB-SMOTE 모델은 모든 굴진율 등급에서 일관되게 우수한 예측 성능을 보였다. 이는 SMOTE를 통한 이상 굴진율 데이터의 증강이 이상 굴진율을 유발하는 지반조건과 TBM 운영인자 간의 패턴 학습 수준을 향상시켰기 때문으로 판단된다. 결론적으로, 본 연구는 머신러닝 기반 TBM 굴진율 이상탐지 시 데이터 증강 기 법을 활용한 불균형 데이터 처리가 효과적임을 보여준다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 14. 선형회귀분석과 머신러닝을 이용한 암석의 강도 및 암석학적 특징 기반 세르샤 마모지수 추정

**저자명**: 홍주표;강윤성;고태영

**주저자 소속기관**: 강원대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: 디스크 커터 마모, 세르샤 마모지수, TBM, 회귀분석, 머신러닝

**초록**: TBM (Tunnel boring machine)은 터널 굴착 과정에서 여러 디스크 커터를 이용하여 암석을 절삭한다. 디스크 커터는 암석과의 지속적인 접촉과 마찰로 인해 마모된다. 디스크 커터의 표면이 마모되면 절삭 능력이 감소하고 굴착 효율이 떨어진다. 암석의 마모성은 디스크 커터 마모에 큰 영향을 미친다. 높은 마모도를 가진 암석은 커터에 더 큰 마모를 일으키며, 이는 디스크 커터의 수명을 단축시킨다. 세르샤 마모지수(Cerchar abrasivity index, CAI)는 암석의 마모성을 평가하는데 널리 사용되는 지표로 CAI는 암석의 마모특성을 나타내며, 디스크 커터의 수명과 성능 예측에 필수적인 요소로 인식되고 있다. 본 연구의 목적은 암석의 강도, 암석학적 특성과 선형회귀, 머신러닝 기법을 이용하여 CAI를 효과적으로 추정하는 새로운 방법을 개발하는 것이다. 문헌 조사를 통해 CAI, 일축압축강도, 압열인장강도, 등가석영함량이 포함된 데이터베이스를 구축하고 파생변수를 추가하였다. 통계적 유의성과 다중공선성을 고려하여 다중선형회귀분석을 위한 입력변수를 선정하였고, 머신러닝 모델의 입력변수는 변수중요도 분석을 통해 선정하였다. 머신러닝 예측모델 중 Gradient Boosting 모델의 예측 성능이 가장 높게 나타나 최적의 CAI 예측 모델로 선정되었다. 마지막으로 본 연구에서 도출한 다중선형회귀분석과 Gradient Boosting 모델의 예측 성능을 선행연구들의 CAI 예측모델과 비교하여 연구 결과의 타당성을 확인하였다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 15. 의사결정나무 및 랜덤포레스트 분류 모델을 이용한 교량 안전등급 예측

**저자명**: 홍지수;전세진

**주저자 소속기관**: 아주대학교

**학술지명**: 대한토목학회논문집(국문)

**저자키워드**: 머신러닝, 의사결정나무, 랜덤포레스트, 교량 안전등급, 유지관리

**초록**: 국내에서 공용연수 30년 이상인 노후 교량의 수가 급증하고 있다. 이에 따라 교량 노후도, 상태 및 성능 예측을 바탕으로 한 첨단 유지관리 기술의 중요성이 점차 주목받고 있다. 이 연구에서는 머신러닝 기반의 의사결정나무 및 랜덤포레스트 분류 모델을 사용하여 교량의 안전등급을 예측하는 방법을 제안하였다. 일반국도상 교량 8,850개를 대상으로 해당 모델들을 혼동행렬, 균형 정확도, 재현율, ROC 곡선 및 AUC와 같이 여러가지 평가 지표를 통해 분석한 결과 전반적으로 랜덤포레스트가 의사결정나무보다 더 나은 예측 성능을 보유하였다. 특히 랜덤포레스트 중 랜덤 언더 샘플링 기법은 노후도가 비교적 커서 유지관리에 주의를 기울여야 하는 C, D등급 교량에 대해 재현율 83.4%로 다른 샘플링 기법들보다 예측 성능이 더 뛰어난 것으로 나타났다. 제안된 모델은 최근 점검이 실시되지 않은 교량들의 신속한 안전등급 파악 및 효율적이고 경제적인 유지관리 계획 수립에 유용하게 활용될 수 있을 것으로 기대된다.

**발행기관명**: 대한토목학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 16. 기계학습법을 활용한 도로시설물의 시간 의존적 안전등급 예측

**저자명**: 김민선;박예원;왕길환;전종수

**주저자 소속기관**: 한양대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 머신러닝, 시간 의존적 안전등급, 도로교량, NATM 터널, 옹벽

**초록**: 시간이 경과하여 노후화된 도로시설물은 내구수명이 감소한다. 이 시설물에 적절한 유지관리가 실시되지 않으면 부재 성능이 감소하고 시설물의 효용성을 감소시킬 수 있다. 시설물의 안전성능을 유지하여 재해 및 재난을 예방함에 있어 시설물의 안전등급 예측은 유지관리 계획 수립에 효과적인 방안이다. 본 연구는 국내 도로시설물의 효과적인 유지관리를 위하여 시간 특성을 고려한 대상 시설물의 안전등급 변화를 예측할 수 있는 모델을 제시한다. 도로시설물은 교량, 터널, 옹벽을 대상으로 한다. 각 시설물의 구조형식은 가장 많이 분포하는 일반 교량과 NATM 터널, 콘크리트 옹벽을 선택하였다. 시간특성은 시설물의 사용연수를 사용하였으며 안전등급 예측 모델은 머신러닝을 기반으로 개발하였다. 이 예측 모델의 데이터베이스는 시설물의 성능평가와 정밀안전진단, 정밀안전점검 결과를 수집하여 구축되었다. XGBoost 예측 모델을 통해 시간특성을 반영한 안전등급을 혼동행렬로 검토한 결과 전 도로시설물은 100 %의 정확도로 예측할 수 있었다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2024

**주제분야**: 재료학

---

## 17. Application of Deep Learning Algorithms for Predicting Consolidation Settlement

**저자명**: 홍성호;이민호;유병수;곽태영;김성렬

**주저자 소속기관**: 서울대학교

**학술지명**: KSCE Journal of Civil Engineering

**저자키워드**: Busan Newport, Consolidation settlement, Degree of consolidation, Time–series forecasting, Machine learning, Deep learning

**초록**: Significant amount of consolidation settlement can occur in construction sites with soft clayey soil deposits. Accurate prediction is important to prevent serious issues, such as tilting and overturning of structures, as demonstrated in Busan Newport, South Korea. Observational methods, which perform regression analysis to predict settlement, are generally applied. However, the methods tend to produce inaccurate predictions when measurement records are limited. Therefore, this study applied deep learning algorithms to enhance the prediction accuracy of settlement. Three distinct models are developed based on artificial neural network, long short–term memory, and gated recurrent unit (GRU) algorithms. The models’ performance was evaluated across 277 scenarios, including 216 from the Busan Newport and 61 from an additional case study. The scenarios were classified based on the average degree of consolidation, mirroring real–world conditions. The performance of the deep learning models was compared against observational methods including the hyperbolic and Asaoka methods. According to analysis, the deep learning models demonstrated a 58 % reduction in root mean square error compared with the observational methods. Statistical analysis showed that deep learning models effectively reduced standard deviation and 90th percentile values, even with limited data. The GRU model, in particular, showed superior accuracy with the lowest statistical variation. This research highlights the potential of deep learning models for practical applications in predicting consolidation settlement.

**발행기관명**: 대한토목학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 18. WiFi 신호강도 기반의 실내 측위를 위한 머신러닝 회귀 알고리즘의 비교 분석

**저자명**: 김용현

**주저자 소속기관**: Electronics and Telecommunications Research Institute

**학술지명**: 한국측량학회지

**저자키워드**: WiFi 신호 기반 위치 결정, 실내 위치 결정, 기계학습, 회귀, 테이블 데이터 세트, 딥러닝, 앙상블 학습

**초록**: WiFi 신호강도 기반 실내 위치 결정은 추가적인 전파 신호의 송수신기를 설치하지 않아도 사용할 수 있다는 장점 덕분에 여전히 다양한 분야에서 활용되고 있다. WiFi 신호강도 기반 측위를 위해서는 사전에 WiFi 신호의 전파강도 분포도가 데이터베이스로 구축되어 있어야 하며, 이러한 데이터는 실제 테이블 형태로 저장된다. 최근 인공지능 기술이 급격히 발전했음에도 불구하고, 이러한 테이블 데이터에 딥러닝을 적용하면 학습이 불안정하고, 측위 정확도 성능은 여전히 기계학습 기반의 회귀 알고리즘이 우수한 것으로 알려져 있다. 본 논문에서는 정교하게 구축된 WiFi 신호강도 분포도를 기반으로 다양한 기계학습 기반 회귀 알고리즘을 적용하여 각 방법론의 장단점을 비교·분석하였다. Extra Tree Regression, Random Forest, Support Vector Regression, Extreme Gradient Boosting 알고리즘을 적용하였으며, 각 알고리즘의 정확도 성능과 학습 시간을 분석하였다. 실험 결과, 측위 정확도 성능은 Extra Tree Regression이 가장 우수하였으며, 학습 속도는 Extreme Gradient Boosting이 가장 빠른 것으로 나타났다. 본 연구에서 사용된 데이터는 하나의 건물 내 모든 층을 통합하여 x축 좌표, y축 좌표, z축(층)으로 구성되었으며, 대부분의 기계학습 기반 회귀 알고리즘이 평균제곱근 오차 2m 이내로 x축 좌표, y축 좌표를 예측하였을 뿐만 아니라 z축(층)은 99% 이상의 정확도로 예측하는 것을 확인하였다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 19. 군집 수에 따른 공간 제약 위계적 군집 기반 기계학습 예측 정확도 변화

**저자명**: 정민;강혜윤;구형모

**주저자 소속기관**: 서울시립대학교

**학술지명**: 대한공간정보학회지

**저자키워드**: 군집 분석, 기계학습, 공간적 이질성, 공간 기계학습

**초록**: 공간자료는 필연적으로 공간적 이질성을 내포하고 있다. 공간적 이질성의 존재는 연구 지역이 동일 모집단을 가진다는 가정을 만족하기 어렵게 하며, 이는 국지적으로 다른 기계학습 모형의 생성 필요성과 연결된다. 서울시 지하철 승하차 인원에 있어서도 공간적 이질성이 존재하며, 공간적으로 유사한 지역의 구성은 기계학습 모형의 예측 정확도 향상에 기여할 수 있다. 본 연구는 공간 제약 위계적 군집 방법으로 생성된 군집별 기계학습 모형의 추정이 기계학습 예측 정확도 향상에 미치는 영향을 탐색한다. 구체적으로 군집의 수를 변화시키며, 군집 수에 따른 예측 정확도를 각 군집별 생성된 모형과 전체 모형 간 평균 제곱근 오차를 이용하여 비교하였다. 본 연구에서 사용한 기계학습 기법은 선형회귀모형, 랜덤포레스트, 그래디언트부스팅이며, 반응변수는 지하철 승하차 인원을 사용하였다. 그 결과 대부분의 기법에서 군집의 수가 증가할수록 군집 모형의 예측 정확도가 전체 모형보다 높은 경우가 증가하는 경향을 보였다. 그러나 군집의 수가 일정 수 이상인 경우 그 경향성이 일정하게 유지되어, 예측 정확도 향상을 위해서 적절한 군집 수의 추정이 요구되는 것을 확인하였다. 본 연구는 공간 제약 위계적 군집 분석과 기계학습 기반 지하철 승하차 인원 예측 모형을 결합하여 공간적 군집 기반 모형 추정이 예측 정확도에 미치는 영향을 탐색하였다는 점에서, 공간 기계학습 발전의 기초 연구로 활용될 것으로 기대한다.

**발행기관명**: 대한공간정보학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 20. 공공 및 교통 빅데이터 기반 코로나-19 확산 예측 및 도로정책연계 방안 연구

**저자명**: 정정호;권경주;박성민;강가원;박준영

**주저자 소속기관**: 한국교통연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: Artificial Intelligence, Machine Learning, Traffic Indicator, Road Policy

**초록**: PURPOSES : This study aimed to predict the number of future COVID-19 confirmed cases more accurately using public and transportation big data and suggested priorities for introducing major policies by region. METHODS : Prediction analysis was performed using a long short-term memory (LSTM) model with excellent prediction accuracy for time-series data. Random forest (RF) classification analysis was used to derive regional priorities and major influencing factors. RESULTS : Based on the daily number of COVID-19 confirmed cases from January 26 to December 12, 2020, as well as the daily number of confirmed cases in Gyeonggi Province, which was expected to occur on December 24 and 25, depending on social distancing, the accuracy of the LSTM artificial neural network was approximately 95.8%. In addition, as a result of deriving the major influencing factors of COVID-19 through random forest classification analysis, according to the number of people, social distancing stages, and masks worn, Bucheon, Yongin, and Pyeongtaek were identified as regions expected to be at high risk in the future. CONCLUSIONS : The results of this study can help predict pandemics such as COVID-19.

**발행기관명**: 한국도로학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 21. 아스팔트 바인더의 단위 고분자에 대한 물성 평가 및 예측 연구 (Part I): 실측자료와 MD를 활용한 물성 분석

**저자명**: 윤태영

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: asphalt binder, machine learning, molecular dynamics, QSPR

**초록**: This study proposes a methodology for predicting properties such as the density of polymer composites, including asphalt binders, and evaluates its feasibility by identifying the quantitative relationship between the structure and properties of individual polymers. To this end, this study investigates the variations in molecular dynamics (MD) results with molecular structural complexity and assesses the independence and correlation of variables that influence density. In this study, MD simulations were performed on hydrocarbon-based and individual asphalt binder molecules. The effects of various temperatures, molecular conditions, and structural features on the density were analyzed. MD-related variables influencing the calculated density were evaluated and compared with experimentally measured densities. The MD-calculated densities were used as target variables in a subsequent study, in which a machine learning model was applied to perform quantitative structure–property relationship analysis.The MD-calculated densities showed a strong correlation with experimental measurements, achieving a coefficient of determination of R2 > 0.95. Potential energy exhibited a tendency to cluster into 4–6 groups depending on the molecular structure. In addition, increasing molecular weight and decreasing temperature led to higher density and viscosity. Torsional energy and other individual energy components were identified as significant factors influencing both potential energy and density. This study provided foundational data for the property prediction of asphalt binders by quantitatively analyzing the relationship between the molecular structure and properties using MD simulations. Key features that could be used in the construction of polymer structure databases and AI-based material design were also proposed. In particular, the integration of MD-based simulation and machine learning was confirmed to be a practical alternative for predicting the properties of complex polymer composite systems.

**발행기관명**: 한국도로학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 22. 아스팔트 바인더의 단위 고분자에 대한 물성 평가 및 예측 연구 (Part II): 기계학습을 활용한 물성 예측

**저자명**: 윤태영

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: asphalt binder, machine learning, molecular dynamics, QSPR

**초록**: This study proposes a methodology for predicting the physical properties such as the density of polymer composites, including asphalt binders, and evaluates its feasibility by identifying the quantitative relationship between the structure and properties of individual polymers. To this end, features are constructed using molecular dynamics (MD) simulation results and descriptor calculation tools. This study investigates the changes in the calculated density depending on the characteristics of the training dataset and analyzes the feature characteristics across datasets to identify key features. In this study, 2,415 hydrocarbon and binder-derived polymer molecules were analyzed using MD simulations and 2,790 chemical descriptors generated using alvaDesc. The features were pre-processed using correlation filtering, PCA, and recursive feature elimination. The XGBoost models were trained using k-fold cross-validation and Optuna optimization. SHAP analysis was used to interpret feature contributions. The variables influencing the density prediction differed between the hydrocarbon and binder groups. However, the hydrogen atom count (H), van der Waals energy, and descriptors such as SpMAD_EA_LboR consistently had a strong impact. The trained models achieved high accuracy (R² > 0.99) across different datasets, and the SHAP results revealed that the edge adjacency, topological, and 3D geometrical descriptors were critical. In terms of predictive accuracy and interpretability, the integrated MDQSPR framework demonstrated high reliability for estimating the properties of individual binder polymers. This approach contributed to a molecular-level understanding and facilitated the development of ecofriendly and efficient modifiers for asphalt binders.

**발행기관명**: 한국도로학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 23. 국가기본도와 항공정사영상을 활용한 객체 탐지 데이터셋 구축 연구

**저자명**: 함형래;김미선;이지영

**주저자 소속기관**: EGIS

**학술지명**: 한국측량학회지

**저자키워드**: 인공지능, 딥러닝, 객체 탐지, 학습 데이터, 항공정사영상

**초록**: 인공지능 산업이 발달함과 동시에 많은 딥러닝 모델들이 오픈 소스로 공개되면서 누구나 쉽게 딥러닝을 활용하는 환경이 마련되었다. 그러나 딥러닝 모델을 사용하기에 충분한 학습 데이터를 구축하기 위해서는 시간과 비용이 많이 소모되어 활용에 제한이 있다. 특히 항공정사영상에서 객체를 탐지하는 연구들은 대부분 수작업으로 학습 데이터를 구축하고 있는 실정이다. 수작업으로 학습 데이터를 구축하는 것은 시간과 비용이 많이 소모될 뿐만 아니라, 작업자의 실수, 착오에 의한 오류, 작업자의 주관적 판단에 따라 데이터가 상이하게 구축된다는 단점이 있다. 본 연구는 이러한 문제를 해결하기 위해 기구축된 데이터를 활용하여 학습 데이터를 제작하는 방법에 대하여 제시한다. 기구축 데이터인 국가기본도와 국토지리정보원에서 제공하는 25cm급 항공정사영상을 활용하여 객체 탐지 학습 데이터 제작 방안을 도출하고, 제작된 객체 탐지 학습 데이터의 효용성을 확인하기 위해 YOLOv5 모델을 활용하여 항공정사영상의 객체 탐지 학습을 진행하였다.

**발행기관명**: 한국측량학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 24. 시공 중 흙막이 벽체 수평변위 예측을 위한 앙상블 모델 개발

**저자명**: 서승환;정문경

**주저자 소속기관**: 한국건설기술연구원 지반연구본부

**학술지명**: 한국지반공학회논문집

**저자키워드**: Boosting, Ensemble, Excavation, Machine learning, Retaining wall

**초록**: 도심지 지하굴착 공사가 대형화되면서 공사 중 안전사고에 대한 위험요인이 더욱 증가하고 있다. 이에 따라 공사현장의 위험요소를 모니터링하고 사전에 예측할 수 있는 기술이 필요하다. 굴착으로 인한 흙막이 벽체의 변형을 예측하는 방법에는 크게 경험식과 수치해석 두 가지 방법으로 분류할 수 있으며, 최근에는 인공지능 기술의 발달과 함께 머신러닝 기법을 활용한 예측 모델이 한 가지 방법으로 자리 잡고 있다. 본 연구에서는 예측력과 효율성이 우수한 부스팅 계열 알고리즘 및 앙상블 모델을 이용하여 시공 중 흙막이 벽체 변형을 예측하는 모델을 구축하였다. 지하흙막이 공사의 설계-시공-유지관리 과정에서 도출되는 자료들을 복합적으로 활용하여 데이터베이스를 구축하고, 이 자료를 토대로 학습모델을 만들고 성능을 평가하였다. 모델 성능 평가 결과, 높은 정확도로 흙막이 벽체 변형을 예측할 수 있었으며, 지반계측 자료를 학습에 활용함으로써 실제 시공과정의 특성이 반영된 예측결과를 제시할 수 있었다. 본 연구에서 구축한 예측 모델을 활용하여 시공 중 흙막이 벽체의 안정성 평가 및 모니터링에 활용할 수 있을 것으로 기대된다.

**발행기관명**: 한국지반공학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 25. 기계학습을 활용한 콘크리트의 강도 예측 모델 검토

**저자명**: 이빛나;유재석

**주저자 소속기관**: 한국건설기술연구원 인프라구조연구실

**학술지명**: 한국도로학회논문집

**저자키워드**: machine learning, compressive strength, concrete, regression analysis

**초록**: machine learning models based on the same data. METHODS : Approximately 478 pieces of concrete compressive strength data were obtained to compare the performance of the machine learning models. In addition, five machine learning models were trained based on the obtained data. The performance of the learned model was compared using three performance indicators. Finally, the performance of the model trained using additional data was reviewed. RESULTS : As a result of comparing the performance of machine learning models, the XGB(eXtra Gradient Boost) model showed the best performance. In addition, as a result of the verification based on additional data, highly reliable results can be obtained if the XGB model is used to predict the compressive strength of concrete. CONCLUSIONS : If a concrete strength prediction model is derived based on a machine learning model, a highly reliable model can be derived.

**발행기관명**: 한국도로학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 26. GPR 영상 지하시설물 탐지를 위한 티처블 머신 활용

**저자명**: 장수민;이병길

**주저자 소속기관**: 경기대학교(Kyonggi University)

**학술지명**: 한국측량학회지

**저자키워드**: GPR, 티처블 머신, 기계 학습, 지하시설물

**초록**: 지하시설물의 탐지에는 GPR (Ground Penetrating Radar) 영상을 이용한 방법이 가장 많이 사용되고 있다. GPR 영상해석은 크게 경계선 검출에 의한 방법과 머신러닝을 활용한 방법으로 나눌 수 있으며, 특히 머신러닝을 이용한 방법에서는 쌍곡선 모양을 형성하는 영상의 특성을 적절히 이용하는 것이 필요하다. 한편 구글에서는 누구나 쉽게 머신러닝 모델을 활용할 수 있도록 티처블 머신이라는 웹 기반 도구를 소개하였다. 본 연구에서는 티처블 머신과같이 간단한 머신러닝 도구를 이용하여 GPR 영상에 포함된 지하시설물을 효과적으로 탐지할 수 있는지와 그 정확도 개선 방안을 제시하고자 하였다. 도로에 매설된 지하시설물의 위치에 따라 GPR 영상에 완전한 쌍곡선과 그렇지 은 쌍곡선이 혼재하게 된다. 본 연구에서는 다양한 쌍곡선 형상을 추출하고, 학습하여 테스트한 결과 여러 형태의 쌍곡선을 동시에 학습하는 것이 매치율 향상에 도움이 되는 것으로 나타났다. 이와 같은 방법으로 트레이닝하면 GPR 영상의 해석에 티처블 머신을 이용할 수 있음을 확인할 수 있었다.

**발행기관명**: 한국측량학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 27. 머신러닝 기반의 강우-유출모형(M-RAT) 매개변수 최적화 기법

**저자명**: 유재은;정세진;김병식;정승권

**주저자 소속기관**: (재)국제도시물정보과학연구원

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 머신러닝, 강우-유출모형, M-RAT, 매개변수, 최적화

**초록**: 최근 기후변화, 기후변동으로 인해 저수지 및 소하천의 유량이 감소하는 추세이다. 이와 같은 하천 유량 감소는 건천화 현상을 발생시켜 하천의 생태계 파괴, 자정기능 상실, 친수 기능 상실 등 각종 부작용의 원인이 될 수 있다. 가뭄으로 인해 하천 및 저수지에 저유량이 유지되는 유역은 유출량의 특성 파악이 중요한 요소로 작용한다. 강우-유출 모형을 활용한 유출량 모의를 통해 하천의 유량을 파악할 수 있으며, 그 중 M-RAT (Monthly Runoff Assessment Tool) 모형은 일반적이고 간단한 월 물수지 방정식을 기반으로 유출 분석을 통해 월 유출량을 추정한다. M-RAT 모형을 활용한 유출량 모의 시 하천 유역의 수문 및 기상자료를 사용하여 모형의 매개변수를 보정하는 과정을 통해 모의의 정확도를 높일 수 있다. 본 연구는 머신러닝 기법을 활용하여 13개 유역을 대상으로 M-RAT 모형의 매개변수를 검보정 및 최적화하고, 획득한 매개변수를 활용하여 M-RAT 모형을 통한 월 유출량을 모의하였다. 모형 성능 검증을 위해 미호강, 합천댐, 홍천강 3개 유역에 적용하여 정확성을 검토한 결과, 머신러닝 기반의 매개변수 최적화 기법을 활용했을 때 기존에 수행된 기법에 비해 개선된 결과를 확인할 수 있었다.

**발행기관명**: 한국수자원학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 28. 하수처리장 유출수 수질 예측을  위한 최적 파이프라인 설계:  블록 시계열 교차 검증 기반 베이지안 최적화

**저자명**: 박형주;심규대;김영모;이상철

**주저자 소속기관**: 한양대학교 건설환경공학과학과/한양대학교 기후변화-재난재해 대응형 디지털 건설공학 인재양성팀 (BK21 FOUR)

**학술지명**: 상하수도학회지

**저자키워드**: 교차  검증,  머신러닝,  모델  최적화,  과적합,  하수처리장

**초록**: 하수처리장  유출수의  수질  예측은  수질  사고의  사전  대응  및  처리장의  안정적인  운영을  위해  필수적인  요소이다.  최근  머신러닝을  활용한  예측  모델링에서  예측  성능  향상과  과적합  방지를  위해  다양한  교차  검증법과  하이퍼파라미터  최적화  기법이  활용되고  있으나, 하수처리장  데이터는  시간적  의존성과  급격한  변동성이  내재되어  있어  과적합에  취약하고  안정적인  모델  구축에  어려움이  따른다.  본  연구에서는  이러한  데이터  특성을  효과적으로  반영할  수  있는  최적의  모델링  파이프라인을  구축하고자  하였으며,  XGBoost  모델을  기반으로  유출수  내  총질소  농도를  예측하였다.  예측  성능  평가  지표로는  평균  제곱근  오차(Root  Mean  Square  Error,  RMSE), 결정계수(coefficient  of  determination,  R 2 ),  RMSE  오차  개선율(the  rate  of  improvement  on  RMSE,  RIR RMSE )  그리고  계산  시간을 사용하였다.  기본적인  Hold-out  방식의  성능을  기준으로  K-fold,  시계열  교차  검증(Time  Series  Cross  Validation,  TSCV),  블록 시계열  교차  검증(Blocked  Time  Series  Cross  Validation,  BTSCV)  기법의  예측  성능을  분석한  결과,  BTSCV는  인접한  데이터만을  고려하는  방식으로  시간적  의존성과  급변  특성을  효과적으로  반영하여  가장  높은  RIR(36.37%)을  기록하였다.  또한,  하이퍼파라미터최적화(그리드  서치와  베이지안  최적화)  기법과의  다양한  교차  검증법의  조합을  통해  모델  성능과  과적합  방지  효과를  분석한  결과,  BTSCV와  베이지안  최적화의  결합은  짧은  계산  시간(364.64초)과  함께  가장  높은  RIR(64.93%)을  보였으며,  훈련  및  평가  데이터  간  성능  차이도  최소화되어  일반화된  예측  모델로서의  효과성이  입증되었다.  따라서  본  연구는  하수처리장  시계열  데이터의  특성에 적합한  BTSCV와  베이지안  최적화  기법을  결합한  모델링  파이프라인  전략을  제안하며,  향후  실시간  수질  모니터링  및  하수처리장  운영  효율성  제고에  기여할  수  있을  것으로  기대된다.

**발행기관명**: 대한상하수도학회

**발행연도**: 2025

**주제분야**: 상하수도공학

---

## 29. 담수호의 위성영상 기반 Multi-model Ensemble을 통한 TOC 예측

**저자명**: 김진욱;장원진;김진휘;이용구;신재기;박용은;김성준

**주저자 소속기관**: 건국대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 총유기탄소, 위성영상, 머신러닝, Stacking 모형, HSIC-Lasso

**초록**: 본 연구는 위성 원격탐사와 머신러닝 기반 Multi-Ensemble 모델의 일종인 Stacking 모형을 결합하여 남양호에서 총유기탄소(Total Organic Carbon, TOC)를 간접적으로 추정하는 것을 목표로 하였다. Sentinel-2A/B 위성 데이터를 활용하여 연구 지역의 반사도 데이터를 구축하였으며, HSIC-Lasso 모델을 통해 TOC와 높은 상관성을 가지는 10개의 주요 입력변수(B4/B3, B4/B5, B2/B3, B8/B7, B4/B2, B1/B3, B1/B5, B8/B6, B5/B2, B2/B5)를 도출하였다. TOC를 예측하기 위해 Support Vector Regression (SVR), Random Forest Regression (RFR), eXtreme Gradient Boosting (XGB), Multi-Layer Perceptron (MLP)을 베이스모델로 사용하고, Partial Least Squares (PLS) 및 Ridge Regression (RID)를 포함한 6개의 메타모델을 결합한 Stacking Ensemble 모델을 개발하였다. Stacking 모델은 훈련 데이터와 테스트 데이터에서 각각 R² 값 0.963과 0.886, MAE 값 0.697 mg/L, RMSE 값 1.556 mg/L의 값을 보였으며, 단일 머신러닝 모델의 예측 성능보다 개선됨을 보여주었다. 본 연구 결과는 위성 데이터와 머신러닝 모델을 통합하여 TOC를 비용 효율적이고 지속 가능한 방식으로 모니터링할 수 있는 기반을 제시하며, 추후 장기간의 TOC 데이터 축적을 통해 수질 관리 및 정책 개발을 위한 실용적인 도구로 활용될 수 있을 것으로 기대된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 30. 머신러닝 기반 부식깊이 예측 모델을 적용한  상수도관망의 누적피해도 분석

**저자명**: 권혁재

**주저자 소속기관**: 청주대학교 토목공학과

**학술지명**: 상하수도학회지

**저자키워드**: 누적피해도,  Monte  Carlo  Simulation,  상수도관망,  머신러닝,  부식

**초록**: 본  연구에서는  Romanoff(1957)의  실측  데이터를  사용하여  머신러닝  기반  상수도관의  부식  깊이를  예측하였다.  이를  실제  상수도관망에 적용하여  누적피해도를  분석하였다.  예측한  부식깊이를  사용하여  누적피해도를  분석하였으며  MCS(Monte  Carlo  Simulation)를  적용한 누적피해도와  비교  분석하였다.  부식깊이  예측모델에  따른  부식깊이를  분석한  결과  MLP-ReLU  모델이  가장  부식속도가  가장  빠르며 MLP-sigmoid가  가장  부식속도가  느렸다.  천안시  신방동과  성환읍  상수도관망에  MCS를  적용한  누적피해도  분석법과  머신러닝을 적용한  누적피해도를  비교  분석하였다.  신방동에서는  두  분석법  모두  2번  상수도관이  먼저  사용  한계에  도달하였으며  성환읍에서는  4번  상수도관이  가장  먼저  사용  한계에  도달하였다.  사용  한계에  가장  먼저  도달한  상수도관은  다른  상수도관보다  사용  년수가  오래되었거나 수압이  높은  것으로  확인되었다.  MCS를  적용한  누적피해도  분석  결과  신방동의  경우  45년  만에  사용  한계를  초과한  반면  성환읍의 경우  47년  만에  사용  한계를  초과했다.

**발행기관명**: 대한상하수도학회

**발행연도**: 2025

**주제분야**: 상하수도공학

---

## 31. 도로포장 재료 개발을 위한 소재정보학과 분자동역학 활용연구 방법 고찰(Ⅱ) : 인공지능 기술을 적용한 재료·소재 연구 동향

**저자명**: 주현진;윤태영;심승보

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: machine learning, material optimization, molecular dynamics, artificial intelligence, road-pavement materials

**초록**: This paper explores a convergent approach that combines advanced informatics and computational science to develop road-paving materials. It also analyzes research trends that apply artificial-intelligence technologies to propose research directions for developing new materials and optimizing them for road pavements. This paper reviews various research trends in material design and development, including studies on materials and substances, quantitative structure–activity/property relationship (QSAR/QSPR) research, molecular data, and descriptors, and their applications in the fields of biomedicine, composite materials, and road-construction materials. Data representation is crucial for applying deep learning to construction-material data. Moreover, selecting significant variables for training is important, and the importance of these variables can be evaluated using Pearson’s correlation coefficients or ensemble techniques. In selecting training data and applying appropriate prediction models, the author intends to conduct future research on property prediction and apply string-based representations and generative adversarial networks (GANs). The convergence of artificial intelligence and computational science has enabled transformative changes in the field of material development, contributing significantly to enhancing the performance of road-paving materials. The future impacts of discovering new materials and optimizing research outcomes are highly anticipated.

**발행기관명**: 한국도로학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 32. 다양한 기계 학습 알고리즘을 활용한 교량 바닥판 상태등급 및 결함도 지수 예측 모델 개발

**저자명**: 이재현;김우혁;민근형;김우석

**주저자 소속기관**: 충남대학교 토목공학과

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 기계 학습, 예측 모델, 열화, 상태 등급, 결함도 지수

**초록**: 본 연구는 Random Forest, XGBoost, k-NN, SVM, Neural Network, LSTM, GRU와 같은 다양한 기계 학습 알고리즘을 활용하여 교량 바닥판의 효율적인 유지관리를 위한 예측 모델을 개발하는 것을 목표로 한다. 본 예측 모델들은 바닥판의 결함도 지수와 상태등급을 예측하는 데 사용되었으며, LSTM, Random Forest, XGBoost는 결함도 지수 예측에서 우수한 성능을 보였고, XGBoost, GRU, LSTM은 상태등급 예측에서 뛰어난 결과를 나타냈다. 모델의 성능 평가는 MSE, RMSE, MAE 등 다양한 지표를 사용하였으며, 과적합 여부를 평가하기 위해 교차 검증을 실시하였다. 연구 결과, 제안된 모델들은 교량 바닥판 유지관리를 보다 정확하고 효율적으로 수행할 수 있도록 기여하며, 예방적 유지보수를 가능하게 하고 유지관리 비용을 최적화하는 데 중요한 역할을 할 수 있음을 확인하였다. 향후 연구에서는 환경적 요인과 같은 추가 변수를 포함하여 예측 성능과 모델의 실용성을 더욱 향상시키는 방향으로 연구를 확장할 예정이다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2024

**주제분야**: 재료학

---

## 33. 공간데이터 기반 기계학습 모형의 예측 정확도 향상을 위한 연접성 제약을 반영한 공간 군집의 활용

**저자명**: 강혜윤;정민;구형모

**주저자 소속기관**: 서울시립대학

**학술지명**: 한국측량학회지

**저자키워드**: 군집분석, 공간 군집분석, 기계학습, 공간적 자기상관

**초록**: 기계학습에서 예측 정확도 향상은 중요하며, 이를 위해 다양한 방법이 연구되고 있다. 그 중 군집 기법은 데이터의 유사성을 바탕으로 분할하거나 병합하는 것으로, 이를 통해 생성된 각 군집에 대해 기계학습 모형을 구축함으로써 예측 정확도를 높일 수 있다. 일반적으로 군집분석은 속성적 유사성만을 반영한다. 그러나 공간데이터는 공간적 자기상관과 같은 특수성을 가지고 있어 이를 고려할 시 기계학습의 예측 정확도를 향상시킬 수 있으며, 공간적 유사성을 고려한 군집모형의 구축도 공간데이터의 특수성을 반영할 수 있는 방안이다. 따라서 본 연구는 공간적 유사성을 고려한 군집 기법이 기계학습 예측 정확도에 미치는 영향을 탐색한다. 구체적으로 속성적 유사성만을 고려한 군집기법과 공간적 유사성과 속성적 유사성 모두를 고려한 군집 기법으로 생성된 기계학습 모형의 예측 정확도를 대중교통 일평균 승하차 인원 예측 모형을 사례로 비교하였다. 본 연구에서 사용한 기계학습 기법은 선형회귀모형, 랜덤포레스트, 그래디언트부스팅이며, 반응변수는 대중교통 일평균 승하차 인원, 그리고 입력변수는 토지특성, 인구특성, 시설특성을 설명하는 11개 변수를 사용하였다. 예측 결과 모든 모형에서 공간적 유사성을 고려한 군집 기법이 그렇지 않은 군집 기법보다 통계적으로 유의미하게 높은 예측 정확도를 보였다. 본 연구는 공간데이터를 기계학습에 적용할 때 공간적 유사성을 고려하는 것이 예측 정확도를 향상시킬 수 있음을 보여주었다는 점에서 의의를 가진다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 34. 농업용 저수지 CCTV 영상자료 기반 수위 인식 모델 적용성 검토

**저자명**: 권순호;하창용;이승엽

**주저자 소속기관**: 고려대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 기계학습, 수위 인식, 저수지, CCTV, 이미지 처리

**초록**: 농업용 저수지는 농업용수 공급에 있어서 매우 중요한 생산기반시설로, 우리나라 농업용수의 60% 정도를 공급하고 있다. 다만, 여러 문제로 인해 농업용수의 효율적인 공급에 어려움이 발생하고 있으며, 효과적인 공급 및 관리 체계 구현을 위한 정확한 실시간 저수위 혹은 저수량 추정이 필요하다. 본 연구에서는 영상정보를 활용한 딥러닝 기반 농업용 저수지 수위 인식 모델을 제안하였다. 개발한 모델은 (1) CCTV 영상정보 자료 수집 및 분석, (2) U-Net 이미지 분할 방법을 통한 입력 자료 생성, 그리고 (3) CNN과 ResNet 모델을 통한 수위 인식 세 단계로 구성된다. 모델은 두 농업용 저수지(G저수지와 M저수지)의 영상자료와 저수위 시계열자료를 활용하여 구현하였다. 적용 결과 이미지 분할 모델의 성능은 매우 우수한 것으로 나타났으며, 수위 인식 모델의 경우 수위 분류 계급구간에 따라 성능이 상이한 것으로 나타났다. 특히 영상자료의 픽셀 변동이 클수록 정확도 80% 이상이 확보 가능한 것으로 확인되었으나, 그렇지 않은 경우, 정확도가 50% 수준인 것으로 나타났다. 본 연구에서 개발한 모델은 향후 이미지 자료가 추가로 확보될 경우, 그 활용도 및 정확도가 더 높아질 것으로 기대한다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 35. 머신러닝을 활용한 계획단계 도로공사 공사비용 추정 모델 개발

**저자명**: 김제원;김준수

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: Road construction, planning stage, construction cost estimation, database, machine learning

**초록**: PURPOSES : Construction cost estimates are important information for business feasibility analysis in the planning stage of road construction projects. The quality of current construction cost estimates are highly dependent on the expert's personal experience and skills to estimate the arithmetic average construction cost based on past cases, which makes construction cost estimates subjective and unreliable. An objective approach in construction cost estimation shall be developed with the use of machine learning. In this study, past cases of road projects were analyzed and a machine learning model was developed to produce a more accurate and time-efficient construction cost estimate in teh planning stage. METHODS : After conducting case analysis of 100 road construction, a database was constructed including the road construction's details, drawings, and completion reports. To improve the construction cost estimation, Mallow's Cp. BIC, Adjusted R methodology was applied to find the optimal variables. Consequently, a plannigs-stage road construction cost estimation model was developed by applying multiple regression analysis, regression tree, case-based inference model, and artificial neural network (ANN, DNN). RESULTS : The construction cost estimation model showed excellent prediction performance despite an insufficient amount of learning data. Ten cases were randomly selected from the data base and each developed machine learning model was applied to the selected cases to calculate for the error rate, which should be less than 30% to be considered as acceptable according to American Estimating Association. As a result of the analysis, the error rates of all developed machine learning models were found to be acceptable with values rangine from 17.3% to 26.0%. Among the developed models, the ANN model yielded the least error rate. CONCLUSIONS : The results of this study can help raise awareness of the importance of building a systematic database in the construction industry, which is disadvantageous in machine learning and artificial intelligence development. In addition, it is believed that it can provide basic data for research to determine the feasibility of construction projects that require a large budget, such as road projects.

**발행기관명**: 한국도로학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 36. 실용 가능한 배합의 28일 재령 콘크리트 압축강도 예측 기계학습 모델 개발

**저자명**: 손재호

**주저자 소속기관**: 홍익대학교

**학술지명**: 한국도로학회논문집

**저자키워드**: Compressive Strength, Concrete, Machine Learning, Gradient Boosting, AdaBoost, Random Forest

**초록**: PURPOSES : To enhance the accuracy of predicting the compressive strength of practical concrete mixtures, this study aimed to develop a machine learning model by utilizing the most commonly employed curing age, specifically, the 28-day curing period. The training dataset consisted of concrete mixture sample data at this curing age, along with samples subjected to a total load not exceeding 2,350 kg. The objective was to train a machine learning model to create a more practical predictive model suitable for real-world applications. METHODS : Three machine learning models—random forest, gradient boosting, and AdaBoost—were selected. Subsequently, the prepared dataset was used to train the selected models. Model 1 was trained using concrete sample data from the 28th curing day, followed by a comprehensive analysis of the results. For Model 2, training was conducted using data from the 28th day of curing, focusing specifically on instances where the total load was 2,350 kg or less. The results were systematically analyzed to determine the most suitable machine learning model for predicting the compressive strength of concrete. RESULTS : The machine learning model trained on concrete sample data from the 28th day of curing with a total weight of 2,350 kg or less exhibited higher accuracy than the model trained on weight-unrestricted data from the 28th day of curing. The models were evaluated in terms of accuracy, with the gradient boosting, AdaBoost, and random forest models demonstrating high accuracy, in that order. CONCLUSIONS : Machine learning models trained using concrete mix data based on practical and real-world scenarios demonstrated a higher accuracy than models trained on impractical concrete mix data. This case illustrates the significance of not only the quantity but also the quality of the data during the machine learning training process. Excluding outliers from the data appears to result in better accuracy for machine learning models. This underscores the importance of using high-quality and practical mixed concrete data for reliable and accurate model training.

**발행기관명**: 한국도로학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 37. 공간 데이터와 기계학습 기법의 결합을 위한 공간적 입력변수 유용성 탐색

**저자명**: 구형모;유무상;서현일;박성재

**주저자 소속기관**: 서울시립대학교

**학술지명**: 한국측량학회지

**저자키워드**: 공간적 변수, 기계학습, 공간 데이터 분석, 공간적 자기상관

**초록**: 공간 데이터는 공간적 자기상관과 같은 고유한 특성을 가지며, 기계학습을 공간 데이터에 적용 시 공간적 자기상관을 고려하지 않으면 기계학습의 예측 정확도 하락과 같은 부정적 결과를 일으킨다. 본 연구는 기계학습에 공간적 특성을 명시적으로 포함하는 방법인 공간적 변수의 투입이 기계학습의 예측 정확도 향상에 미치는 영향을 탐색한다. 나아가 공간적 변수 유형과 기계학습 모형 간의 유용성 차이를 비교하고자 한다. 사용된 공간적 변수의 유형은 공간좌표, 공간 지체 그리고 모런 고유벡터 공간 필터이며, 기계학습 기법은 선형회귀모형, 일반화가법모형, 랜덤포레스트, 서포트벡터머신이다. 강한 양의 공간적 자기상관이 있는 서울시 아파트 매매가격을 반응변수로 사용하였고, 속성적 변수와 공간적 변수를 결합하여 예측모형을 설계하였다. 본 연구의 결과 훈련데이터와 검증데이터 모두에서 선형회귀모형, 일반화가법모형, 그리고 랜덤포레스트는 공간 지체, 서포트벡터머신은 공간 좌표가 가장 높은 예측 정확도 상승을 보였다. 모형 간 비교에서는 랜덤포레스트와 공간 지체를 결합한 모형이 가장 높은 정확도를 보였으며, 일반적으로 공간적 변수의 활용이 기계학습 모형의 예측 정확도 향상에 기여함을 확인하였다. 본 연구는 다양한 형태의 공간적 변수의 구성 방법을 정리·제시하고, 기계학습 모형별 변수 선택 방법과 결합하여 공간적 변수의 활용도를 높였다는 점에서 공간 기계학습 발전의 기초 연구로 활용할 수 있을 것으로 기대한다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 38. 고속국도 터널구간 미세먼지 농도 추정 모형 개발

**저자명**: 정도영

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: particulate matter(PM), expressway tunnel sections, machine learning, random forest

**초록**: PURPOSES : In this study, a model was developed to estimate the concentrations of particulate matter (PM2.5 and PM10) in expressway tunnel sections. METHODS : A statistical model was constructed by collecting data on particulate matter (PM2.5 and PM10), weather, environment, and traffic volume in the tunnel section. The model was developed after accurately analyzing the factors influencing the PM concentration. RESULTS : A machine learning-based PM concentration estimation model was developed. Three models, namely linear regression, convolutional neural network, and random forest models, were compared, and the random forest model was proposed as the best model. CONCLUSIONS : The evaluation revealed that the random forest model displayed the least error in the concentration estimation model for (PM2.5 and PM10) in all tunnel section cases. In addition, a practical application plan for the model developed in this study is proposed.

**발행기관명**: 한국도로학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 39. XGBoost 알고리즘 기반 철근콘크리트 기둥의 Backbone 곡선 파라미터 예측

**저자명**: 윤준영;조진우;조은선;한상환

**주저자 소속기관**: 한양대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 철근콘크리트 기둥, 백본커브, 기계학습, 정확도, 모델링 파라미터

**초록**: 철근 콘크리트 골조의 내진 성능을 평가할 때 기둥의 거동이 시스템 성능에 상당한 영향을 미치기 때문에 기둥에 대한 정확한 수치 모델을 사용하는 것이 중요하다. 대부분의 이전 연구에서 기둥 모델의 매개변수는 경험식을 사용하여 결정되었다. 그러나 회귀 분석에서 개발된 경험식을 사용하여 실제 기둥의 복잡하고 비선형적인 특성을 완전히 포착하는 것은 어렵습니다. 본 연구의 목적은 RC 기둥에 대한 이상적인 백본 곡선을 구성하기 위한 머신 러닝(ML) 모델을 개발하는 것이다. 이를 위해 이전 연구에서 반복 하중을 받는 직사각형 RC 기둥에 대한 테스트 데이터를 수집했다. 백본 곡선을 구성하기 위해 세 가지 손상 상태를 정의했다. 제안된 ML 모델의 정확성이 검증하였디. 수집된 기둥의 측정된 백본 곡선이 제안된 ML 모델에서 얻은 매개변수 값을 사용하여 정확하게 예측되었음을 보여주었다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2025

**주제분야**: 재료학

---

## 40. Seismic Acceleration Estimation Method at Arbitrary Position Using Observations and Machine Learning

**저자명**: 이경석;안진희;박해용;서영덕;김석찬

**주저자 소속기관**: 부산대학교

**학술지명**: KSCE Journal of Civil Engineering

**저자키워드**: Machine-learning regression, Seismic acceleration prediction, Seismic measurement station, Supervised learning

**초록**: This study proposes a method of estimating the measurement data of nearby seismic stations by training an artificial neural network (ANN) through machine learning to understand the seismic acceleration time history at an arbitrary location where seismic acceleration time history is unknown. The ANN is trained using the observation data of 6 earthquakes at 10 ground seismic stations in Korea and 12 earthquakes at 212 underground seismic stations from the Korea Meteorological Administration. The location of the seismic station is assumed to be arbitrary in the untrained observation data to verify the validity of the trained ANN, and the measured and estimated data are compared. It is confirmed that the estimation accuracy of the ANN trained with the observation data of the underground seismic station is higher than that of the ANN trained with the observation data of the ground seismic station. The accuracy of the seismic acceleration estimation method proposed in this study is improved according to the level of learning data. It can also be applied as seismic acceleration to evaluate seismic damage or behavior of structures or facilities, even in places without seismic acceleration.

**발행기관명**: 대한토목학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 41. LSTM - MLP 인공신경망 앙상블을 이용한 장기 강우유출모의

**저자명**: 안성욱;강동호;성장현;김병식

**주저자 소속기관**: Department of Urban Environmental Disaster Management, Kangwon National University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: LSTM, MLP, 장기유출, 기계학습, 인공신경망

**초록**: 수자원 관리를 위해 주로 사용되는 물리 모형은 입력자료의 구축과 구동이 어렵고 사용자의 주관적 견해가 개입될 수 있다. 최근 수자원 분야에서 이러한 문제점을 보완하기 위해 기계학습과 같은 자료기반 모델을 이용한 연구가 활발히 진행되고 있다. 본 연구에서는 관측자료만을 이용하여 강원도 삼척시 오십천 유역의 장기강우유출모의를 수행했다. 이를 위해 기상자료로 3개의 입력자료군(기상관측요소, 일 강수량 및 잠재증발산량, 일 강수량 – 잠재증발산량)을 구성하고 LSTM (Long Short-term Memory)인공신경망 모델에 각각 학습시킨 결과를 비교 및 분석했다. 그 결과 기상관측요소만을 이용한 LSTM-Model 1의 성능이 가장 높았으며, 여기에 MLP 인공신경망을 더한 6개의 LSTM-MLP 앙상블 모델을 구축하여 오십천 유역의 장기유출을 모의했다. LSTM 모델과 LSTM-MLP 모형을 비교한 결과 두 모델 모두 대체적으로 비슷한 결과를 보였지만 LSTM 모델에 비해 LSTM-MLP의 MAE, MSE, RMSE가 감소했고 특히 저유량 부분이 개선되었다. LSTM-MLP의 결과에서 저유량 부분의 개선을 보임에 따라 향후 LSTM-MLP 모델 이외에 CNN등 다양한 앙상블 모형을 이용해 물리적 모델 구축 및 구동 시간이 오래 걸리는 대유역과 입력 자료가 부족한 미계측 유역의 유황곡선 작성 등에 활용성이 높을 것으로 판단된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 42. 지상 우량계 자료를 활용한 격자 형태의 강우 시나리오 생성 방법 개발: 서울특별시 내 대류성 강우를 중심으로

**저자명**: 차호영;전창현;백종진;김현준

**주저자 소속기관**: 고려대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 대류성 강우, 강우 공간 보간, 레이더 합성장, 머신러닝, 독립 호우사상

**초록**: 본 연구에서는 2019년부터 2022년까지 서울특별시 내 위치한 우량계와 레이더를 통해 관측된 강우 자료를 활용하여 대류성 강우의 특징을 반영한 격자 형태의 강우 시나리오를 제작할 수 있는 머신러닝 모형을 제안하였다. 우량계에서 관측한 강우 자료는 특정 조건(IETD: 2시간, 절단값: 0.5 mm)에 따라 독립 호우사상으로 분리하였다. 독립 호우사상은 대류성 강우가 발생한 시기를 구분하기 위해 활용된다. 레이더 합성장은 가우시안 필터링을 활용하여 잡음을 제거한 이후, 우량계 중심으로 가까운 36개의 격자 자료를 대류성 강우의 공간적 크기로 정의하여 구분하였다. 이후, 머신러닝 구축을 위해 활용된 학습 자료는 입력자료로 우량계에서 관측된 강우 자료, 우량계의 위도와 경도, 우량계와 레이더 중심과의 거리 차이, 시간 관련 변수를, 출력자료로 우량계 주변의 36개 강우 격자 자료로 구성하였다. 구축된 자료는 회귀모형의 머신러닝에 적용하였으며, 활용된 머신러닝은 그래디언트 부스팅, 랜덤 포레스트, 엑스트라 트리, 다층 퍼셉트론이다. 분석 결과, 4개의 머신러닝은 레이더 합성장에서 관측된 강우강도와 서로 비교하면 평가 지표인 피어슨 상관계수가 전반적으로 0.7 이상이지만, 다층 퍼셉트론은 다른 모델에 비해 MAE와 RMSE가 작다는 점을 통해 준수한 성능을 가지고 있었다. 강우강도와의 유사성을 비교하면, 제작된 강우 시나리오는 우량계와 레이더보다 과소 추정하는 결과를 보여주었다. 마지막으로 강우 시나리오와 레이더 자료와의 공간분포를 비교한 결과를 보면, 정규화된 상관계수는 0.2에서 0.4로 산출되었다. 본 연구에서 제안한 방법론은 도시에 특화된 소규모 유역의 대류성 강우에 대한 강우 자료의 공간 보간 방법으로 활용 가능할 것으로 판단된다. 또한, 본 방법론은 우량계 중심의 정보만 있다면, 우량계 주변 격자 형태의 시나리오를 추정할 수 있다.

**발행기관명**: 한국수자원학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 43. 기계학습과 최대 커버링 입지 모형을 이용한 광주시 스마트 공공복합편의시설 최적 입지선정

**저자명**: 조성호;구형모

**주저자 소속기관**: 주식회사 선도소프트

**학술지명**: 한국측량학회지

**저자키워드**: 최대 커버링 입지 모형, 기계학습, 지방도시, 스마트도서관

**초록**: 지방도시는 지역별 인구밀도의 차이가 수도권에 비해 상대적으로 크기 때문에 공공 서비스 설치 시 이용률 확보에 어려움을 겪는다. 본 연구는 지방도시의 여건을 고려하여 광주광역시 내 스마트도서관 기반 스마트 공공복합편의시설의 입지를 제안한다. 구체적으로 스마트 공공복합편의시설의 예상 수요량을 기계학습을 이용하여 추정한 후, 이를 바탕으로 최대 커버링 입지 모형을 적용하여 자치구별 스마트 공공복합편의시설의 최적입지를 제안한다. 최적입지 제안은 도서관 서비스 영역 내에 포함되는 수요량을 제거하고 선정하는 신규 설립과, 기존 도서관 위치를 고려하지 않는 기존 도서관의 이전의 두 방향으로 진행한다. 마지막으로 광산구를 대상으로 신규 설립과 이전을 결합한 스마트 공공복합편의시설 입지를 제안한다. 본 연구의 결과가 지방도시의 지속가능한 발전과 시민 복지 향상을 위한 효과적인 전략의 사례로 활용될 수 있기를 기대한다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 44. Influence Analysis of Pavement Distress on International Roughness Index Using Machine Learning

**저자명**: 권기범;최항석;Khanh Pham;Sang Woo Kim;Abraham Bae

**주저자 소속기관**: School of Civil, Environmental and Architectural Engineering, Korea University

**학술지명**: KSCE Journal of Civil Engineering

**저자키워드**: Influence analysis, International roughness index, Pavement distress, Severity, Interpretable machine learning

**초록**: The International Roughness Index (IRI) is closely related to pavement distress. However, previous studies employing statistics and machine learning approaches would present challenges in comprehensively analyzing the influence of pavement distress on IRI considering their severities. This study introduces interpretable machine learning to investigate the influence of pavement distress on IRI, with a particular focus on the severity of pavement distress. The pavement distress and IRI data for flexible pavements obtained from the long-term pavement performance (LTPP) program were meticulously preprocessed. The developed random forest (RF) model demonstrated satisfactory predictive performance, with an RMSE of 0.2191 and an R2 of 0.7874. The relationship between pavement distress and IRI, as captured by the developed model, was further analyzed using the SHapley Additive exPlanations (SHAP) method. The model interpretation identified the transverse crack, rutting, and alligator crack as the key factors influencing IRI. Notably, both transverse and alligator cracks exhibited significant contributions to IRI increment at medium and high severity levels, highlighting the importance of proactive maintenance for these distress types at lower severity levels. Additionally, a threshold in rutting depth was observed, which could increase IRI. A comparative analysis with the AASHTO MEPDG smoothness model demonstrated that the predictive performance of the RF model was notably superior.

**발행기관명**: 대한토목학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 45. 기계학습기법을 통한 액상화 발생가능 지수 예측에 관한 연구

**저자명**: 전준서;김종관;한진태;서승환;전병한

**주저자 소속기관**: Department of Geotechnical Engineering Research, Korea Institute of Civil Engineering and Building Technology (KICT)

**학술지명**: 한국지반환경공학회 논문집

**저자키워드**: 액상화 발생가능 지수, 시추공 자료, 기계학습, 베이지안 최적화, 초매개변수

**초록**: 실제 시추공 정보 및 지진파를 이용하여 액상화 발생가능 지수를 산정하고, 기계학습기법을 이용하여 액상화 발생가능 지수 예측모델을 학습하였다. 학습을 위해 지진파의 특징을 반영한 인자를 포함하여 총 10가지의 특징을 선택하였다. 일반적으로 이용되는 기계학습기법 중 사전학습을 통해 후보 모델을 선정하고, 후보 모델에 대해 베이지안 최적화를 적용하여 초매개변수를 최적화시켰다. 인공신경망, 가우시안 프로세스 회귀, 랜덤 포레스트 중 평균제곱근오차, 결정계수 및 과대적합 여부를 종합한 결과, 랜덤 포레스트가 액상화 발생가능 지수를 잘 예측하였다. 다만, 액상화 발생가능 지수가 5 이상에서는 액상화 발생가능 지수를 과소예측하는 경향을 보였다.

**발행기관명**: 한국지반환경공학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 46. 강화학습을 이용한 수처리 및 물환경 관리 최적화  기술의 현황 및 미래

**저자명**: 박정수

**주저자 소속기관**: 국립한밭대학교 건설환경공학과

**학술지명**: 상하수도학회지

**저자키워드**: 머신러닝,  운영비  절감,  강화학습,  상하수도  처리,  물환경  관리

**초록**: 강화학습은  지속적으로  변화하는  환경에서  최적의  해결책을  제시할  수  있도록  구현되는  머신러닝  알고리즘으로  시간  및  조건에  따라 변화하는  시스템의  최적화에  우수한  성능을  보이는  장점을  가지고  있다.  따라서,  최근  운영  조건과  시간에  따라  변화하는  상하수도 시설  및  취수원  등  현장  물환경  관리  최적화에  강화학습을  적용하기  위한  연구에  대한  관심이  높아지고  있다.  본  연구에서는  강화학습이 상하수도  시설  및  물환경  관리에  적용된  사례를  분석하였다.  상하수도  시설의  운영시  시설  운영의  목적에  맞는  처리수  수질을  유지하면서 운영에  필요한  에너지  소비  및  비용을  최소화하는  노력이  중요하다.  강화학습은  데이터에  기반한  반복적인  분석을  통해  시스템  운영의 최적  조건을  학습할  수  있으며,  다양한  연구  사례에서  강화학습의  적용을  통해  상하수도  시설  등의  운영  효율  개선이  가능함을  보여주었다.  하수처리  시설의  경우  강화학습을  활용하여  운영비의  많은  부분을  차지하는  폭기조  산소  공급과  내부  반송  펌프  운전을  최적화할  수  있으며,  정수장의  경우  약품  투입량  절감  등을  통해  운영비  절감  효과를  달성할  수  있음을  확인하였다.  또한,  용수  공급망과  저류조 운영의  최적화를  통해  상수도  및  하천  현장의  오염  발생을  저감할  수  있음을  알  수  있었다.  본  연구를  통해  강화학습을  활용하여 기존의  경험에  기반한  시설  운영  방식의  한계를  개선하고  상하수도  시설  운영  및  물환경  관리  효율  향상에  기여할  수  있음을  확인하였다.

**발행기관명**: 대한상하수도학회

**발행연도**: 2025

**주제분야**: 상하수도공학

---

## 47. 철근콘크리트 기둥에 대한 연성 기반 폭발손상평가를 위한 기계학습 모델

**저자명**: 김예은;김수빈;이기학;신지욱

**주저자 소속기관**: 경상국립대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 폭발손상평가, 철근콘크리트 기둥, 유한요소해석, 기계학습

**초록**: 본 연구의 목적은 변위 기반 내폭 성능 평가기법을 기반으로 한 신속 폭발손상 평가 기계학습 모델을 개발하는 것이다. 해당 모델은 파괴유형에 따른 폭발손상 예측 정확도의 향상을 위해 2가지의 기계학습 모델이 결합 되어있는 Multi-Step Learner로 구성하였다. 해당 모델의 입력변수는 기둥 상세, 폭발 규모, 그리고 기계학습 모델을 통해 도출한 파괴유형이며, 출력 변수는 변위 연성도 기반 폭발손상 등급이다. 모델 개발을 위해 학습 및 검증에 필요한 데이터베이스는 과거 연구에서 개발한 유한요소해석모델을 통해 도출하였으며, 높은 예측 성능을 도출하기 위해 7가지의 분류 학습기를 학습하여 높은 예측 성능을 보이는 Best-fit 모델을 선정하였다. 우수한 성능을 보인 Ensemble 기법은 검증 데이터에서 다른 학습기 대비 41.05 % 향상된 F-score 값과 14.65 % 향상된 AUC 값을 나타내었다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2024

**주제분야**: 재료학

---

## 48. 동수역학적 모형과 기계학습을 모형을 결합한 하천 홍수 예측모형

**저자명**: 이재경;전경수

**주저자 소속기관**: Department of Water Resources, Graduate School of Water Resources, Sungkyunkwan University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 홍수위 예측, 동수역학적 모형, 기계학습 모형, 혼합모형

**초록**: 홍수위 예측의 정확도를 향상시키기 위하여 분포형 매개변수를 갖는 동수역학적 흐름모형과 심화학습 기반의 오차보정 모형을 결합한 혼합모형을 제시하였다. 한강 하류구간을 대상으로 동수역학적 계산모형을 수립하였으며, 부정류 상태에서 Manning 조도계수의 시간적, 공간적 변동성을 고려하여 모형의 보정을 수행하였다. 이어지는 오차보정 과정에서는 장단기 기억 신경망(LSTM) 모형을 사용하여 동수역학적 모형의 시스템적 오차를 찾아내고자 하였다. 모형의 정확성을 평가하기 위하여 동수역학적 모형, 두 개의 LSTM 기반 모형(LSTM1, LSTM2) 및 혼합모형 등 4개 모형의 성능을 비교하였다. LSTM1은 현재까지의 관측 자료들만을 입력변수로 사용하는 모형이며, LSTM2는 여기에 이후 시간에서의 동수역학적 모형 경계조건들을 입력변수로 추가하여 수위를 예측하도록 수립된 모형이다. 평균제곱근 오차를 평가 지표로 하여 모형들의 성능을 평가한 결과, 혼합모형이 개별 모형들에 비하여 홍수위의 예측 정확성을 현저하게 개선하는 것으로 나타났다. 이는 혼합모형이 동수역학적 모형과 LSTM 모형의 상호 보완적인 장점들을 모두 취함으로써 가능한 것이라 할 수 있다. 또한 LSTM 기반의 혼합모형은 인공신경망 기반의 혼합모형보다도 우수한 성능을 보여, 예측 선행시간이 3시간인 경우에도 제곱평균제곱근 오차 10 cm 이내로 홍수위를 예측하는 것으로 나타났다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 49. 건설 리스크 도출을 위한 SVM 기반의 건설프로젝트 문서 분류 모델 개발

**저자명**: 강동욱;조민건;차기춘;박승희

**주저자 소속기관**: 성균관대학교

**학술지명**: 대한토목학회논문집(국문)

**저자키워드**: 공기 지연, 건설 재해, 데이터 분류, 텍스트 마이닝, SVM

**초록**: 건설프로젝트는 공기 지연, 건설 재해 등 다양한 요인으로 인한 리스크가 존재한다. 이러한 건설 리스크를 기반으로 건설프로젝트의 공사 기간의 산정 방법은 주로 감독자 경험에 의존한 주관적 판단으로 이루어지고 있다. 또한, 공기 지연과 건설 재해로 지연된 건설프로젝트 일정을 맞추기 위한 무리한 단축 시공은 부실시공 등의 부정적인 결과를 초래하며, 지연된 일정으로 인한 사회 기반 시설물 부재로 경제적 손실이 발생한다. 이러한 건설프로젝트의 리스크 해결을 위한 데이터 기반의 과학적 접근과 통계적 분석이 필요한 실정이다. 실제 건설프로젝트에서 수집되는 데이터는 비정형 텍스트 형태로 저장되어 있어 데이터를 기반으로 한 리스크를 적용하기 위해서는 데이터 전처리에 많은 인력과 비용을 수반하기 때문에 텍스트 마이닝을 활용한 데이터 분류 모델을 통한 기초자료를 요구한다. 따라서, 본 연구에서는 건설프로젝트 문서를 수집하여 텍스트 마이닝을 활용하여 SVM(Support Vector Machine) 기반의 데이터 분류 모델을 통해 리스크 관리를 위한 문서 기초자료 생성 분류 모델을 개 발하였다. 향후 연구 결과를 통해 정량적인 분석을 통해서 건설프로젝트 공정관리 등에 있어 효율적이고 객관적인 기초자료로 활용되어 리스크 관리가 가능해질 것으로 기대된다.

**발행기관명**: 대한토목학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 50. RC 기둥의 폭발 저항성능 예측을 위한 소수 데이터 세트 기반 기계학습 모델 방법론

**저자명**: 김예은;김수빈;이기학;신지욱

**주저자 소속기관**: 경상국립대학교

**학술지명**: 콘크리트학회 논문집

**저자키워드**: 폭발손상평가, 철근콘크리트 기둥, 유한요소해석, 기계학습

**초록**: 본 연구는 200개의 소수 데이터를 활용하여 철근콘크리트(RC) 기둥의 폭발 저항 성능을 정밀하게 평가할 수 있는 결합형기계학습 모델을 제안한다. 이를 위해 다양한 기둥 상세 및 폭발 규모 값을 고려한 유한요소해석 기반의 폭발 성능 평가 응답 데이터를구축하였다. 각 개별 학습 모델에는 7가지 분류 알고리즘이 적용되었으며, 가장 우수한 평가 지표를 보인 모델들을 선별하여 개발하였다. 제안된 기계학습 모델의 조합 기법은 기존의 700개 샘플 기반 모델 대비 데이터 사용량을 65.5 % 절감하면서도 평균 14.3 %의성능 향상을 달성하였다. 이는 데이터가 제한된 환경에서도 고정밀·고속 평가가 가능함을 입증하는 결과이다.

**발행기관명**: 한국콘크리트학회

**발행연도**: 2025

**주제분야**: 재료학

---

## 51. Do Perceptions of Hydrogen Energy Effect on Vehicle Preference? A Learning-Based Model Approach

**저자명**: 김우진;김정화;장정아;김숙희

**주저자 소속기관**: 경기대학교

**학술지명**: KSCE Journal of Civil Engineering

**저자키워드**: e-Mobility, Machine learning, Hydrogen fuel, Risk perception, Psychometric analysis, Decision tree analysis

**초록**: The attention towards hydrogen energy is growing as green energy sources are becoming more and more important over the world. the South Korean government has also implementedhydrogen economy since 2018 and established a plan to develop into a hydrogen economy leading country through fuel cell electric vehicles (FCEVs) and hydrogen fuel cells. Therefore, a preparatory process of verifying awareness and acceptance of FCEV and hydrogen energy through research is necessary. As there are issues about the safety of hydrogen energy due to several explosion accidents, we hypothesized that psychological attitudes to hydrogen energy like risk perception and familiarity would be effect on vehicle purchase behavior. In order to verify hypothesis this study analyzed using logistic regression and decision tree method, a machine learning technique for a preference model among FCEVs. The results show that hydrogen risk has a larger influence than hydrogen familiarity on the choice of FCEVs. In addition, we identified that the variables which are vehicle price, charge price, VKT(Vehicle Kilometers Traveled), distance to the charging station, gender, and age group also affect on vehicle purchase behavior. Using the decision tree algorithm in the AI technique, analysis results for vehicle preference in e-mobility (EVs, hybrid, FCEVs) show that hybrid vehicles select 46%, EVs 31%, FCEVs 23%. In addition, as a result of analyzing the influence of variables on the e-mobility Preference, the major variables were charge price, distance to the charging station, and vehicle price, in the descending order of importance.

**발행기관명**: 대한토목학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 52. 선형기계학습모델을 이용한 자갈해빈상에서의 쇄파지표 예측

**저자명**: 안을혁;이영찬;김도삼;이광호

**주저자 소속기관**: 해양수산부 부산항건설사무소

**학술지명**: 한국해안·해양공학회논문집

**저자키워드**: 쇄파파고, 쇄파수심, 자갈해빈, 기계학습, 선형모델

**초록**: 지금까지 쇄파는 발생기구의 본질적인 복잡성으로 인해 실내수리모형실험을 통해 쇄파파고 및 쇄파수심등의 쇄파지표 예측을 위한 많은 경험식이 제안되어 왔다. 하지만, 자갈해빈에 대한 쇄파의 특성 및 쇄파지표예측을 위한 연구는 거의 수행되어 있지 않았다. 본 연구에서는 자갈해빈을 대상으로 쇄파파고 및 쇄파수심의 예측을위하여 회귀 또는 분류 문제와 관련된 다양한 연구 분야에서 높은 예측 성능을 보이는 대표적인 선형기반 기계학습기법에 기반한 쇄파지표를 예측하고자 하였다. 먼저, 자갈해빈에 대하여 기존에 제안된 쇄파지표의 경험식의 적용성을 검토하고 기존의 경험식의 자갈해빈의 쇄파지표 예측성능의 한계성을 극복하기 위하여 다양한 선형기반 기계학습 알고리즘을 적용하여 쇄파지표 예측모델을 구축하였다. 구축된 기계학습모델 중 자갈해빈에서 발생하는 쇄파파고 및 쇄파수심에 대한 높은 예측성능을 보인 모델을 기반으로 손쉬운 계산이 가능한 쇄파지표에 대한 새로운산정식을 제안하였고 수리모형실험결과 및 기존의 경험식과 비교하고 새롭게 제안한 쇄파지표의 예측성능을 검증하였다. 본 연구에서 제안한 쇄파지표에 대한 경험식은 단순한 다항식임에도 불구하고 자갈해빈에 대한 양호한 예측성능을 보였다.

**발행기관명**: 한국해안,해양공학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 53. 1시간 호우피해 규모 예측을 위한 AI 기반의 1ST-모형 개발

**저자명**: 이준학;이하늘;강나래;황석환;김형수;김수전

**주저자 소속기관**: 인하대학교 스마트시티공학과

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 호우특보, 재해유발강우, 미신러닝, 호우피해규모

**초록**: 집중호우, 홍수 및 도시침수와 같은 재해를 저감시키기 위하여 자연 재난으로 인한 재해의 발생 여부를 사전에 파악하는 것은 중요하다. 현재 국내는 기상청에서 운영하고 있는 호우주의보 및 호우경보를 발령하고 있지만, 이는 전국에 일괄적인 기준으로 적용하고 있어 사전에 호우로 인한 피해를 명확하게 인지하지 못하고 있는 실정이다. 따라서, 일괄된 기준을 지역적 특성을 반영한 호우특보 기준으로 재설정하고 1시간 후에 강우로 발생할 수 있는 피해의 규모를 예측하고자 하였다. 연구 대상 지역으로는 호우피해가 가장 빈번하게 발생하였던 경기도 지역으로 선정하였고, 강우량 및 호우 피해액 자료를 활용하여 지역적 특성을 고려한 시간단위 재해 유발 강우를 설정하였다. 강우에 의한 호우피해 발생 여부를 예측하는 모형을 개발하기 위해 재해 유발 강우 및 강우 자료를 활용하였으며, 머신러닝 기법인 의사 결정 나무 모형과 랜덤 포레스트 모형을 활용하여 분석 및 비교하였다. 또한 1시간 후의 강우를 예측하기 위한 모형으로는 장단기 메모리, 심층 신경망 모형을 활용하여 분석 및 비교하였다. 최종적으로 예측 모형을 통해 예측된 강우를 훈련된 분류 모형에 적용하여 1시간 후 호우에 의한 규모별 피해 발생 여부를 예측하였고, 이를 1ST-모형이라고 정의하였다. 본 연구를 통해 개발된 1ST-모형을 활용하여 예방 및 대비 차원의 재난관리를 실시한다면 호우로 인한 피해를 저감하는데 기여 할 수 있을 것으로 판단된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 54. 아스팔트 층 두께 예측을 위한 통계적 모형과 기계학습 기법 활용에 대한 연구

**저자명**: 김연태;박혜민;박희문

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국도로학회논문집

**저자키워드**: Asphalt Layer Thickness, Machine Learning, Multiple Linear Regression (MLR), Prediction Model, Mean Absolute Percentage Error (MAPE)

**초록**: This study aimed to improve the accuracy of road pavement design by comparing and analyzing various statistical and machine-learning techniques for predicting asphalt layer thickness, focusing on regional roads in Pakistan. The explanatory variables selected for this study included the annual average daily traffic (AADT), subbase thickness, and subgrade California bearing ratio (CBR) values from six cities in Pakistan. The statistical prediction models used were multiple linear regression (MLR), support vector regression (SVR), random forest, and XGBoost. The performance of each model was evaluated using the mean absolute percentage error (MAPE) and root-mean-square error (RMSE). The analysis results indicated that the AADT was the most influential variable affecting the asphalt layer thickness. Among the models, the MLR demonstrated the best predictive performance. While XGBoost had a relatively strong performance among the machine-learning techniques, the traditional statistical model, MLR, still outperformed it in certain regions. This study emphasized the need for customized pavement designs that reflect the traffic and environmental conditions specific to regional roads in Pakistan. This finding suggests that future research should incorporate additional variables and data for a more in-depth analysis.

**발행기관명**: 한국도로학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 55. 기계학습 기반 지하매설물 속성 및 밀집도를 활용한 지반함몰 위험도 예측 모델

**저자명**: 이성열;강재모;김진영

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국지반환경공학회 논문집

**저자키워드**: 지반함몰, 지하매설물, 밀집도, 기계학습, 지반함몰 위험 예측모델

**초록**: 지반함몰의 주요 발생원인은 지하매설물의 손상으로 알려져 있다. 지반함몰은 상·하수관의 손상으로 인한 물길 형성에 따른 지반 내 토립자의 이동으로 공동이 형성되어 상부지반이 붕괴되는 메커니즘을 보이고 있다. 따라서 지반함몰은 지하매설물의 밀집도가 높은 도심지를 중심으로 발생하고 있으며, 사고 발생 시 인명 및 경제적 피해를 야기하므로 사고에 대한 대비가 반드시 필요하다. 이에 따라 지반함몰 위험을 예측하기 위한 연구가 꾸준히 수행되고 있으며, 본 연구에서는 ○○시의 2개 구를 대상으로 지반함몰 위험도 예측 모델을 제시하고자 하였다. 대상 지역의 지하매설물 속성 데이터(활용년수, 관직경)와 지하매설물 밀집도, 지반함몰 이력 데이터를 활용하여 데이터셋을 구축하고 전처리를 수행한 뒤, 기계학습 모델에 적용하여 최적의 평가지표가 도출되는 모델을 선정하였으며, 선정된 모델의 신뢰도를 평가하고 모델에서 도출되는 지반함몰 위험도 예측 시 활용된 영향인자의 중요도를 제시하고자 하였다.

**발행기관명**: 한국지반환경공학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 56. 암석 터널 막장의 3차원 포인트 클라우드에서 절리 계측을 위한 R-C-D 기계 학습 방법

**저자명**: 문상모;Bara Alseid;최항석;양정훈;문홍표;서형준

**주저자 소속기관**: 고려대학교

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: R-C-D 기계 학습 방법, 3D 포인트 클라우드, 암석 터널 막장, 경사각, 경사 방향

**초록**: 암석터널 굴착에서 절리는 터널 막장의 안정성을 판단하는데 중요한 요소중 하나이다. 본 연구에서는 지질 암석면의 경사각과 방향을 측정하기 위한 새로운 방법인 Roughness-CANUPO-Dip filtration (R-C-D)을 제시한 후 3개 현장 모델에 의해 평가했다. R-C-D 방법은 거칠기 분석, CANUPO 분석으로 구성된다. 또한 본 연구에서는 경사각 및 방향에 대한 네 가지 다른 측정 방법인 평면 피팅, 법선 벡터 변환, 면 세분화 및 나침반 측정을 평가한다. 결과는 모든 측정 방법에서 97~99.4% 범위의 정확도로 경사각을 정확하게 계산할 수 있음을 보여주었다. 면 세분화 방법은 수동적인 개입 없이 자동으로 정확한 결과를 제공할 수 있어 최적의 측정 방법으로 선택되었다. 법선 벡터를 계산하기 위해 사용되는 최적의 LNR (local neighbor radius)도 산출되었으며, LNR 값이 클수록 더 정확한 결과를 얻을 수 있지만 계산 시간도 증가하는 것으로 나타났다. 절리암대를 나타내는 추가 지점을 필터링하고 삭제하는 데 사용되는 경사각을 추정하기 위한 검증을 수행하였으며, 각 지점에 대해 최적 경사각은 각각 45°, 30°, 45°였다. R-C-D 방법은 절리면을 제거하고 절리 근입점을 유지하여 경사각과 방향을 얻기 위해 개발되었다. R-C-D 방법을 3개 현장 모델에 적용한 결과, 이 방법은 절리면을 감지하여 제거하는 데에 적합한 것으로 나타났으며, 경사각 필터링 방법은 절리대를 성공적으로 제거하였다. R-C-D 방법이 지질 구조를 정확히 구분하고 정밀한 경사각 및 방향 측정을 얻는 데 효과적이라는 것을 보여주었다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 57. 강우-유출 모의를 위한 개념적 모형과 기계학습 모형의 성능 비교

**저자명**: 이승철;김대하

**주저자 소속기관**: 전북대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 강우-유출 모의, 기계학습 알고리즘, 개념적 강우-유출 모형, 계측 및 미계측 유역 예측 기법, 인접성 기반 지역화

**초록**: 최근 기후변화로 인해 유역의 기상자료에 대한 반응이 달라지고 있어 강우-유출 모의에 대한 연구는 중요해지고 있다. 아울러 최근 기계학습 기법에 대한 높은 관심으로 이를 통한 강우-유출 모의 역시 활발하게 증가하고 있으나 기계학습 모형이 전통적으로 사용되어온 개념적 모형에 비해 활용성이 높은지는 아직 확실치 않다. 본 연구에서는 개념적 모형인 GR6J와 기계학습 모형인 Random Forest 성능을 한국 전역의 38개 계측 유역에 대해 계측 유역 예측기법과 미계측 유역 예측기법을 이용해 평가하였다. 먼저 계측 유역 적용기법 평가를 위해 각 모형을 관측 일 유량자료에 학습시키고 분리된 평가기간에 대한 모의성능을 비교하였다. 이후 미계측 유역 모의성능 평가를 위해 인접성 기반 지역화 방법을 Leave-One-Out Cross-Validation (LOOCV)을 이용해 평가하였다. 그 결과 계측 유역 평가에서는 Random Forest 기법이 GR6J 모형보다 일관되게 높은 성능을 보였다. 학습된 데이터를 출력 값으로 재생산하도록 구조화되어 있는 기계학습 기법이 개념적 이론을 통한 모형보다 높은 재현성을 갖기 때문으로 판단된다. 하지만 Random Forest 모형의 성능은 미계측 유역의 예측기법으로는 재현되지 않았고 GR6J 모형보다 성능이 더 낮은 것이 확인되었다. 본 연구는 기계학습 모형은 계측 유역의 유출예측에는 적용성이 높을 수 있으나 미계측 유역에 대한 적용가능성은 전통적인 개념적 모형보다 낮을 수 있음을 제시한다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 58. 생성형 인공지능 기반 터널 콘크리트 균열 영상 데이터의 증강을 위한 파라미터 분석

**저자명**: 심승보

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국터널지하공간학회 논문집

**저자키워드**: 터널 유지관리, 훈련 데이터 증강, 생성형 AI, 균열 탐지, 균열 영상

**초록**: 노후 인프라 구조물을 안전하게 유지하기 위해서는 지속적인 관리가 필요하며, 이는 터널 내부의 콘크리트 구조물에도동일하게 적용된다. 터널 구조물의 건전성 관리는 정기적인 점검과 정밀한 검사 기술을 통해 이루어진다. 기존의 검사 방법은 인력 기반으로, 작업자가 직접 현장을 방문하여 육안으로 상태를 확인하고 기록하는 방식이다. 이로 인해 구조물 상태는 경험적이고 주관적인 판단에 의해 결정될 수밖에 없는 상황이다. 이러한 문제를 개선하고 점검 결과의 객관성과 신뢰성을 높이기 위해 고해상도 카메라와 딥러닝을 활용한 방법이 활발히 연구되고 있다. 특히, 터널 구조물에 발생하는 균열을 탐지하는 신경망 모델 기반의 알고리즘은 높은 정확도를 보여주고 있다. 그러나 이러한 딥러닝 기술은 다수의 훈련영상 데이터가 확보되었다는 전제가 필요하다. 현실적으로 균열과 같은 손상 영상은 주변에서 흔히 찾아볼 수 없고, 이를확보하는 데 많은 비용과 시간이 소요된다. 이러한 문제를 해결하기 위해 본 연구에서는 생성형 AI를 이용해 균열 영상데이터를 증강하는 방법을 제안하였다. 또한, 실제와 유사한 균열 영상을 생성하기 위한 파라미터 분석을 완료하였고,그 결과 Fréchet Inception Distance가 31.73의 값을 나타내는 성능의 생성모델을 확보하였다. 이러한 방법은 향후 균열탐지 훈련 방법과 연계하여 유지관리 점검의 정확성과 신뢰성을 높이는 기술로 활용될 것으로 기대된다.

**발행기관명**: 사단법인 한국터널지하공간학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 59. AI 기법을 활용한 정수장 수질예측에 관한 연구

**저자명**: 이승민;강유진;송진우;김주환;김형수;김수전

**주저자 소속기관**: Program in Smart City Engineering, Inha University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: AI, 다중회귀, 전염소, 잔류염소 농도 예측모형, 염소제어

**초록**: 상수도 공급을 위한 정수장에서 전염소 또는 중염소 공정이 도입된 수처리 공정의 염소농도 관리에 필요한 공정제어를 위하여 AI 기술을 활용한 수질예측 기법이 연구되고 있다. 본 연구에서는 정수장 수처리 공정에서 실시간으로 관측, 생산되고 있는 수량･수질자료를 이용하여 염소소독 공정제어 자동화를 목적으로 침전지 후단의 잔류염소 농도를 예측하기 위한 AI 기반 예측모형을 개발하였다. AI 기반 예측모형은 과거 수질 관측자료를 학습하여 이후 시점의 수질에 대한 예측이 가능한 기법으로, 복잡한 물리･화학･생물학적 수질모형과 달리 간단하고 효율적이다. 다중회귀 모형과 AI 기반 모형인 랜덤포레스트와 LSTM을 이용하여 정수장의 침전지 후단 잔류염소 농도를 예측하여 비교하였다. 최적의 잔류염소 농도 예측을 위한 AI모형의 입출력 구조로는 침전지 전단의 잔류염소 농도, 침전지 탁도, pH, 수온, 전기전도도, 원수의 유입량, 알칼리도, NH3 등을 독립변수로, 예측하고자 하는 침전지 유출수의 잔류염소 농도를 종속변수로 선정하였다. 독립변수는 침전지 후단의 잔류염소에 영향이 있는 정수장에서 확보가 가능한 관측자료중에서 분석을 통해 선별하였으며, 분석 결과 연구대상 정수장인 정수장에서는 중회귀모형, 신경망모형, 모델트리 및 랜덤포레스트 모형을 비교한 결과 랜덤포레스트에 기반한 모형오차가 가장 낮게 도출되는 결과를 얻을 수 있었다. 본 연구에서 제시하는 침전지 후단의 적정 잔류염소 농도 예측값은 이전 처리단계에서 염소주입량의 실시간 제어가 가능토록 할 수 있어 수처리 효율 향상과 약품비 절감에 도움이 될 것으로 기대된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 60. HEC 소프트웨어 기반 홍수범람지도 엑셀러레이터 개발

**저자명**: 김종천;황석환;정종호

**주저자 소속기관**: 하존이앤씨㈜

**학술지명**: 대한토목학회논문집(국문)

**저자키워드**: 홍수, 홍수지도, HEC-RAS, RAS Mapper, 인공지능

**초록**: 최근 홍수예측과 관련한 연구에서 기계학습과 같은 인공지능 기법을 이용한 데이터모형의 활용에 관한 관심이 높다. 데이터모형은 미리 학습된 정보를 활용하기 때문에 모의에 소요되는 시간을 크게 줄일 수 있다는 장점이 있다. 그러나 데이터모형의 사전학습을 위해서는 많은 양의 침수자 료가 필요한 데 반하여 적용할 수 있는 실측자료가 부족한 것이 현실이다. 대안으로 매개변수가 검정된 물리모형의 모의 결과를 실측자료와 함께 사전학습자료로 활용하고 있다. 이러한 상황에서 본 연구에서는 하천범람에 의한 침수예측에 데이터모형을 활용하고자 사전학습을 위한 홍수범 람지도를 생성하는 엑셀러레이터를 개발하였다. 개발된 엑셀러레이터에서는 HEC-1을 이용한 홍수량 산정, HEC-RAS를 이용한 홍수위 산정, RAS Mapper를 이용한 하천범람 모의 및 침수예상도 출력의 전체 과정을 자동화한다. 이에 따라 사용자는 수백에서 수십만건의 강우시나리오 에 대하여 손쉽게 침수예상도 데이터베이스를 구축할 수 있다. 그래픽 편의 인터페이스(GUI)를 포함하여 홍수범람지도 작성에 필요한 다양한 편의기능을 탑재하고 있으며, 전국에 걸쳐서 위치한 26개소의 테스트베드에 적용하여 실무적용성을 검토하였다.

**발행기관명**: 대한토목학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 61. 위성영상의 계절적 특성에 따른 비닐하우스 탐지 결과 분석

**저자명**: 윤병현;장안진;성선경;최재완

**주저자 소속기관**: 지오포커스

**학술지명**: 한국측량학회지

**저자키워드**: 비닐하우스, 계절 영향, 딥러닝 모델

**초록**: 다양한 위성센서의 운용과 드론을 비롯한 탑재체들의 발전으로 인하여 획득할 수 있는 원격탐사 자료들이 지속적으로 증가하고 있다. 또한, 인공지능 및 빅데이터 기술의 발전으로 인하여 다량의 자료를 효과적으로 처리할 수있는 기술에 대한 연구들도 활발하게 이루어지고 있다. 본 연구에서는 다양한 시기에 취득된 위성영상을 이용하여 농경지의 비닐하우스 지역을 효과적으로 탐지할 수 있는 방법에 대하여 분석하였다. 이를 위하여, 봄, 여름, 겨울에 취득된 위성영상들을 이용하여 훈련자료를 구축하였다. 특히, 비닐하우스 지역은 계절의 영향을 받지 않기 때문에, 충분한 수의 다양한 시기에 취득된 영상들을 통합하여 훈련자료를 추가적으로 생성하였다. 총, 4종류의 훈련자료를 구축하고, 이를 이용하여 비닐하우스 탐지를 위한 딥러닝 모델의 학습을 수행하였다. 딥러닝 모델의 평가 결과, 다양한 시기의 위성영상을 통합하여 구성한 학습자료를 이용하여 구축된 딥러닝 모델의 비닐하우스 탐지 결과가 가장 우수한 성능을 나타내는 것을 확인하였다. 다양한 지역 및 시기에 취득된 위성영상을 지속적으로 구축하고, 이를 통하여 비닐하우스 탐지 모델을 구성할 경우, 향후 농업지역 모니터링에 효과적으로 적용할 수 있을 것으로 기대된다.

**발행기관명**: 한국측량학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 62. U-Net 및 U-Net++ 구조 기반의 초단기 레이더 강우예측 모델 성능 비교

**저자명**: 정민도;윤광석;권현한

**주저자 소속기관**: Department of Civil and Environmental Engineering, Sejong University

**학술지명**: 한국수자원학회 논문집

**저자키워드**: U-Net++, 딥러닝, 레이더, 강우 예측

**초록**: 본 연구에서는 딥러닝 기반의 U-Net++ 모형을 활용하여 강우 레이더 예측 모델을 개발하고, 기존의 U-Net 모형과의 성능을 정량적으로 비교하였다. 강우 예측의 성능 평가는 CSI(Critical Success Index)와 RMSE(Root Mean Square Error)를 이용하여 강우 임계치에 따라 선행시간별로 수행되었다. 연구 결과, U-Net++ 모형은 U-Net 모형에 비해 RMSE가 전반적으로 낮아, 양적 예측 성능이 향상되었음을 확인하였다. 반면, CSI의 경우 기존 U-Net 모형이 더 높은 값을 보여 강우 발생 여부 예측에 있어 우수한 성능을 나타냈다. 그러나 임계치가 커지고 선행시간이 증가함에 따라 두 모델 모두 CSI가 감소하고 RMSE가 증가하는 경향을 보였다. 또한, 소양강 유역의 유역 면적 강수량을 지상 강우, 강우 레이더, U-Net++ 모형, 그리고 U-Net 모형을 활용하여 비교하였다. 총 8개의 강우사상을 대상으로 10분 간격으로 누적 유역 면적 강수량을 산정한 결과, U-Net++ 모형은 선행시간이 길어질수록 다소 과대 추정되는 경향이 있었지만, 60분까지의 누적 유역 면적 강수량 예측 성능에서는 U-Net 모형보다 우수함을 보였다. 특히, 강우량이 상대적으로 많은 사상에서 U-Net++ 모형은 지상 강우 및 강우 레이더와의 높은 유사도를 나타내었으며, RMSE 분석에서도 더 낮은 중앙값과 적은 변동성을 보여 예측 성능이 우수함을 확인하였다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 63. 물리정보 기반 딥러닝을 이용한 도시침수 해석: 온천천 유역 사례

**저자명**: 우현아;최현진;김민영;노성진

**주저자 소속기관**: Department of Civil Engineering, Kumoh National Institute of Technology

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 인공지능, 딥러닝, 물리정보, 도시침수, 홍수 예측

**초록**: 기후변화로 인한 집중호우의 증가로 도시침수의 발생 빈도가 높아짐에 따라, 침수 위험 지역에서의 신속한 대응을 위해 2차원 침수해석 정보가 필요하다. 하지만, 기존 물리과정 기반 모형은 고해상도 침수 정보 생산에 높은 계산 비용이 요구되어 실시간 활용에 한계가 있다. 본 연구에서는 물리과정 기반 모형의 도시침수 공간분포 해석 결과를 신속하고 정확하게 모사할 수 있는 CNN (Convolutional Neural Network) 기반 딥러닝 모형을 개발하고 그 적용성을 평가하였다. 부산 온천천 유역을 대상으로 물리과정 기반 모형으로 다양한 가상 강수 시나리오에 대해 10 m 공간해상도의 2차원 침수 정보를 생성하고, CNN 모형을 훈련시켰다. 모형의 검증에는 2014년과 2020년의 두 가지 과거 침수 사상에 대한 물리모형 대비 최대 침수심 해석 재현성을 HR (Hit Rate), FAR (False Alarm Ratio), CSI (Critical Success Index) 등의 정량지표로 평가하였다. 또한, 딥러닝 모형에서 강수량의 시간 변동성이 미치는 영향을 평가하기 위해 강수 입력의 시간 범위(강수 윈도우)에 따른 민감도 분석을 수행하였다. 모의 결과, 2014년 침수사상은 HR 0.98, FAR 0.12, CSI 0.85, 2020년 침수사상은 HR 0.92, FAR 0.19, CSI 0.76 로 CNN 모형이 기존 물리모형 대비 침수 공간분포를 적절하게 재현함을 확인하였다. 강수 윈도우 분석 결과, 2014년 사상에서는 6시간, 2020년 사상에서는 2시간 범위를 입력할 때 CNN 모형의 성능이 최적이었다. 또한, 딥러닝 기반 모형은 물리과정 기반 모형의 순차 계산 대비 연산 시간을 약 98%, 병렬 계산 대비 약 90% 단축할 수 있어 준실시간에 가까운 효율적 침수 예측이 가능함을 확인하였다. 제안된 딥러닝 기반 모형은 계산 효율성과 정확도 측면에서 물리과정 기반 모형의 대안으로 활용 가능하며, 도시 침수 예측 및 조기 경보 시스템의 운영을 위한 효율적인 도구가 될 수 있을 것으로 기대된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 64. 관로 조사를 위한 오토 인코더 기반 이상 탐지기법에 관한 연구

**저자명**: 김관태;이준원

**주저자 소속기관**: 주식회사 키네틱스 기술연구소

**학술지명**: 상하수도학회지

**저자키워드**: 이상 탐지, 오토 인코더, 딥러닝, 관로 조사

**초록**: In this study, we present a sewer pipe inspection technique through a combination of active sonar technology and deep learning algorithms. It is difficult to inspect pipes containing water using conventional CCTV inspection methods, and there are various limitations, so a new approach is needed. In this paper, we introduce a inspection method using active sonar, and apply an auto encoder deep learning model to process sonar data to distinguish between normal and abnormal pipelines. This model underwent training on sonar data from a controlled environment under the assumption of normal pipeline conditions and utilized anomaly detection techniques to identify deviations from established standards. This approach presents a new perspective in pipeline inspection, promising to reduce the time and resources required for sewer system management and to enhance the reliability of pipeline inspections.

**발행기관명**: 대한상하수도학회

**발행연도**: 2024

**주제분야**: 상하수도공학

---

## 65. 딥러닝을 활용한 스트리트뷰에서의 barrier-free 출입 객체 탐지

**저자명**: 김혜진;박슬아;김지영

**주저자 소속기관**: 건국대학교 Social Eco Tech 연구소

**학술지명**: 한국측량학회지

**저자키워드**: 객체 탐지, 스트리트뷰, 딥러닝, Barrier-free

**초록**: 교통약자의 이동권 보장은 사회적으로 중요한 이슈로 부각되고 있으며, 이에 따라 공공건물 및 시설물에 대해 장애물 없는 생활환경(BF: Barrier-Free) 인증 제도가 의무화되고 있다. BF와 관련된 요소 중에서 건물 출입구의 접근성 정보는 휠체어 사용자가 실외와 실내를 원활하게 이동하는 데 있어 핵심적인 요소이다. 그러나 현장 조사를 통해 이러한 정보를 수집하고 관리하는 것은 높은 시간적·비용적 제약으로 인해 어려움이 있다. 본 연구는 스트리트뷰 영상을 활용하여 건물 출입구와 BF 관련 객체(출입문, 회전문, 계단, 경사로)를 탐지하는 딥러닝 기반 프레임워크를 제안한다. 휠체어가 접근 가능한 출입문, 경사로, 접근성을 저해하는 회전문 및 계단을 탐지 대상으로 설정하였으며, YOLOv5 모델을 이용하여 학습 및 객체 탐지를 수행하였다. 학습 데이터셋은 스트리트뷰 영상, 서울시 공공 데이터의 건물 출입문 사진, 오픈 데이터셋을 통합하여 구성하였으며, 탐지된 객체를 기반으로 출입구의 BF 상태를 분석하였다. 실험 결과, 추가 데이터셋을 포함하여 학습한 경우에 스트리트뷰 단독 데이터를 사용한 경우보다 전반적으로 탐지 정확도가 향상되었으며, 모든 데이터셋을 활용한 조합에서 가장 높은 정확도(검증 mAP50: 0.657, 테스트 mAP50: 0.532)를 기록하였다. 그러나 경사로와 계단 탐지 성능은 상대적으로 낮았으며, 이는 비정형 형태와 제한된 학습 샘플 때문으로 분석된다. 본 연구는 BF 정보 자동 구축의 가능성을 제시하며, 접근성 평가 방법의 개선 방향을 제안한다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 66. 딥러닝 기반 위성영상 건물 폴리곤 추출 알고리즘 비교 분석

**저자명**: 최연오;박진혁;이승우;신상헌;곽송연

**주저자 소속기관**: Lodics Co.,LTD

**학술지명**: 한국측량학회지

**저자키워드**: 위성영상, 건물 추출, 폴리곤 추출, 딥러닝 알고리즘

**초록**: 본 연구는 위성영상에서 건물을 추출하는 최신 알고리즘을 산업에서 활용되는 위성영상 데이터셋으로 비교평가하였다. 위성영상 건물 추출 알고리즘 분야에서 우수한 성능을 보인 세 가지 알고리즘 Frame Field Learning, PolyWorld, HiSup에 새롭게 라벨링 한 테스트 데이터셋을 넣어 AP (Average Precision), IoU (Intersection over Union), C-IoU (Complete-Intersection over Union), PoLiS (Polygons and Line Segments), MTA (Max Tangent Angle Error) 다섯 가지 성능지표를 구해 평가하였다. 실험 결과, 세 가지 알고리즘 중에서 Frame Field Learning이 모든 지표에서 우수한 결과를 나타냈다. 추후 Frame Field Learning에 활용하려는 위성영상을 학습시키고 알고리즘을 고도화한다면 산업에 적용할 수 있을 것으로 기대한다.

**발행기관명**: 한국측량학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 67. 인공지능 학습용 토공 건설장비 영상 데이터셋 구축 및 타당성 검토

**저자명**: 나종호;신휴성;이재강;윤일동

**주저자 소속기관**: 한국건설기술연구원 미래스마트건설연구본부 학생연구원

**학술지명**: 대한토목학회논문집(국문)

**저자키워드**: 토목 현장 데이터, 건설 장비, 딥러닝, 영상처리

**초록**: 최근 건설 현장의 안전사고 비율은 전체 산업에서 가장 높은 비중을 차지한다. 인공지능 기술을 건설 현장에 접목하기 위해서는 기초 학습 자료로 활용될 수 있는 데이터셋 확보가 필수적이다. 본 논문에서는 실제 현장 확보를 통해 원천 데이터를 수집하였으며, 토목 현장에서 주로 운용되고 있는 주요 건설장비 객체를 선정하고 약 9만장의 정지영상 데이터셋 가공을 통해 최적의 학습 데이터셋 구축을 완료하였다. 또한, 객체 인식분야의 대표적인 모델인 YOLO를 활용하여 구축된 데이터의 검증 작업을 수행하였고 90 % 근접한 검출 성능을 확인해 데이터 신뢰성을 확보하였다. 본 연구에서 사용되는 학습 데이터셋은 공공데이터포털에서 활용 가능하도록 공개를 완료하였다. 본 데이터셋은 향후 건설안전 분야의객체 인식 기술의 건설현장 적용을 위한 기반 데이터로 활용 가능하리라 판단된다.

**발행기관명**: 대한토목학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 68. Transformer 딥러닝 모델의 학습 데이터 구성에 따른 라이다 데이터 분류 분석

**저자명**: 임재형;손경완;김경휘;이동천

**주저자 소속기관**: 새한항업

**학술지명**: 한국측량학회지

**저자키워드**: 라이다, 딥러닝, 트랜스포머 모델, 학습 성능, 분류

**초록**: 딥러닝이 추구하는 목표는 학습 효율과 예측에 대한 정확성 향상이며, 더 나아가 학습된 딥러닝 모델의 적용 범 위를 넓혀서 일반성과 범용성을 확대하는 것이다. 이를 위해 최근에는 혁신적 개념의 트랜스포머 구조의 딥러닝 모 델이 개발되고 있다. 본 논문에서는 트랜스포머 기반의 SPT (Superpoint Transformer) 모델을 여러 경우의 학습 데이터 구성과 학습 조건에 대해 대용량의 고밀도 항공 라이다 데이터인 DALES (Dayton Annotated Laser Earth Scan) 데이터 셋으로 학습을 수행하여 라이다 데이터의 의미적 분할을 수행하였다. 결과를 분석하여 SPT 모델의 학습 성능과 예측 결과의 정확도를 분석하였다. SPT 모델의 superpoint는 딥러닝의 학습 효율과 결과에 대한 신뢰 성을 높이는 데 기여하기 위한 의미 있는 특성을 내포하고 있으며, 점군 데이터 분할을 위한 핵심적인 요소이다. 또 한 선형성, 평면성, 산란성 및 수직과 같은 라이다 데이터에 내재된 고유의 특성 정보를 원래 라이다의 표고 데이터 와 함께 학습에 사용함으로써 학습 성능을 향상시킬 수 있는 장점이 있다. 본 연구에서는 네개의 학습 조건을 구성 하여 SPT 모델의 성능을 평가하였다. 실험 결과, 가장 우수한 조건에서는 97.61% 의 정확도를, 가장 열악한 조건에 서는 84.28%의 정확도를 기록하였다. 학습 데이터의 수량과 에포크를 극단적으로 줄인 경우에도 신뢰성 높은 타 당한 분류 결과를 보여주었다.

**발행기관명**: 한국측량학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 69. 소형 유물 3D 모델 생성을 위한 이미지 매팅기반 턴테이블 시스템 구축 및 평가

**저자명**: 최석근;이승기;최도연;김광호

**주저자 소속기관**: 충북대학교

**학술지명**: 한국측량학회지

**저자키워드**: 딥러닝, 유물 이미지, 실감모형, 매팅, 턴테이블

**초록**: 문화재 분야에서 사진측량 소프트웨어를 통해 3D 기록을 제작하는 것이 보편화 되고 있다. 특히, 소형 유물에 있어 사진측량을 이용한 데이터 기록은 턴테이블을 이용하여 빠르게 취득하는 방법이 일반적이다. 하지만 턴테이블을 이용한 3D 기록은 이미지 취득에 있어 배경의 제거와 유물의 전체 이미지를 취득하는데 어려움이 있어다. 본 연구에서는 딥러닝 기반의 이미지 매팅 알고리즘을 이용하여 취득된 이미지의 배경을 제거하고 소형 유물의 전체 이미지를 보다 빠르게 취득하기 위하여 다시점 카메라와 턴테이블 시스템을 이용하였다. 제안된 방법과 기존의 방법을 비교하기 위하여 감독자 분류 이미지 매팅을 수행하였다. 추출된 이미지를 이용하여 사진측량소프트웨어 적용 3D 모델을 생성하고 정성적, 정량적 결과를 평가하였다. 그 결과 정량적 평가에서 5%이내의 오차를 보였으며, 정성적 평가에서도 기존의 방법(감독자 분류)과 같이 구멍, 모서리 누락부분, 노이즈가 없는 결과를 보였다. 따라서 제안된 방법은 턴테이블을 이용한 소형 유물의 이미지 취득 및 3D 모델 생성에 있어 높은 정확도와 빠른 처리 속도를 나타냈으며, 실제 유물 촬영 및 3D 모델 생성에서 그 활용 가능성을 확인하였다.

**발행기관명**: 한국측량학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 70. 고해상도 도시 침수 해석을 위한 딥러닝 기반 초해상화 기술 적용

**저자명**: 최현진;이송희;우현아;김민영;노성진

**주저자 소속기관**: 금오공과대학교

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 딥러닝, 초해상화, 도시 침수, 고해상도

**초록**: 기후변화와 도시화의 영향으로 인해 자연재해의 발생빈도와 규모가 증가하고 있다. 특히 도시 침수는 발생 시간이 짧고 막대한 인명 및 경제적 손실을 초래할 수 있기 때문에 신속하고 정확도 높은 예측 정보 생산이 중요하다. 하지만, 기존 물리과정 및 인공지능 기반 기법은 고해상도 침수 해석을 위해 많은 전산 자원이나 데이터가 요구되는 한계가 있다. 본 연구에서는 딥러닝 기반 초해상화(Super-Resolution) 기법을 통한 고해상도 도시 침수 해석 방법을 제안하고 적용성을 평가한다. 제안된 방법은 고해상도 물리 모형의 결과로 훈련된 초해상화 딥러닝 모형을 이용하여 저해상도 침수 해석 이미지를 고해상도로 변환한다. 미국 포틀랜드 도심지의 두 가지 침수 사례에 대해 적용, 4 m 공간해상도 물리 모의 결과를 1 m 급 고해상도 침수 해석 정보로 초해상화 하였으며, 초해상화 이미지와 고해상도 원본 간 높은 구조적 유사성이 확인되었다. 성능 지표로 평가한 결과, 전체 검증 대상 이미지에 대한 평균 PSNR 22.77 dB, SSIM 0.77로 우수하여, 초해상화 기법의 도시 침수 해석 적용성이 검증되었다. 제안된 방법은 적은 양의 침수 시나리오만으로도 효율적인 딥러닝 모형 훈련이 가능하고, 물리 모형의 정보를 최대한 활용할 수 있기 때문에, 고해상도 도시 침수 정보 생산에 효과적으로 사용될 수 있을 것으로 기대된다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 71. 적대적 생성 신경망을 이용한 레이더 기반 초단시간 강우예측

**저자명**: 윤성심;신홍준;허재영

**주저자 소속기관**: 한국건설기술연구원

**학술지명**: 한국수자원학회 논문집

**저자키워드**: 레이더, 강우예측, 적대적 생성 신경망, 딥러닝

**초록**: 적대적 생성 신경망 기반의 딥러닝 모델은 학습된 정보를 바탕으로 새로운 정보를 생성하는데 특화되어 있다. 구글 딥마인드에서 개발한 deep generative model of rain (DGMR) 모델은 대규모 레이더 이미지 데이터의 복잡한 패턴과 관계를 학습하여, 예측 레이더 이미지를 생성하는 적대적 생성 신경망 모델이다. 본 연구에서는 환경부 레이더 강우관측자료를 이용하여 DGMR 모델을 학습하고, 2021년 8월 호우사례를 대상으로 적대적 생성 신경망을 이용하여 강우예측을 수행하고 기존 예측기법들과 정확도를 비교하였다. DGMR은 대체적으로 선행 60분까지는 강우 분포 위치가 관측강우와 가장 유사하였으나, 전체 영역에서 강한 강우가 발생한 사례에서는 강우가 지속적으로 발달하는 것으로 예측하는 경향이 있었다. 통계적 평가에서도 DGMR 기법이 1시간 선행예측에서 임계성공지수 0.57~0.79, 평균절대오차 0.57~1.36 mm로 나타나 타 기법 대비 효과적인 강우예측 기법임을 보여주었다. 다만, 생성 결과의 다양성이 부족한 경우가 발생하여 예측 정확도를 저하하므로 다양성을 개선하기 위한 연구와 2시간 이상의 선행예측에 대한 정확도 개선을 위해 물리기반 수치예보모델 예측강우 자료를 이용한 보완이 필요할 것으로 판단되었다.

**발행기관명**: 한국수자원학회

**발행연도**: 2023

**주제분야**: 토목공학

---

## 72. 딥러닝 기반 강수 예측 모델 개선 연구: 가중 평균 앙상블 기법을 통한 성능 향상

**저자명**: 오세훈;주유형;박상윤;홍지완;허준

**주저자 소속기관**: 연세대학교(Yonsei University)

**학술지명**: 한국측량학회지

**저자키워드**: 단기 강수 예측, HSR, 딥러닝, U-Net, Attention, 앙상블

**초록**: 본 연구는 다중 고도각 기반 합성 강우량(HSR) 데이터를 활용해 강원도 지역을 대상으로 딥러닝 기반 단기 강수 예측 모델을 개발하고, 가중 평균 앙상블 기법을 적용해 강수 예측 성능을 개선하고자 하였다. 최근 기후 변화로 극한 강수 사건의 빈도와 강도가 증가함에 따라, 정확하고 신뢰성 높은 단기 강수 예측의 필요성이 커지고 있다. 이를 위해 U-Net과 Attention 메커니즘을 적용한 다양한 모델(SE U-Net, Attention U-Net, Dual Attention U-Net)을 학습하고, 각 모델의 예측 결과를 가중 평균 앙상블로 결합하였다. Attention 메커니즘은 중요한 정보를 포착하고 불필요한 신호를 억제하여 강수의 위치와 강도를 보다 정밀하게 예측하는 데 기여하지만, 낮은 강수 강도에서는 과적합으로 인해 오탐률(FAR)이 증가하는 현상이 나타났다. 이를 보완하기 위해 앙상블 기법을 적용하여 과적합을 줄이고 예측의 신뢰성을 높이고자 하였다. 실험 결과, 30mm/h 이상의 극한 강수를 제외한 다양한 강수 조건에서 단일 모델에 비해 모든 성능 지표에서 일관된 성능 향상이 나타났으며, 앙상블 기법이 Attention 기반 모델의 장점을 유지하면서도 과적합 문제를 줄여 예측의 신뢰성과 정확도를 높이는 데 효과적임을 확인하였다. 본 연구는 Attention 메커니즘과 앙상블 기법의 결합이 강수 예측 성능을 효과적으로 향상시킬 수 있음을 보여주며, 향후 다양한 기상 데이터와 앙상블 기법의 확장을 통해 더 일반화된 예측 모델 개발의 필요성을 제안한다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

## 73. 인공신경망을 활용한 박스 구조물 부재력의 최적 예측 모델 개발

**저자명**: 신서연;윤누리;박건;홍기남

**주저자 소속기관**: 국립재난안전연구원 지진방재센터

**학술지명**: 대한토목학회논문집(국문)

**저자키워드**: 박스 구조물, 딥러닝, 유한요소법, 부재력

**초록**: 토목공사에서 박스 구조물은 고대부터 현대에 이르기까지 다양한 토목 구조물의 건설에 널리 사용되어 왔으며, 향후 그 사용이 더욱 증가하고 대형화될 것으로 예상된다. 현재 박스 구조물의 안전성을 확인하기 위해 널리 사용되는 해석기법인 유한요소법(Finite Element Method, FEM)은 정밀한 해석을 제공하는 유용한 도구이나, 복잡한 모델링과 해석 과정으로 인해 많은 시간과 노력이 소요되며, 대규모 구조물의 경우 해석 시간이 길어져 설계 및 검토 과정이 비효율적일 수 있다. 따라서, 본 연구에서는 박스 구조물의 상시 해석 및 지진 해석을 유한요소법을 사용하여 수행하고, 이를 통해 얻어진 해석 결과를 바탕으로 딥러닝 모델을 구축하여 구조물의 부재력을 예측하고자 하였다. 이를 위해 MIDAS 소프트웨어를 사용하여 총 600개의 수치모델을 생성하였으며, 예측 성능은 MSE, MAE, R2 등의 지표로 평가하였다. 결과는 정적 하중 조건에서의 예측이 지진 하중 조건보다 우수함을 보여주며, 이는 복잡한 동적 응답의 영향을 반영한 것으로 판단된다. 본 연구는 딥러닝 기술이 구조 해석 분야에서 유한요소법을 보완할 수 있는 가능성을 제시하였으며, 향후 구조물의 안전성 평가 및 설계 과정에서의 효율성을 높이는 데 기여할 수 있을 것으로 판단된다.

**발행기관명**: 대한토목학회

**발행연도**: 2025

**주제분야**: 토목공학

---

## 74. 딥러닝을 활용한 거리뷰 기반 도시 범죄요인 분석: 범죄예방 환경설계(CPTED) 전략을 중심으로

**저자명**: 전현진;양병윤

**주저자 소속기관**: 동국대학교

**학술지명**: 한국측량학회지

**저자키워드**: 도시범죄, 거리뷰, 딥러닝, CPTED, 스피어만 상관분석

**초록**: 현대 도시에서 범죄는 시민의 안전과 삶의 질을 저해하는 중요한 사회 문제이며, 이를 해결하기 위해 물리적 환경요인에 관한 연구는 필수적이다. 기존 연구들은 이러한 요인을 객관적이고 정량적으로 분석하는 데 한계가 있었다. 이에 본 연구는 거리뷰와 딥러닝 기술을 활용하여 도시의 물리적 환경이 범죄 발생에 미치는 영향을 분석하고자 한다. 특히, 물리적 환경 설계를 통한 범죄 예방 전략인 CPTED(범죄예방 환경설계)에 기반하여, 범죄와 관련 있는 환경 요인을 변수로 선정하고 이를 정량적으로 평가하였다. 딥러닝 모델인 DeepLabV3+를 적용해 보스턴 지역의 거리뷰 이미지에서 물리적 환경 요인을 추출하고, 이들의 공간적 분포를 분석하였다. 또한, 실제 범죄 데이터와의 스피어만 상관분석을 통해 각 요인이 범죄 발생에 미치는 영향을 파악하였다. 연구 결과, CPTED 실천 원리 중 '영역성'과 '활동 지원' 관련 요인들이 범죄 발생과 유의미한 상관성을 보였으며, 특히 녹지율 등이 범죄 발생에 중요한 역할을 한다는 점을 확인하였다. 본 연구는 이러한 결과를 통해 범죄에 영향을 미치는 주요 요인들을 밝혀내어, 안전하고 지속 가능한 도시 환경 조성 및 범죄 예방 정책 수립에 기여할 수 있을 것으로 기대된다.

**발행기관명**: 한국측량학회

**발행연도**: 2024

**주제분야**: 토목공학

---

