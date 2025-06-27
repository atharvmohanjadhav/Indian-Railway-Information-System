import streamlit as st
import pandas as pd
from utils.custom_exception import IrisException
import sys
from src.station_trains.trains_from_station import TrainFromStation

class TrainFromStationUI:

    def get_all_trains_from_station(self,option):
        try:
            st.sidebar.write("You selected:",option)
            station_code = st.text_input("Enter station code (e.g., NDLS, CSMT, BCT)", value="CSMT")
            station_code = station_code.upper().strip()
            if station_code:
                info = TrainFromStation().trains_info(station_code=station_code)
                if info and isinstance(info, (list, dict)) and len(info) > 0:
                    st.dataframe(info, use_container_width=True)
                else:
                    st.json({
                        "ResponseCode": "202",
                        "Message": "Server busy. Try again after 5 Min."
                    })
            else:
                st.error("Invalid station code or information not found")

        except Exception as e:
            raise IrisException(e,sys)
        