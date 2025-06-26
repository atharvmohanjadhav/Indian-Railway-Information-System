import streamlit as st
from ai_services.train_query_agent.run_chain import RunChain
from utils.custom_exception import IrisException
import os
import sys

class TrainAgent:
    def __init__(self) -> None:
        self.api = st.text_input("Enter you Groq API")
        