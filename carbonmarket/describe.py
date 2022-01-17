import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import io

from global_variables import data as df

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

def app():
    with st.container():
        st.header('Database Information')
        #st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        st.text(s)
        st.header('Markets Statistics')
        st.write(df.describe().T)