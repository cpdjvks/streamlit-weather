import streamlit as st
import joblib
import numpy as np

def run_ml_app() :
    st.subheader('평년기온 예측')

    regressor = joblib.load('./model/regressor2.pkl')

    high = st.number_input('최고기온 입력', 10, 30)

    low = st.number_input('최저기온 입력', 0, 20)

    rain = st.number_input('강수량 입력', 0, 10)

    wind = st.number_input('풍량 입력', 0, 10)

    if st.button('평년기온 예측') :
        new_data = np.array([high, low, rain, wind])
        print(new_data)
        new_data = new_data.reshape(1, 4)
        y_pred = regressor.predict(new_data)
        avg = y_pred[0]
        if avg <= 0 :
            st.text('평년기온을 예측하기 어렵습니다.')
        else :
            st.text('평년기온은 섭씨 {}도 입니다.'.format(avg))

    else :
        st.text('')