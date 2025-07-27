import streamlit as st

st.title("Budgeting Dashboard")

account = st.selectbox("Choose an account", ["Monzo", "Cash"])
amount = st.number_input("Amount", step=0.01)
category = st.selectbox("Category", ["Groceries", "Salary", "Rent"])
submit = st.button("Add Transaction")

if submit:
    st.success(f"Logged {amount} to {category} in {account}")