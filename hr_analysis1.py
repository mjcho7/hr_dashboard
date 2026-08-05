import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

st.set_page_config(page_title="퇴직율 대시보드", layout="wide")

# seaborn 테마를 먼저 적용한 뒤 한글 폰트를 설정해야
# seaborn이 폰트를 Arial로 다시 변경하지 않음
sns.set_theme(style="whitegrid")
koreanize_matplotlib.koreanize()
plt.rcParams["axes.unicode_minus"] = False

# 1) 데이터 로드
@st.cache_data
def load_df(path:str ="HR Data.csv") -> pd.DataFrame:
    try:
        df = pd.read_csv(path, encoding="utf-8")
    except: 
        return df 
    df["퇴직"] = df["퇴직여부"].map({"Yes":1, "No":0}).astype("int8")
    df.drop(['직원수', '18세이상'], axis=1, inplace=True)
    return df

df = load_df()
if df.empty:
    st.error("데이터가 없습니다. 'HR Data.csv' 파일을 확인하세요.")
    st.stop()

# ===== KPI  =====
# 1) 헤더 & KPI
st.title("퇴직율 분석 및 인사이트")
n = len(df); quit_n = int(df["퇴직"].sum())
quit_rate = df["퇴직"].mean()*100
stay_rate = 100 - quit_rate
k1,k2,k3,k4 = st.columns(4)
k1.metric("전체 직원 수", f"{n:,}명")
k2.metric("퇴직자 수", f"{quit_n:,}명")
k3.metric("유지율", f"{stay_rate:.1f}%")
k4.metric("퇴직율", f"{quit_rate:.1f}%")

# ===== 2행 3열 퇴직 현황 그래프 =====
# 퇴직 여부(0, 1)를 백분율(0, 100)로 변환
df["퇴직률"] = df["퇴직"] * 100

# 연령, 근속연수, 월급여를 구간으로 나누기
df["연령대"] = pd.cut(
    df["나이"],
    bins=[0, 29, 39, 49, 59, 100],
    labels=["20대 이하", "30대", "40대", "50대", "60대 이상"]
)

df["근속구간"] = pd.cut(
    df["근속연수"],
    bins=[-1, 2, 5, 10, 20, 100],
    labels=["2년 이하", "3~5년", "6~10년", "11~20년", "21년 이상"]
)

df["월급여구간"] = pd.cut(
    df["월급여"],
    bins=[0, 3000, 6000, 10000, 15000, float("inf")],
    labels=["3천 이하", "3~6천", "6천~1만", "1만~1.5만", "1.5만 초과"]
)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1. 부서별 퇴직률
sns.barplot(data=df, y="부서", x="퇴직률", estimator="mean",
            errorbar=None, ax=axes[0, 0])
axes[0, 0].axvline(quit_rate, color="red", linestyle="--")
axes[0, 0].set_title("부서별 퇴직률")
axes[0, 0].set_xlabel("퇴직률(%)")

# 2. 연령대별 퇴직률
sns.barplot(data=df, x="연령대", y="퇴직률", estimator="mean",
            errorbar=None, ax=axes[0, 1])
axes[0, 1].axhline(quit_rate, color="red", linestyle="--")
axes[0, 1].set_title("연령대별 퇴직률")
axes[0, 1].set_ylabel("퇴직률(%)")

# 3. 근속구간별 퇴직률
sns.barplot(data=df, x="근속구간", y="퇴직률", estimator="mean",
            errorbar=None, ax=axes[0, 2])
axes[0, 2].axhline(quit_rate, color="red", linestyle="--")
axes[0, 2].set_title("근속구간별 퇴직률")
axes[0, 2].set_ylabel("퇴직률(%)")

# 4. 야근 여부별 퇴직률
sns.barplot(data=df, x="야근정도", y="퇴직률", estimator="mean",
            errorbar=None, ax=axes[1, 0])
axes[1, 0].axhline(quit_rate, color="red", linestyle="--")
axes[1, 0].set_title("야근 여부별 퇴직률")
axes[1, 0].set_ylabel("퇴직률(%)")

# 5. 출장 빈도별 퇴직률
sns.barplot(data=df, x="출장빈도", y="퇴직률", estimator="mean",
            errorbar=None, ax=axes[1, 1])
axes[1, 1].axhline(quit_rate, color="red", linestyle="--")
axes[1, 1].set_title("출장 빈도별 퇴직률")
axes[1, 1].set_ylabel("퇴직률(%)")
axes[1, 1].tick_params(axis="x", rotation=15)

# 6. 월급여 구간별 퇴직률
sns.barplot(data=df, x="월급여구간", y="퇴직률", estimator="mean",
            errorbar=None, ax=axes[1, 2])
axes[1, 2].axhline(quit_rate, color="red", linestyle="--")
axes[1, 2].set_title("월급여 구간별 퇴직률")
axes[1, 2].set_ylabel("퇴직률(%)")

fig.suptitle("HR 퇴직 현황 대시보드", fontsize=21, fontweight="bold")
plt.tight_layout()

# Streamlit 화면에 그래프 출력
st.pyplot(fig, width="stretch")
plt.close(fig)
