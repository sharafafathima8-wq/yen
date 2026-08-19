import streamlit as st
st.title('calculator app using streamlit')
st.write('---------------------------------------')

num1=st.number_input(label='enter the first number')
num2=st.number_input(label='enter the second number')
operation=st.radio('select the operation',('add','subtract','multiply','divide'))

ans=0
def calculate():
    if operation=='add':
        ans=num1+num2
    elif operation=='subtract':
        ans=num1-num2
    elif operation=='multiply':
        ans=num1*num2
    elif operation=='divide':
        ans=num1/num2
    else:
        ans='not defined'
    st.success(f'answer={ans}')
if st.button('calculate result'):
    calculate()
