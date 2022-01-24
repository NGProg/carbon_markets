import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from global_variables import df
from global_variables import CORR_METHODS

def market_heatmap(method):
    fig, ax = plt.subplots()
    sb.heatmap(df.corr(method = method))
    plt.show()
    st.pyplot(fig)

def app():
    with st.sidebar.container():
        method = st.sidebar.selectbox('Choose correlation Method', list(CORR_METHODS.keys()))
        selection = CORR_METHODS[method]
    with st.container():
        st.subheader('Markets Correlation with ' + method + ' Method')
        st.write(df.corr(method = selection))
        st.write('')
        st.subheader('Markets Correlation Heatmap with ' + method + ' Method')
        market_heatmap(selection)
        

        