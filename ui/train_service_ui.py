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
        
            with st.sidebar:
                st.subheader("🚂 Railway Service Panel")
                options = load_yaml_file("config.yaml")
                menu_options = options["menu_options"]
                option = st.selectbox("Select service", menu_options)

            if option == menu_options[1]:
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
            raise IrisException(e,sys)
