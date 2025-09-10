import streamlit as st
from utils.load_yaml import load_yaml_file

from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare_ui import TrainFareUI
from src.seats.seat_availability_ui import SeatAvailabilityUI

from src.trains.special_trains.special_trains_info_ui import SpeacialTrainsUI
from src.trains.premium_trains.premium_trains_info_ui import PremiumTrainsUI
from src.trains.rajdhani_trains.rajdhani_trains_info_ui import RajdhaniTrainsUI
from src.trains.super_fast_trains.superfast_trains_info_ui import SuperfastTrainsUI

from scripts.station_code.station_to_code_ui import StationToCodeUI
from scripts.train_no_to_name.train_numer_to_name_ui import TrainNoToNameUI

from scripts.feedback.review_ui import Feedback
from utils.custom_exception import IrisException
import sys


class TrainService:
    def __init__(self) -> None:
        try:
            options = load_yaml_file("config.yaml")
            menu_options = options["menu_options"]

            with st.sidebar:
                st.subheader("🚂 Railway Service Panel")
                option = st.selectbox("Select service", menu_options)

            st.markdown("""
                <style>
                .service-card {
                    background: linear-gradient(135deg, #283c86, #45a247);
                    padding: 20px;
                    border-radius: 14px;
                    margin-bottom: 18px;
                    color: white;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                    transition: transform 0.2s ease-in-out;
                }
                .service-card:hover {
                    transform: scale(1.02);
                    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
                }
                .service-title {
                    font-size: 20px;
                    font-weight: bold;
                    margin-bottom: 8px;
                }
                .service-desc {
                    font-size: 15px;
                    line-height: 1.5;
                }
                </style>
            """, unsafe_allow_html=True)

            if option == menu_options[0]:  
                st.subheader("Available Railway Services")

                services = [
                    ("📍 Station Info", 
                    "Get details about a railway station including station code, full name, and location. "
                    "Perfect for quickly finding the code of your boarding or destination station."),

                    ("🕒 Train Schedule", 
                    "View detailed schedules of trains including arrival, departure, halt duration, and running days. "
                    "Helps you plan your journey and check train timings in advance."),

                    ("🚉 All Trains from Station", 
                    "Find all trains that start, stop, or pass through a given station. "
                    "Helpful if you only know your starting point but want to explore all available trains from there."),

                    ("💰 Train Fares", 
                    "Check fare details for different classes (Sleeper, 3A, 2A, 1A, Chair Car, etc.) on specific train routes. "
                    "You can compare prices before booking tickets."),

                    ("🎟️ Seat Availability", 
                    "Check real-time seat availability for trains across different classes. "
                    "Helps you decide whether to book immediately or look for alternate options.")
                ]

                for title, desc in services:
                    st.markdown(f"""
                        <div class="service-card">
                            <div class="service-title">{title}</div>
                            <div class="service-desc">{desc}</div>
                        </div>
                    """, unsafe_allow_html=True)


            elif option == menu_options[1]:
                StationInfoUI().get_station_details(option=option)
            elif option == menu_options[2]:
                TrainScheduleUI().get_train_schedule(option=option)
            elif option == menu_options[3]:
                TrainFromStationUI().get_all_trains_from_station(option=option)
            elif option == menu_options[4]:
                TrainFareUI().get_train_fare_details(option=option)
            elif option == menu_options[5]:
                SeatAvailabilityUI().get_seat_availability_info(option=option)
            
            with st.sidebar:
                st.markdown("### 🛤️ Trains Panel")
                sp_trains_options = options["special_trains"]
                with st.expander("🚅 Search Trains", expanded=False):
                    search_type = st.selectbox("Train Type", sp_trains_options)
            if st.sidebar.button("Search Trains"):
                if search_type == sp_trains_options[0]:
                    st.markdown("## 🚅 Special Trains")
                    SpeacialTrainsUI()
                elif search_type == sp_trains_options[1]:
                    st.markdown("## 🚄 Premium Trains")
                    PremiumTrainsUI()
                elif search_type == sp_trains_options[2]:
                    st.markdown("## 🚄 Rajdhani Trains")
                    RajdhaniTrainsUI()
                elif search_type == sp_trains_options[3]:
                    st.markdown("## 🚄 Superfast Trains")
                    SuperfastTrainsUI()
            with st.sidebar:
                st.markdown("### 🎛️ Quick Tools")
                script_options = options["script_menu"]
                with st.expander("🔍 Quick Search", expanded=False):
                    search_type = st.selectbox("Search Type", script_options)
                    search_query = st.text_input(f"Enter {search_type}")
            if st.sidebar.button("Search"):
                if search_type == script_options[0]:
                    StationToCodeUI(station_name=search_query)
                elif search_type == script_options[1]:
                    TrainNoToNameUI(train_no=search_query)
            Feedback()

        except Exception as e:
            st.error("Oops! Some error occurred...")
            raise IrisException(e, sys)
