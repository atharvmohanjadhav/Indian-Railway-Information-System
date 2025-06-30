import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.smart_station_assistant.station_info_extractor import ExtractStationInfo
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys

class RunStationInfoChain:
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain = ExtractStationInfo(api_key=api_key).extract_station_info()

            system_prompt = """
                You are SmartStation Assistant, a knowledgeable and friendly Railway AI helper.
                You answer ANY question related to an Indian railway station — including its history, location, number of platforms, 
                major trains, available facilities, nearby places, accessibility, or any unique features.
                Always respond clearly, conversationally, and with helpful detail. When appropriate, use structured responses 
                or short lists, but keep the tone human-like and easy to understand.
                If you don't know something, politely suggest the user check the official Indian Railways portal or ask at the station help desk.
            """

            if "station_chat_messages" not in st.session_state:
                st.session_state.station_chat_messages = [SystemMessage(content=system_prompt)]

            for msg in st.session_state.station_chat_messages[1:]:
                role = "assistant" if isinstance(msg, AIMessage) else "user"
                with st.chat_message(role):
                    st.markdown(msg.content)

            user_query = st.chat_input("Ask me anything about your station!")

            if user_query:
                st.session_state.station_chat_messages.append(HumanMessage(content=user_query))
                with st.chat_message("user"):
                    st.markdown(user_query)

                try:
                    result = chain.invoke(st.session_state.station_chat_messages)
                    st.session_state.station_chat_messages.append(AIMessage(content=result))

                    with st.chat_message("assistant"):
                        st.markdown(result)

                except Exception as e:
                    if "invalid_api_key" in str(e).lower():
                        st.error("Invalid Groq API Key. Please reset and try again.")
                        return
                    else:
                        raise IrisException(e, sys)

            # Optional reset button
            # if st.button("🔄 New Conversation"):
            #     st.session_state.station_chat_messages = [SystemMessage(content=system_prompt)]

        except Exception as e:
            raise IrisException(e, sys)
