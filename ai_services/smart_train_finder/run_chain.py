from utils.session_helper import get_or_set_api_key
from ai_services.smart_train_finder.extractor_chain import Extract
from ai_services.smart_train_finder.train_search_chain import SearchTrain
from utils.custom_exception import IrisException
import streamlit as st
import sys

class RunChain:
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain1 = Extract(api_key=api_key).extract_features()
            chain2 = SearchTrain(api_key=api_key).search()
            final_chain = chain1 | chain2

            query = st.text_input("Tell where you want to go")
            if query:
                try:
                    res = final_chain.invoke({"query": query})
                    st.write(res)

                except Exception as e:
                    if "invalid_api_key" in str(e).lower():
                        st.error("Invalid Groq API Key. Please reset and try again.")
                        return 
                    else:
                        raise IrisException(e, sys)

        except Exception as e:
            raise IrisException(e, sys)

