import streamlit as st
import pandas as pd
import numpy as np


st.title('판다스 데이터프레임 출력하기')

# DataFrame 생성
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': ["a", "b", "c", "d"],
})

# DataFrame
st.subheader('dataframe')
st.dataframe(df, use_container_width=True)

# 테이블
st.subheader('table')
st.table(df)

# # 메트릭
st.metric(label="미세먼지 (PM10)", value="45 ㎍/㎥", delta="-12 ㎍/㎥")
st.metric(label="습도", value="63%", delta="+4%")

# 컬럼 영역
col1, col2, col3 = st.columns(3)
col1.metric(label="방문자 수", value="12,400 명", delta="+320 명")
col2.metric(label="구독자 수", value="3,560 명", delta="+120 명")
col3.metric(label="이탈률", value="42%", delta="-2.5%")