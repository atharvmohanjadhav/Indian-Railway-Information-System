import streamlit as st
from scripts.feedback.review_ui import Feedback
from utils.load_yaml import load_yaml_file
from ai_services.smart_train_finder.run_chain import RunChain as RunTrainFinderChain
from ai_services.smart_train_assistant.run_info_chain import RunInfoChain as RunTrainInfoChain
from ai_services.smart_station_assistant.run_chain import RunStationInfoChain
from ai_services.travel_planner_assistant.run_travel_plan_chain import RunTravelPlanChain
from ai_services.RailSaarthi.run_faq_final_chain import RunFaqChain
from ai_services.ai_storyteller.story_agent import RunStoryTeller
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

            # ================== Attractive Cards CSS ==================
            st.markdown("""
                <style>
                .ai-card {
                    background: linear-gradient(135deg, #283c86, #45a247);
                    padding: 20px;
                    border-radius: 14px;
                    margin-bottom: 18px;
                    color: white;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                    transition: transform 0.2s ease-in-out;
                }
                .ai-card:hover {
                    transform: scale(1.02);
                    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
                }
                .ai-title {
                    font-size: 20px;
                    font-weight: bold;
                    margin-bottom: 8px;
                }
                .ai-desc {
                    font-size: 15px;
                    line-height: 1.5;
                }
                </style>
            """, unsafe_allow_html=True)

            # ================== Landing Page (when select is chosen) ==================
            if option == menu_options[0]:  
                st.subheader("✨ Explore Our AI-Powered Services")

                ai_services = [
                    ("🚂 SmartTrain Finder", 
                     "Find detailed information about trains, their routes, and connections. "
                     "Helps you locate the best train for your journey with minimal input."),

                    ("🧑‍💻 SmartTrain Assistant", 
                     "Ask any train-related questions and get instant answers powered by AI. "
                     "Great for real-time travel help."),

                    ("🚉 SmartStation Assistant", 
                     "Get station-specific details, nearby facilities, and important info to make your travel smoother."),

                    ("🗺️ Travel Planner Assistant", 
                     "Plan your trip smartly with AI. Enter your origin, destination, and date, "
                     "and get a personalized travel plan instantly."),

                    ("❓ RailSaarthi: Smart FAQ Assistant", 
                     "Your railway FAQ companion. Quickly get answers to common queries about trains, booking, refunds, and more."),

                    ("📖 StoryBuddy", 
                     "Take a break from travel planning and enjoy AI-generated short stories based on your mood and preferences.")
                ]

                for title, desc in ai_services:
                    st.markdown(f"""
                        <div class="ai-card">
                            <div class="ai-title">{title}</div>
                            <div class="ai-desc">{desc}</div>
                        </div>
                    """, unsafe_allow_html=True)

            # ================== Run Selected Services ==================
            elif option == menu_options[1]:
                if api_key: RunTrainFinderChain()
                else: st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[2]:
                if api_key: RunTrainInfoChain()
                else: st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[3]:
                if api_key: RunStationInfoChain()
                else: st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[4]:
                if api_key: RunTravelPlanChain()
                else: st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[5]:
                if api_key: RunFaqChain()
                else: st.warning(" ⚠️ Please enter your API key")
            elif option == menu_options[6]:
                if api_key: RunStoryTeller()
                else: st.warning(" ⚠️ Please enter your API key")

            Feedback()

        except Exception as e:
            raise IrisException(e, sys)
