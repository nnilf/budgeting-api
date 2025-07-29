import streamlit as st
import requests

st.title("Budgeting API")

account = st.selectbox("Choose an account", ["Monzo", "Cash"])
amount = st.number_input("Amount", step=0.01)
category = st.selectbox("Category", ["Groceries", "Salary", "Rent"])
submit = st.button("Add Transaction")

payload = {'account': account,
           'amount': amount,
           'category': category}

if submit:
    r = requests.get('http://127.0.0.1:8000/items/5?q=somequery')
    print(r.text)
    st.success(f"Logged {amount} to {category} in {account}")