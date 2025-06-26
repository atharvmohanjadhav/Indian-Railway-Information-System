import streamlit as st
from scripts.feedback.review_ui import Feedback

class AiService:
    def __init__(self) -> None:
        with st.sidebar:
            st.subheader("🤖 AI StudyMate Panel")
            ai_task = st.radio("Choose AI Tool", ["Notes Generator", "Quiz Maker", "Mind Map", "Syllabus Navigator"])
            user_input = st.text_area("Enter your topic/query")
            if st.button("Run AI"):
                st.success(f"Running: {ai_task} for topic '{user_input}'")

        st.markdown("## 🤖 Welcome to AI StudyMate")
        st.write("""
            Use this panel to interact with AI-powered learning tools:
            - ✍️ **Notes Generator**
            - 🧠 **Mind Map Visualizer**
            - 📚 **Syllabus Navigator**
            - ❓ **Quiz Generator**

            Each tool helps personalize and speed up your learning!
    """)
        Feedback()
        