import streamlit as st
import pandas as pd
from src.station_details.station_info_ui import StationInfoUI
from iris_custom_exception.custom_exception import IrisException
import sys
from src.schedule.train_schedule_ui import TrainScheduleUI

st.header("Indian Railway Information System 🚂")

options = ["live location of train", "station info", "train schedule", "all trains from station"]
option = st.sidebar.selectbox(label="Select which service do you want", options=options)

if option == 'station info':
    StationInfoUI().get_station_details(option=option)
elif option == "train schedule":
    TrainScheduleUI().get_train_schedule(option=option)
else:
    st.write("You selected:", option)
