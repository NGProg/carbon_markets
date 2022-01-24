import streamlit as st 
st.set_page_config(layout="wide")
import pandas as pd

import describe
import linegraphs
import histogram
import correlation
import decomposition

PAGES = {
    "Data Description": describe,
    "Line Charts": linegraphs,
    "Histogram": histogram,
    "Correlation": correlation,
    "Decomposition": decomposition
}

st.title('Carbon Markets Explorer') 
st.subheader('Exploratory analysis of carbon markets') 
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

selection = st.sidebar.selectbox('Menu', list(PAGES.keys()))
st.sidebar.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
page = PAGES[selection]
with st.empty():
    page.app()
