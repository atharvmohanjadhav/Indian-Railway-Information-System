from utils.session_helper import get_or_set_api_key
from ai_services.smart_train_finder.extractor_chain import Extract
from ai_services.smart_train_finder.train_search_chain import SearchTrain
from ai_services.smart_train_finder.translate_chain import get_translation_chain
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

            # Init chains
            chain1 = Extract(api_key=api_key).extract_features()
            chain2 = SearchTrain(api_key=api_key).search()
            translation_chain = get_translation_chain(api_key)
            base_chain = chain1 | chain2

            # Initialize session state safely
            if "train_response" not in st.session_state:
                st.session_state.train_response = ""
            if "last_query" not in st.session_state:
                st.session_state.last_query = ""
            if "language" not in st.session_state:
                st.session_state.language = "None"

            # User input box (same box for new query and update)
            query = st.text_input(
                "Where do you want to go?",
                value=st.session_state.last_query,
                placeholder="e.g. Mumbai to Pune tomorrow evening"
            )

            if query:
                # If query changed, re-invoke
                if query != st.session_state.last_query:
                    try:
                        res = base_chain.invoke({"query": query})
                        st.session_state.train_response = res
                        st.session_state.last_query = query
                        st.session_state.language = "None"
                    except Exception as e:
                        if "invalid_api_key" in str(e).lower():
                            st.error("Invalid Groq API Key. Please reset and try again.")
                            return
                        else:
                            raise IrisException(e, sys)

            # Show original response if exists
            if st.session_state.train_response:
                st.write(st.session_state.train_response)

                # Translation selectbox
                selected_language = st.selectbox(
                    "🌐 Translate response to:",
                    ["None", "Hindi", "Marathi"],
                    index=["None", "Hindi", "Marathi"].index(st.session_state.language)
                )
                st.session_state.language = selected_language

                if selected_language != "None":
                    translated = translation_chain.invoke({
                        "text": st.session_state.train_response,
                        "language": selected_language
                    })
                    st.write(f"### 🌐 Translated ({selected_language}):")
                    st.write(translated)

        except Exception as e:
            raise IrisException(e, sys)
