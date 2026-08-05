import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False


# DataFrame 생성 (학생 성적 예제)
st.subheader('학생 성적 데이터')
data = pd.DataFrame({
    '이름': ['민수', '지연', '철수', '영희'],
    '수학': [88, 92, 75, 85],
    '영어': [76, 85, 90, 95],
    '과학': [90, 80, 70, 88]
})

st.dataframe(data, use_container_width=True)

# 과목별 평균 점수 시각화
avg_scores = data[['수학', '영어', '과학']].mean()

fig, ax = plt.subplots()
sns.barplot(x=avg_scores.index, y=avg_scores.values, ax=ax, palette="Set2")
ax.set_title("과목별 평균 점수")
ax.set_ylabel("평균 점수")
ax.set_xlabel("과목")
st.pyplot(fig)


# 라인그래프 DataFrame (월별 매출)
st.subheader('월별 매출 데이터')
data = pd.DataFrame({
    '월': ['1월','2월','3월','4월','5월','6월'],
    '매출액': [120, 135, 150, 160, 155, 170]
})

st.dataframe(data, use_container_width=True)

# 라인그래프
fig, ax = plt.subplots()
ax.plot(data['월'], data['매출액'], marker='o', linestyle='-', color='blue')
ax.set_title("월별 매출 추이")
ax.set_ylabel("매출액 (단위: 만원)")
ax.set_xlabel("월")

st.pyplot(fig)

