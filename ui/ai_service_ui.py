import streamlit as st
from scripts.feedback.review_ui import Feedback
from utils.load_yaml import load_yaml_file
from ai_services.smart_train_finder.run_chain import RunChain as RunTrainFinderChain
from ai_services.smart_train_assistant.run_info_chain import RunInfoChain as RunTrainInfoChain
from ai_services.smart_station_assistant.run_chain import RunStationInfoChain
from ai_services.travel_planner_assistant.run_travel_plan_chain import RunTravelPlanChain
from ai_services.RailSaarthi.run_faq_final_chain import RunFaqChain
from utils.custom_exception import IrisException
from utils.session_helper import get_or_set_api_key, reset_api_key 
import sys

class AiService:
    def __init__(self) -> None:
        try:
            with st.sidebar:
                st.subheader("🤖 RAIL AI Service Panel")
                api_key = get_or_set_api_key()

                if st.button("🔄 Reset API Key"):
                    reset_api_key()

                options = load_yaml_file("config.yaml")
                menu_options = options["ai_services"]
                option = st.selectbox("Select service", menu_options)

                if "last_service" not in st.session_state:
                    st.session_state.last_service = None

                if option != st.session_state.last_service:
                    st.session_state.last_service = option
                    
                    st.session_state.pop("train_finder_chat_messages", None)
                    st.session_state.pop("train_info_chat_messages", None)
                    st.session_state.pop("station_chat_messages", None)
                    st.session_state.pop("travel_plan_messages", None)

            if option == menu_options[1]:
                if api_key:
                    RunTrainFinderChain()
                else:
                    st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[2]:
                if api_key:
                    RunTrainInfoChain()
                else:
                    st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[3]:
                if api_key:
                    RunStationInfoChain()
                else:
                    st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[4]:
                if api_key:
                    RunTravelPlanChain()
                else:
                    st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[5]:
                if api_key:
                    RunFaqChain()
                else:
                    st.warning(" ⚠️ Please enter your API key")

            Feedback()

        except Exception as e:
            st.error("Oops! Some error occured...")
            raise IrisException(e, sys)
