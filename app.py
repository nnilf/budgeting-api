import streamlit as st
import requests

st.set_page_config(page_title="API Tester", layout="centered")

st.title("🌐 FastAPI Backend Tester")

# Backend base URL
BASE_URL = st.text_input("Backend Base URL", "http://127.0.0.1:8000")

st.header("🔍 GET Request Example")

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

st.header("📤 POST Request Example")

post_route = st.text_input("POST Route (e.g. /items)", "/items?item=apple")

# Example JSON payload
default_payload = {
    "from_account": "12345",
    "to_account": "67890",
    "amount": 100.00,
    "description": "Example transfer"
}


if st.button("Send POST Request"):
    try:
        response = requests.post(f"{BASE_URL}{post_route}")
        st.subheader("Response")
        st.json(response.json())
    except Exception as e:
        st.error(f"Error: {e}")