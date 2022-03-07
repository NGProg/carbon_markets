import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from global_variables import df

def app():
    with st.sidebar.container():
        market = st.selectbox('Choose Market to view', df.columns.tolist())
        lags = st.number_input('Lags', min_value = 1, step = 1)
        df_new = df[market].interpolate()
        df_new = df_new.dropna()
        df_new = df_new.sort_index()
       
    with st.container():
        st.subheader( f'{market} Market Autocorrelation')
        df_market = df[market]
        df_market_shifted = df_market.diff(lags).dropna()
        col1, col2, col3 = st.columns(3)
        with col1:
            fig_original, ax = plt.subplots()
            plt.plot(df_new.resample('M').mean())
            plt.show()
            plt.title('Line Chart')
            plt.xlabel('Date')
            plt.ylabel('USD per tonne of carbon dioxide')
            st.pyplot(fig_original)

            fig_shifted, ax = plt.subplots()
            plt.plot(df_market_shifted)
            plt.show()
            plt.title('Differencing (Order = ' + str(lags) + ')')
            plt.xlabel('Date')
            plt.ylabel('USD per tonne of carbon dioxide')
            st.pyplot(fig_shifted)

        with col2:
            st.pyplot(plot_acf(df_market, alpha = 0.05))
            st.pyplot(plot_acf(df_market_shifted, alpha = 0.05))
    
        with col3:
            st.pyplot(plot_pacf(df_market, alpha = 0.05))
            st.pyplot(plot_pacf(df_market_shifted, alpha = 0.05))
          
            


