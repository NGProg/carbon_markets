import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from global_variables import df

def plot_line_market(df, option):
    df_month = df.resample('M').mean()[option]
    fig, ax = plt.subplots()
    plt.plot(df_month.index, df_month, label=option)
    plt.show()
    plt.title('Chart of ' + option + ' Market')
    plt.xlabel('Date')
    plt.ylabel('USD per tonne of carbon dioxide')
    st.pyplot(fig)

def plot_dist_market(df, option):
    fig1, ax1 = plt.subplots()
    sb.distplot(df[option])
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

def plot_dist_diff(df, option, shift):
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
            plot_dist_market(df, option)
        with col2:
            plot_line_diff(df_diffed, option, shift)
            plot_dist_diff(df_diffed, option, shift)
            



