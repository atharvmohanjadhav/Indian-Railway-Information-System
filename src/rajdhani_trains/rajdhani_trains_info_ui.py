import streamlit as st
import pandas as pd
from utils.custom_exception import IrisException
import sys
from src.rajdhani_trains.rajdhani_trains_info import RajdhaniTrains

class RajdhaniTrainsUI:
    def __init__(self):
        try:
            info = RajdhaniTrains().rajdhani_trains_info()
            if info and isinstance(info, (list, dict)) and len(info) > 0:
                st.dataframe(info, use_container_width=True)
            else:
                st.json({
                    "ResponseCode": "202",
                    "Message": "Server busy. Try again after 5 Min."
                })
                
        except IrisException as e:
            raise (e,sys)
        