import streamlit as st 
import pandas as pd

st.title('Streamlit con cache')
DataURL = 'dataset.csv'

@st.cache
def load_data(nrows): 
    data = pd.read_csv(DataURL, nrows = nrows)
    return data

data_load = st.text('Loading data...')

data = load_data(500)

st.dataframe(data)
