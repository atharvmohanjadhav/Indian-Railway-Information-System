import streamlit as st
import pandas as pd
from iris_custom_exception.custom_exception import IrisException
import sys
from src.station_trains.trains_from_station import TrainFromStation

class TrainFromStationUI:

    def get_all_trains_from_station(self,option):
        try:
            st.sidebar.write("You selected:",option)
            station_code = st.text_input("Enter station code (e.g., NDLS, CSMT, BCT)", value="CSMT")
            if station_code:
                info = TrainFromStation().trains_info(station_code=station_code)
                if info:
                    st.dataframe(info,use_container_width=True)
                    # st.table(df)
            else:
                st.error("Invalid station code or information not found")

        except IrisException as e:
            raise (e,sys)
        