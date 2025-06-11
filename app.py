import streamlit as st
import pandas as pd
from utils.custom_exception import IrisException
import sys
from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare_ui import TrainFareUI
from src.seats.seat_availability_ui import SeatAvailabilityUI
from utils.load_yaml import load_yaml_file

st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
        color: #FFD700;
    }
    .stTextInput > div > input {
        background-color: #1E1E1E;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="big-font">Indian Railway Info Portal 🚂</p>', unsafe_allow_html=True)

options = load_yaml_file("config.yaml")

#options = ["live location of train", "station info", "train schedule", "all trains from station","train fares"]
option = st.sidebar.selectbox(label="Select which service do you want", options=options)

if option == options[1]:
    StationInfoUI().get_station_details(option=option)
elif option == options[2]:
    TrainScheduleUI().get_train_schedule(option=option)
elif option == options[3]:
    TrainFromStationUI().get_all_trains_from_station(option=option)
elif option == options[4]:
    TrainFareUI().get_train_fare_details(option=option)
elif option == options[5]:
    SeatAvailabilityUI().get_seat_availability_info(option=option)
else:
    st.write("You selected:", option)
