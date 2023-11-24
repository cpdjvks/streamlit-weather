import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_eda_app() :

    st.subheader('데이터 분석')

    tab1, tab2, tab3 = st.tabs(['전체 데이터 프레임 확인하기' , '기초통계데이터 확인하기', '최대 / 최소 데이터 확인하기'])

    with tab1:
        df = pd.read_csv('./data/weather.csv')

        st.area_chart(df[['avg', 'high', 'low', 'rain', 'wind']])

        if st.checkbox('자세히 보기') :
            st.dataframe(df)
        else :
            st.text('')

    with tab2:
        st.dataframe(df.describe())

    with tab3:
        column_list = df.columns[1: ]

        selected_column = st.selectbox('컬럼을 선택하세요', column_list)

        st.text(selected_column + ' 컬럼의 최소값')
        st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), ])

        st.text(selected_column + ' 컬럼의 최대값')
        st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), ])

        st.text(selected_column + ' 컬럼의 히스토그램')
        fig1 = plt.figure()
        df[selected_column].hist(bins = 20)
        st.pyplot(fig1)