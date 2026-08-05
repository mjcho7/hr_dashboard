#심플 streamlit 웹 앱
import streamlit as st

# 타이틀 
st.title('타이틀')

# Header 
st.header('헤더')

# subheader
st.subheader('서브해더')

# 캡션 
st.caption('캡션')

# 이모지 
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title(':100: 스마일')

# 코드 표시
python_code = '''
    print('hi python!')
'''
st.code(python_code, language="python")

# 일반 텍스트
st.text('가을 하늘입니다.')

# 마크다운 문법 지원
st.markdown('**마크다운**을 지원합니다.')