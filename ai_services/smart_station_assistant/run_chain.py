import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.smart_station_assistant.station_info_extractor import ExtractStationInfo
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys
from utils.prompt_templates import station_assistant_prompt

class RunStationInfoChain:
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain = ExtractStationInfo(api_key=api_key).extract_station_info()
            system_prompt = station_assistant_prompt

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

        except Exception as e:
            st.error("Oops! Some error occured...")
            raise IrisException(e, sys)
