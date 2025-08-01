import streamlit as st
import requests
from pydantic import BaseModel

class Account(BaseModel):
    AccountId : int | None = None
    Balance : float = 0.0
    Name : str
    Password : str

st.set_page_config(page_title="API Tester", layout="centered")

st.title("Budgeting API tester")

# Backend base URL
BASE_URL = st.text_input("Backend Base URL", "http://127.0.0.1:8000")

st.header("GET Request Example")

get_route = st.text_input("GET Route (e.g. /items/1)", "/items/1")

if st.button("Send GET Request"):
    try:
        response = requests.get(f"{BASE_URL}{get_route}")
        print(response)
        st.subheader("Response")
        st.code(f"Status: {response.status_code}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

# Divider
st.markdown("---")

st.header("POST Request Example")

post_route = st.text_input("POST Route (e.g. /items)", "/items?item=apple")

if st.button("Send POST Request"):
    try:
        response = requests.post(f"{BASE_URL}{post_route}")
        st.subheader("Response")
        st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")


st.markdown("---")

st.header("Register/Login")

username = st.text_input("username")
password = st.text_input("password")

if st.button("Register"):
    try:
        account = Account(
            AccountId=None,
            Balance=0.0,
            Name=username,
            Password=password
        )
        response = requests.post(f"{BASE_URL}/register", json=account.model_dump())
        st.subheader("Response")
        st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Login"):
    try:
        account = Account(
            AccountId=None,
            Balance=0.0,
            Name=username,
            Password=password
        )
        response = requests.get(f"{BASE_URL}/login", json=account.model_dump())
        st.subheader("Response")
        st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")