import streamlit as st
import pandas as pd

st.title("영화 예매 도우미")

# 버튼
if st.button("오늘의 추천 영화 보기"):
    st.success("오늘은 '인터스텔라' 어때? 🎬")

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')

# 다운로드 버튼: 상영 시간표 샘플
showtimes = pd.DataFrame({
    "영화": ["인터스텔라", "듄: 파트2", "라라랜드", "기생충"],
    "상영관": ["A관", "B관", "C관", "A관"],
    "시작시간": ["14:00", "16:30", "18:10", "20:00"]
})
st.download_button(
    label="시간표 CSV 다운로드",
    data=showtimes.to_csv(index=False),
    file_name="showtimes_sample.csv",
    mime="text/csv"
)

# 체크박스
is_student = st.checkbox("학생이야?")
if is_student:
    st.info("학생 할인 적용 가능!")

# 라디오
format_choice = st.radio(
    "상영 포맷을 골라줘",
    ("2D", "IMAX", "4DX")
)
st.write(f"선택한 포맷: {format_choice}")

# 셀렉트박스
movie = st.selectbox(
    "보고 싶은 영화를 선택해줘",
    ("인터스텔라", "듄: 파트2", "라라랜드", "기생충"),
    index=1
)
st.write(f"선택한 영화: {movie}")

# 텍스트 입력
theater = st.text_input(
    "가고 싶은 극장명을 입력해줘",
    placeholder="예) 강남 메가박스"
)
st.write(f"극장: {theater if theater else '아직미정'}")
