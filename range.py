import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')
DataUrl = 'dataset.csv'

@st.cache

def loadData(startid, endid): 
    data = pd.read_csv(DataUrl)
    filterdata = data[(data['index'] >= startid) & (data['index'] <= endid)]
    return filterdata

startid = st.text_input('Start index:')
endid = st.text_input('End index:')
btn = st.button('Search by range')

if (btn): 
    filtered = loadData(int(startid), int(endid))
    count = filtered.shape[0]
    st.write(f'Total: {count}')

    st.dataframe(filtered)