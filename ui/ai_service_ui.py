import streamlit as st
from scripts.feedback.review_ui import Feedback
from utils.load_yaml import load_yaml_file
from ai_services.smart_train_finder.run_chain import RunChain
from ai_services.smart_train_assistant.run_info_chain import RunInfoChain
from utils.custom_exception import IrisException
from utils.session_helper import get_or_set_api_key, reset_api_key 
import sys

class AiService:
    def __init__(self) -> None:
        try:
            with st.sidebar:
                st.subheader("🤖 RAIL AI Service Panel")
                api_key = get_or_set_api_key()

                if st.button("🔄 Reset API Key"):
                    reset_api_key()

                options = load_yaml_file("config.yaml")
                menu_options = options["ai_services"]
                option = st.selectbox("Select service", menu_options)

            if option == menu_options[1]:
                if api_key:
                    RunChain() 
                else:
                    st.error("Please enter you API key")
            elif option == menu_options[2]:
                if api_key:
                    RunInfoChain()
                else:
                    st.error("Please enter you API key")
            
            Feedback()

        except Exception as e:
            raise IrisException(e, sys)
