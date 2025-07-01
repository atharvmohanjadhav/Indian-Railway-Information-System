from scripts.feedback.review import get_feedback
import streamlit as st

class Feedback:
    
    def __init__(self):
        text = st.sidebar.text_area("Give your feedback")
        if st.sidebar.button("Feedback"):
            res = get_feedback(text=text)
            st.sidebar.success(res)