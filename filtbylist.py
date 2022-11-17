import streamlit as st
import pandas as pd

st.title('Streamlit - Filter by sex')

data_url = 'dataset.csv'

@st.cache
def load_data(): 
    data = pd.read_csv(data_url)
    return data

@st.cache
def load_data_bysex(sex): 
    data = pd.read_csv(data_url)
    filtered = data[data['sex']==sex]
    return filtered

data = load_data()
selectbox = st.selectbox('Select sex', data['sex'].unique())
bttnfilter = st.button('Filter by sex')

if bttnfilter:
    filtered = load_data_bysex(selectbox)
    countrows = filtered.shape[0]
    st.write(f'Total items: {countrows}')

    st.dataframe(filtered)