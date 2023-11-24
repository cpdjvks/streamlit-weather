import streamlit as st

from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app


def main() :
    st.title('2020년 전국 날씨')

    menu = ['Home', '데이터 분석', '평년기온 예측']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_eda_app()
    elif choice == menu[2] :
        run_ml_app()
    

if __name__ == '__main__' :
    main()