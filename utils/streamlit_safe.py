
import streamlit as st
from utils.custom_exception import IrisException
import sys

def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        if "invalid_api_key" in str(e).lower():
            st.error("Invalid API Key. Please check and reset.")
        elif "no healthy upstream" in str(e).lower():
            st.warning("Service temporarily unavailable. Please try again later.")
        else:
            st.error(f"Something went wrong: {e}")
        raise IrisException(e, sys)
