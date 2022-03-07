import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, kpss
import seaborn as sb
import io

from global_variables import df

def app():
    with st.sidebar.container():
        market = st.selectbox('Choose Market to view', df.columns.tolist())
        df_new = df[market].interpolate()
        df_new = df_new.dropna()
        df_new = df_new.sort_index()

    with st.container():
        st.header(f'{market} Market Stationarity Tests')
        col1, col2, col3 = st.columns(3)
        with col1:
            fig, ax = plt.subplots()
            plt.plot(df_new.resample('M').mean())
            plt.show()
            plt.title('Line Chart')
            plt.xlabel('Date')
            plt.ylabel('USD per tonne of carbon dioxide')
            st.pyplot(fig)

    with col2:
        st.subheader('Augmented Dickey-Fuller (ADF) Test')
        result = adfuller(df_new, autolag='AIC')
        st.write(f'ADF Statistic: {result[0]}')
        st.write(f'p-value: {result[1]}')
        st.write('Critial Values:')
        for key, value in result[4].items():
            st.write(f'   {key}: {value}')

    with col3:
        st.subheader('Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test')
        statistic, p_value, n_lags, critical_values = kpss(df_new)
        st.write(f'KPSS Statistic: {statistic}')
        st.write(f'p-value: {p_value}')
        st.write(f'num lags: {n_lags}')
        st.write('Critial Values:')
        for key, value in critical_values.items():
            st.write(f'   {key} : {value}')
        st.write(f'Result: The series is {"not " if p_value < 0.05 else ""}stationary')

            