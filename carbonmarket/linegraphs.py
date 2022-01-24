import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

from global_variables import df
from global_variables import PERIODS


def app():
    with st.sidebar.container():
        with st.expander('Choose Market(s) to Plot'):
            markets_options = st.multiselect('', df.columns.tolist(), ['European Union'])
        
        period_option = st.selectbox('Resample  By', ('Day', 'Week', 'Month', 'Year'), index = 2)
        period = PERIODS[period_option]
        markets = period[markets_options]

        start, end = st.sidebar.slider("Choose time period to display on chart:", value=(0, len(markets)-1))
        st.sidebar.write("Start:", markets.index[start].date(), "End:", markets.index[end].date())
        markets = markets[start : end]
    
    with st.container():
        #st.header('Line graphs of Markets')
        fig, ax = plt.subplots()
        for col in markets.columns:
            if not col == 'markets.index':
                plt.plot(markets.index, markets[col], label=col)

        plt.legend(bbox_to_anchor=(1.01, 1))
        plt.show()
        plt.title('Line graphs of Markets')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig)

