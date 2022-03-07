import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sb
from statsmodels.tsa.seasonal import seasonal_decompose

from global_variables import df

def plot_line_market(df, option):
    #df_month = df.resample('M').mean()[option]
    df_new = df[option]
    fig, ax = plt.subplots()
    plt.plot(df_new.index, df_new, label=option)
    plt.show()
    plt.title('Line Chart')
    plt.xlabel('Date')
    plt.ylabel('USD per tonne of carbon dioxide')
    st.pyplot(fig)

def plot_dec_market(df, option, model, component):
    df1 = df.loc[:, df.columns == option]
    df1 = df1.dropna()
    df1 = df1.asfreq('D')
    df1 = df1.interpolate()
    decomposed = seasonal_decompose(df1, extrapolate_trend='freq', model = model)
    if component == 'Trend':
        fig1, ax1 = plt.subplots()
        decomposed.trend.plot()
        plt.show()
        plt.title('Trend')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig1)

    elif component == 'Seasonal':
        fig2, ax = plt.subplots()
        decomposed.seasonal.plot()
        plt.show()
        plt.title('Seasonal')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig2)

    else:
        fig3, ax = plt.subplots()
        decomposed.resid.plot()
        plt.show()
        plt.title('Residuals')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig3)

def diffed_df(df, option, shift):
    df1 = df.loc[:, df.columns == option]
    df1['Shifted'] = df[option].diff(periods=shift)
    df1.drop([option], axis = 1, inplace = True)
    return df1   

def plot_line_diff(df, shift):
    fig1, ax1 = plt.subplots()
    plt.plot(df.index, df)
    plt.show()
    plt.title('Line Chart with Order ' + str(shift) + ' Differencing')
    plt.xlabel('Date')
    plt.ylabel('USD per tonne of carbon dioxide')
    st.pyplot(fig1) 

def plot_dec_diff(df, option, model, shift, component):
    df1 = df.loc[:, df.columns == option]
    df1 = df.dropna()
    df1 = df1.asfreq('D')
    df1 = df1.interpolate()
    decomposed = seasonal_decompose(df1, extrapolate_trend='freq', model=model)
    decomposed.seasonal.plot()
    if component == 'Trend':
        fig1, ax1 = plt.subplots()
        decomposed.trend.plot()
        plt.show()
        plt.title('Trend with Order ' + str(shift) + ' Differencing')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig1)

    elif component == 'Seasonal':
        fig2, ax = plt.subplots()
        decomposed.seasonal.plot()
        plt.show()
        plt.title('Seasonal with Order' + str(shift) + ' Differencing')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig2)

    else:
        fig3, ax = plt.subplots()
        decomposed.resid.plot()
        plt.show()
        plt.title('Residuals with Order ' + str(shift) + ' Differencing')
        plt.xlabel('Date')
        plt.ylabel('USD per tonne of carbon dioxide')
        st.pyplot(fig3)

def app():
    with st.sidebar.container():
        option = st.selectbox('Choose Market to view', df.columns.tolist())
        shift = st.number_input('Difference', min_value = 1, step = 1)
        model = st.selectbox('Decompostion Model', ['Additive', 'Multiplicative'])
        component = st.selectbox('View', ['Trend', 'Seasonal', 'Residual'])
       
    with st.container():
        st.subheader( option + ' Market Decomposition with ' + ' ' + model + ' Model')
        df_diffed = diffed_df(df, option, shift)
        col1, col2 = st.columns(2)
        with col1:
            plot_line_market(df, option)
            plot_dec_market(df, option, model.lower(), component)
        with col2:
            plot_line_diff(df_diffed, shift)
            if model == 'Additive':
                plot_dec_diff(df_diffed, option, model.lower(), shift, component)
            



