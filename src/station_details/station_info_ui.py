from utils.custom_exception import IrisException
import sys
import streamlit as st
from src.station_details.station_info import StationInfo


class StationInfoUI:

    def get_station_details(self,option:list):
        try:
            st.sidebar.write("You selected:", option)
            station_name = st.text_input("Enter station name:")
            station_name = station_name.lower().strip()

            if station_name:
                info = StationInfo().station_info(station=station_name)
                if info:
                    st.dataframe(info)
                else:
                    st.error("No station info found or invalid station name.")
        except Exception as e:
            raise IrisException(e,sys)
