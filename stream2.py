import streamlit as st
import pandas as pd


df = pd.read_csv('dataset.csv')
st.dataframe(df)