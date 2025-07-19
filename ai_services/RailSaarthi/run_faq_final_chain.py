import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.RailSaarthi.run_faq_chain import FaqChain
from ai_services.smart_train_finder.translate_chain import get_translation_chain
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage
import sys

class RunFaqChain:
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain = FaqChain(api_key=api_key).get_data()
            translation_chain = get_translation_chain(api_key)

            if "last_faq_query" not in st.session_state:
                st.session_state.last_faq_query = ""
            if "last_faq_response" not in st.session_state:
                st.session_state.last_faq_response = ""

            with st.chat_message("assistant"):
                st.markdown("Hello! Ask me any railway question!")

            user_query = st.chat_input("Ask your railway question...")

            if user_query:
                with st.chat_message("user"):
                    st.markdown(user_query)
                try:
                    result = chain.invoke({"query": user_query})
                    if isinstance(result, dict) and "result" in result:
                        answer = result["result"]
                    else:
                        answer = str(result)

                    st.session_state.last_faq_query = user_query
                    st.session_state.last_faq_response = answer
                except Exception as e:
                    if "invalid_api_key" in str(e).lower():
                        st.error("Invalid Groq API Key. Please reset and try again.")
                        return
                    else:
                        raise 

            if st.session_state.last_faq_response:
                with st.chat_message("assistant"):
                    st.markdown(st.session_state.last_faq_response)

                    selected_language = st.selectbox(
                        "🌐 Translate response to:",
                        ["None", "Hindi", "Marathi"],
                        key=f"translate_{st.session_state.last_faq_query[:5]}"
                    )

                    if selected_language != "None":
                        translated = translation_chain.invoke({
                            "text": st.session_state.last_faq_response,
                            "language": selected_language
                        })
                        st.write(f"### 🌐 Translated ({selected_language}):")
                        st.write(translated)

        except Exception as e:
            if "invalid_api_key" in str(e).lower():
                pass
            else:
                st.error("Oops! Some error occurred...")
                raise IrisException(e, sys)

        
