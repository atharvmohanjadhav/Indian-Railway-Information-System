from iris_custom_exception.custom_exception import IrisException
import sys
import streamlit as st
from src.station_details.station_info import StationInfo
import pandas as pd


class StationInfoUI:

    def get_station_details(self,option):
        try:
            st.sidebar.write("You selected:", option)
            station_name = st.text_input("Enter station name:")

            if station_name:
                info = StationInfo().station_info(station=station_name)
                if info:
                    st.dataframe(info)
                    # st.table(df)
                else:
                    st.error("No station info found or invalid station name.")
        except IrisException as e:
            raise(e,sys)
