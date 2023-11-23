import streamlit as st

def run_home_app():
    st.subheader('안녕하세요')
    st.text('2020년 전국 날씨를 분석하는 앱입니다')
    
    st.text('평년기온, 최고기온, 최저기온, 강수량, 풍량 등을 분석합니다.')
    
    img_url = 'https://cdn.issuenbiz.com/news/photo/202204/14078_14451_4450.png'

    st.image(img_url)