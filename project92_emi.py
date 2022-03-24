import streamlit as st
@st.cache()
def calculate_emi(p,n,r):
  emi = p * (r/100) * ((1 + (r/100)**n) / ((1 + (r/100))**n - 1))
  return round(emi,3)

emi = ''
st.title('EMI Calculator App')
principal = st.slider('Principal',1000,1000000)
tenure = st.slider('Tenure',1,30)
roi = st.slider('Rate of Interest',1.0,15.0)
n = tenure * 12
r = roi / 12
if st.button('Calculate EMI'):
  emi = calculate_emi(principal,n,r)
st.write('EMI = ',emi)