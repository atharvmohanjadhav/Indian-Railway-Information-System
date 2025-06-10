import streamlit as st
import pandas as pd
from iris_custom_exception.custom_exception import IrisException
import sys
from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI

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


options = ["live location of train", "station info", "train schedule", "all trains from station"]
option = st.sidebar.selectbox(label="Select which service do you want", options=options)

if option == 'station info':
    StationInfoUI().get_station_details(option=option)
elif option == "train schedule":
    TrainScheduleUI().get_train_schedule(option=option)
elif option == "all trains from station":
    TrainFromStationUI().get_all_trains_from_station(option=option)
else:
    st.write("You selected:", option)
