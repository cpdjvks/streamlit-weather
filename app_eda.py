import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_eda_app() :
    st.subheader('데이터 분석')

    st.text('전체 데이터 프레임 확인하기')

    df = pd.read_csv('./data/weather')

    st.dataframe(df)