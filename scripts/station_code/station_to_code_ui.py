from scripts.station_code.station_to_code import StationToCode
from utils.custom_exception import IrisException
import sys
import streamlit as st

class StationToCodeUI:

    def __init__(self,station_name):
        try:
  
            station_name = station_name.lower().strip()

            if station_name:
                info = StationToCode().station_to_code_info(station_name=station_name)
                if info:
                    st.sidebar.success(info)
                else:
                    st.sidebar.error("No station info found or invalid station name.")
        except Exception as e:
            st.error("Oops! Some error occured...")
            raise IrisException(e,sys)
