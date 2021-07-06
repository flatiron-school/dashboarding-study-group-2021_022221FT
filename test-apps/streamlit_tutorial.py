import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import fsds as fs
st.title('Our First Streamlit App')
df = fs.datasets.load_mod1_proj(read_csv_kwds={'na_values':'?'})
df.dropna(inplace=True)
st.write('Anything that is shown in a line in a streamlit app will be displayed.')
st.write(df.head())
st.write(df.isna().sum())
st.write(df.info())

map_df = df[['lat','long','price']]
map_df.rename({"long":'lon'},axis=1,inplace=True)

if st.checkbox('Show map'):
    st.map(map_df)