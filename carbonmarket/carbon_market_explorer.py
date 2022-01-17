import streamlit as st 
import pandas as pd

from global_variables import data
#import global_variables

import describe
import linegraphs
import histogram

PAGES = {
    "Data Description": describe,
    "Line Charts": linegraphs,
    "Histogram": histogram
}

st.title('Carbon Markets Explorer') 
st.subheader('Exploratory analysis of carbon markets') 
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

selection = st.sidebar.selectbox('Menu', list(PAGES.keys()))
st.sidebar.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
page = PAGES[selection]
with st.empty():
    page.app()
