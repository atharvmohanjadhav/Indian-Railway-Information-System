from scripts.feedback.review import get_feedback
import streamlit as st
from utils.custom_exception import IrisException
import sys

class Feedback:
    
    def __init__(self):
        try:
            text = st.sidebar.text_area("Give your feedback")
            if st.sidebar.button("Feedback"):
                res = get_feedback(text=text)
                st.sidebar.success(res)
        except Exception as e:
            st.error("Oops! Some error occured...")
            raise IrisException(e,sys)