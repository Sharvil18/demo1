import streamlit as st
@st.cache()
def calculate_emi(p,n,r):
  emi = p * (r/100) * ((1 + (r/100)**n) / ((1 + (r/100))**n - 1))
  return round(emi,3)

def calculate_outstanding_balance(p,n,r,m):
  balance = ((p*(1+(r/100))**n) - ((1+(r/100))**m)) / (((1+(r/100))**n)-1)
  return round(balance,3)

emi = ''
bal = ''
st.title('Improvided EMI calculator')
principal = st.slider('Principal',1000,1000000)
tenure = st.slider('Tenure', 1,30)
roi = st.slider('Rate of Interest',1.0,15.0)
m = st.slider('Period after which the outstanding loan balance is calculated',1,(tenure*12))
n = tenure * 12
r = roi / 12
if st.button('Calculate EMI'):
  emi = calculate_emi(principal,n,r)
if st.button('Calculate Outstanding Loan Balance'):
  bal = calculate_outstanding_balance(principal,n,r,m)
st.write('EMI = ',emi)
st.write('Outstanding Loan Balance = ',bal)