import streamlit as st
import pandas as pd
from src.station_details.station_info_ui import StationInfoUI

st.header("Indian Railway Information System 🚂")

options = ["live location of train", "station info", "train status", "all trains from station"]
option = st.sidebar.selectbox(label="Select which service do you want", options=options)

if option == 'station info':
    StationInfoUI().get_station_details(option=option)
else:
    st.write("You selected:", option)
