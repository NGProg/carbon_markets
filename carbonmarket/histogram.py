import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from global_variables import data as df
#df_month = df.resample('M')

def app():
    with st.sidebar.container():
        option = st.selectbox('Choose Market to view', df.columns.tolist())
    with st.container():
        df_month = df.resample('M').mean()[option]
        fig, ax = plt.subplots()
        plt.plot(df_month.index, df_month, label=option)
        plt.legend()
        plt.show()
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig)

        fig1, ax1= plt.subplots()
        sb.histplot(df_month)
        #plt.legend()
        plt.show()
        #plt.xlabel('Date')
        #plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig1)


