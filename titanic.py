import streamlit as st
import pandas as pd
import datetime

titdat = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
dat_tit = pd.read_csv(titdat)

st.title('Titanic app')

sidebar = st.sidebar

sidebar.title('Acciones')
sidebar.write('You can add any element')

today = datetime.date.today()
t_date=sidebar.date_input('Current date',today)
st.success('Curren date: `%s`' %(t_date))

if sidebar.checkbox('Show Dataset?'):
    st.dataframe(dat_tit)


st.header('Clase:')
sle_class= sidebar.radio('Select Class:',dat_tit['class'].unique())


st.success(f'Selected Class: {sle_class}')

slec_sex = sidebar.selectbox('Select sex:', dat_tit['sex'].unique())
st.success(f'Sleccted Sex: {str(slec_sex).capitalize()}')





st.markdown('___')

optionals = sidebar.expander('Optional config',True)
fare_selec = optionals.slider(
    'Select the Fare:',
    min_value= float(dat_tit['fare'].min()),
    max_value= float(dat_tit['fare'].max())

)

subset_fare = dat_tit[(dat_tit['fare']>= fare_selec)]
st.write(f'Numero de registros sobre esta tarifa: {subset_fare.shape[0]}')
st.dataframe(subset_fare)