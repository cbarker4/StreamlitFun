import streamlit as st
import pandas as pd
import numpy as np 

st.write("""
streamlit is goated
""")
df = pd.read_csv('./data.csv')
st.dataframe(df)


sample_df = pd.DataFrame(
    np.random.randn(20,3)
    ,columns=['a','b','c']
)

st.line_chart(sample_df)


x = st.slider('x')
st.write(x*3)