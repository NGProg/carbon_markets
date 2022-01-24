import streamlit as st
import pandas as pd
from datetime import datetime

@st.cache()
def load_market_data():
    data = pd.read_csv('carbonmarket/carbonmarket.csv', header=0, parse_dates=[1], index_col=1)
    del data['Unnamed: 0']
    data = data.dropna(how = 'all', axis = 1)
    data = data.sort_index()
    data = data.interpolate()
    data = data.dropna(how='all')
    data = data.sort_index()
    return data

df = load_market_data()

PERIODS = {
    "Day": df,
    "Week": df.resample('W').mean(),
    "Month": df.resample('M').mean(),
    "Year": df.resample('Y').mean(),
}

CORR_METHODS = {
    "Pearson": "pearson",
    "Kendall": "kendall",
    "Spearman": "spearman"
}

