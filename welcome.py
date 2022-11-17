import streamlit as st

def bienvenido(nombre):
    mensaje = 'bienvenido/a: ' + nombre
    return mensaje

myname = st.text_input('Nombre: ')

if (myname): 
    nmensaje = bienvenido(myname)
    st.write(f'mensaje: {myname}')