from ai_services.train_query_agent.extractor_chain import Extract
from ai_services.train_query_agent.train_search_chain import SearchTrain
from utils.custom_exception import IrisException
import os
import sys
import streamlit as st

class RunChain:
    def __init__(self) -> None:
        try:
            api_key = st.sidebar.text_input("Enter your Groq API_KEY")
            if api_key:

                chain1 = Extract(api_key=api_key).extract_features()
                chain2 = SearchTrain(api_key=api_key).search()

                final_chain = chain1 | chain2

                query = st.text_input("Enter your query")
                if query:
                    res = final_chain.invoke({"query":query})
                    st.write(res)
            # return res
        except Exception as e:
            raise IrisException(e,sys)
    

