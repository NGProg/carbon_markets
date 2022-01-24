import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from statsmodels.tsa.seasonal import seasonal_decompose

from global_variables import df

def plot_line_market(df, option):
    #df_month = df.resample('M').mean()[option]
    df_new = df[option]
    fig, ax = plt.subplots()
    plt.plot(df_new.index, df_new, label=option)
    plt.show()
    plt.title('Chart of ' + option + ' Market')
    plt.xlabel('Date')
    plt.ylabel('USD per tonne of carbon dioxide')
    st.pyplot(fig)

def plot_dec_market(df, option):
    df1 = df.dropna()
    df1 = df1.asfreq('D')
    fig1, ax1 = plt.subplots()
    sb.distplot(df[option])
    #decomposed = seasonal_decompose(df1, extrapolate_trend='freq', model='additive')
    #decomposed.plot()
    plt.show()
    plt.title('Distribution of ' + option + ' Market')
    plt.xlabel('USD per tonne of carbon dioxide')
    plt.ylabel('')
    st.pyplot(fig1)

def diffed_df(df, option, shift):
    df1 = df.loc[:, df.columns == option]
    df1['Shifted'] = df[option].diff(periods=shift)
    df1.drop([option], axis = 1, inplace = True)
    return df1   

def plot_line_diff(df, option, shift):
    fig1, ax1 = plt.subplots()
    plt.plot(df.index, df)
    plt.show()
    plt.title('Chart of ' + option + ' Market with Order ' + str(shift) + ' Differencing')
    plt.xlabel('Date')
    plt.ylabel('USD per tonne of carbon dioxide')
    st.pyplot(fig1)  

def plot_dec_diff(df, option, shift):
    fig1, ax1 = plt.subplots()
    sb.distplot(df)
    plt.show()
    plt.title('Distribution of ' + option + ' Market with Order ' + str(shift) + ' Differencing')
    plt.xlabel('USD per tonne of carbon dioxide')
    plt.ylabel('')
    st.pyplot(fig1)

def app():
    with st.sidebar.container():
        option = st.selectbox('Choose Market to view', df.columns.tolist())
        shift = st.number_input('Difference', min_value = 1, step = 1)
       
    with st.container():
        df_diffed = diffed_df(df, option, shift)
        col1, col2 = st.columns(2)
        with col1:
            plot_line_market(df, option)
            plot_dec_market(df, option)
        with col2:
            plot_line_diff(df_diffed, option, shift)
            plot_dec_diff(df_diffed, option, shift)
            



