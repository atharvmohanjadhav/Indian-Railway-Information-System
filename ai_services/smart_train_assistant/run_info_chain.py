import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.smart_train_assistant.info_extractor_chain import ExtractInfo
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys

class RunInfoChain:
    def __init__(self) -> None:
        try:
            
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            # ✅ Build your ExtractInfo chain (history-aware)
            chain = ExtractInfo(api_key=api_key).extract_info()

            # ✅ System instructions (ONLY here, not in the chain)
            system_prompt = """
                You are SmartTrain Info Chatbot, a helpful Railway AI Assistant.
                You answer ANY question about a specific train: history, route, fare, stops, punctuality, facilities, or anything else.
                Be clear, conversational, and helpful. If info is missing, politely suggest the user check official railway sources.
                """

            # ✅ Initialize chat history if not already present
            if "messages" not in st.session_state:
                st.session_state.messages = [SystemMessage(content=system_prompt)]

            # ✅ Display all past messages
            for msg in st.session_state.messages[1:]:  # skip SystemMessage
                role = "assistant" if isinstance(msg, AIMessage) else "user"
                with st.chat_message(role):
                    st.markdown(msg.content)

            # ✅ Get user input in chat
            user_query = st.chat_input("Ask me anything about your train!")

            if user_query:
                # Save user input
                st.session_state.messages.append(HumanMessage(content=user_query))
                with st.chat_message("user"):
                    st.markdown(user_query)

                try:
                    # Call the chain with full message history
                    result = chain.invoke(st.session_state.messages)

                    # Add assistant response
                    st.session_state.messages.append(AIMessage(content=result))

                    with st.chat_message("assistant"):
                        st.markdown(result)

                except Exception as e:
                    if "invalid_api_key" in str(e).lower():
                        st.error("Invalid Groq API Key. Please reset and try again.")
                        return
                    else:
                        raise IrisException(e, sys)

        except Exception as e:
            raise IrisException(e, sys)
