import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import date

from global_variables import data as df

PERIODS = {
    "Day": df,
    "Week": df.resample('W').mean(),
    "Month": df.resample('M').mean(),
    "Year": df.resample('Y').mean(),
}

def app():
    with st.sidebar.container():
        with st.expander('Choose Market(s) to Plot'):
            markets_options = st.multiselect('', df.columns.tolist(), df.columns.tolist())
        
        period_option = st.selectbox('Resample  By', ('Day', 'Week', 'Month', 'Year'), index = 2)
        period = PERIODS[period_option]
        markets = period[markets_options]

        time_period = st.sidebar.slider(
     "Choose time period to display on chart:",
     value=(date(2005, 1, 1), date(2022, 12, 31)))
        st.sidebar.write("Time period:", time_period)
    
    with st.container():
        st.header('Line graphs of Markets')
        fig, ax = plt.subplots()
        for col in markets.columns:
            if not col == 'markets.index':
                plt.plot(markets.index, markets[col], label=col)

        plt.legend(bbox_to_anchor=(1.01, 1))
        plt.show()
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig)

