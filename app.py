import streamlit as st

st.set_page_config(
    page_title="첫 번째 Streamlit 앱",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 첫 번째 Streamlit 앱")
st.write("Streamlit을 이용해 만든 첫 번째 웹 애플리케이션입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("인사하기"):
    if name:
        st.success(f"{name}님, Streamlit 실습을 시작합니다!")
    else:
        st.warning("이름을 먼저 입력해 주세요.")