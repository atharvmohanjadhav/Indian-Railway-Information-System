import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.smart_station_assistant.station_info_extractor import ExtractStationInfo
from ai_services.travel_planner_assistant.travel_plan import TravelPlan
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys
from utils.prompt_templates import travel_planner_assistant_prompt

class RunTravelPlanChain :
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain = TravelPlan(api_key=api_key).travel_plan_info()

            system_prompt = travel_planner_assistant_prompt

            if "travel_plan_messages" not in st.session_state:
                st.session_state.travel_plan_messages = [SystemMessage(content=system_prompt)]

            for msg in st.session_state.travel_plan_messages[1:]:
                role = "assistant" if isinstance(msg, AIMessage) else "user"
                with st.chat_message(role):
                    st.markdown(msg.content)

            user_query = st.chat_input("Where would you like to plan your trip? Ask me anything about your destination!")

            if user_query:
                st.session_state.travel_plan_messages.append(HumanMessage(content=user_query))
                with st.chat_message("user"):
                    st.markdown(user_query)

                try:
                    result = chain.invoke(st.session_state.travel_plan_messages)
                    st.session_state.travel_plan_messages.append(AIMessage(content=result))

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
