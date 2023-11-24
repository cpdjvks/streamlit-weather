import streamlit as st

def run_home_app():
    st.subheader('Home')
    st.text('2020년 전국 날씨를 분석하는 앱입니다.')
    
    st.text('평년기온, 최고기온, 최저기온, 강수량, 풍량 등을 분석합니다.')

    st.text('출처 : https://data.kma.go.kr/cmmn/main.do')
    
    img_url = 'https://yimgf-thinkzon.yesform.com/docimgs/public/1/28/27421/27420559.jpg'

    st.image(img_url)