import streamlit as st
from utils.session_helper import get_or_set_api_key
from ai_services.smart_station_assistant.station_info_extractor import ExtractStationInfo
from ai_services.travel_planner_assistant.travel_plan import TravelPlan
from utils.custom_exception import IrisException
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys

class RunTravelPlanChain :
    def __init__(self) -> None:
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            chain = TravelPlan(api_key=api_key).travel_plan_info()

            system_prompt = """
                You are SmartTrip Planner, an intelligent, knowledgeable and friendly Indian Railway Travel Assistant.
                You help users plan trips to any place in India. For each query, you provide:
                - A friendly introduction about the destination, including its history, best time to visit, and local vibe.
                - Recommendations for places to stay: budget hotels, homestays, or resorts, with general price ranges if possible.
                - A list of must-see attractions and activities near the destination, each explained in short, clear paragraphs.
                - If the user mentions the number of days, provide a structured day-by-day plan.
                - Clear guidance on how to reach the destination by train: direct trains (name and number if known), and if not available, practical connecting routes via major junctions or nearby railway stations.
                - Tips on how to reach local spots from the station (taxi, bus, auto, or on foot).
                - Useful advice on local food, safety, or cultural etiquette.
                Always respond in a friendly, conversational tone using short paragraphs, bullet points, or headings where helpful. 
                If you don't know any part of the information, politely let the user know and recommend they check official railway 
                sites or local tourism portals for the most accurate details.
                """

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
            raise IrisException(e, sys)
