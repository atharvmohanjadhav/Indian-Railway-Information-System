import streamlit as st
from scripts.feedback.review_ui import Feedback
from utils.load_yaml import load_yaml_file
from ai_services.train_query_agent.run_chain import RunChain


class AiService:
    def __init__(self) -> None:
        with st.sidebar:
            st.subheader("🚂 Railway Service Panel")
            options = load_yaml_file("config.yaml")
            menu_options = options["ai_services"]
            option = st.selectbox("Select service", menu_options)
        if option == menu_options[1]:
            RunChain()

        Feedback()
        