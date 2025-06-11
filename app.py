import streamlit as st
import pandas as pd
from iris_custom_exception.custom_exception import IrisException
import sys
from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare import TrainFare

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


options = ["live location of train", "station info", "train schedule", "all trains from station","train fares"]
option = st.sidebar.selectbox(label="Select which service do you want", options=options)

if option == options[1]:
    StationInfoUI().get_station_details(option=option)
elif option == options[2]:
    TrainScheduleUI().get_train_schedule(option=option)
elif option == options[3]:
    TrainFromStationUI().get_all_trains_from_station(option=option)
elif option == options[4]:
    try:
        st.write("You have select:",option)
        d = st.date_input(label="Select a date",min_value="today")
        d = str(d)
        d = d.split("-")
        d = "".join(d)
        st.write(d)
        train_no = st.text_input("Enter train number:")
        src_station = st.text_input("Enter source station: ")
        dest_station = st.text_input("Enter destination station")
        quota = st.text_input("Enter quata (e.g GN,CK): ")
        src_station = src_station.lower()
        dest_station = dest_station.lower()
        quota = quota.upper()

        if train_no and src_station and dest_station and quota:
            info = TrainFare().train_fare_datail(train_no=train_no,src_station=src_station,dest_station=dest_station,quata=quota)
            try:
                st.write(info)
            except IrisException as e:
                raise (e,sys)
    except IrisException as e:
        raise (e,sys)
else:
    st.write("You selected:", option)
