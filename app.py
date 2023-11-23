import streamlit as st

from app_home import run_home_app
from app_eda import run_eda_app


def main() :
    st.title('2020년 전국 날씨')

    menu = ['Home', 'eda']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_eda_app()
    

if __name__ == '__main__' :
    main()