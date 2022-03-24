import streamlit as st
num = st.slider("choose your number",1,100)
st.write('squre of ', num, 'is', num**2)