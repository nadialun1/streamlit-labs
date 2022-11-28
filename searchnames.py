import streamlit as st
import pandas as pd

st.title('Streamlit - search name')
Data = 'dataset.csv'

@st.cache
def loaddata(name): 
    data = pd.read_csv(Data)
    filtered_data = data[data['name'].str.contains(name)]
    return filtered_data


myname = st.text_input('Name :')
if (myname): 
    filterbyname = loaddata(myname)
    count = filterbyname.shape[0]
    st.write(f'Total names: {count}')
    st.dataframe(filterbyname)