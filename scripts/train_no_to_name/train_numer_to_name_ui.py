from scripts.station_code.station_to_code import StationToCode
from scripts.train_no_to_name.train_number_to_name import TrainNoToName
from utils.custom_exception import IrisException
import sys
import streamlit as st

class TrainNoToNameUI:

    def __init__(self,train_no):
        try:
            #st.sidebar.subheader("Station Name To Station Code ⬇️")
            #train_no = st.sidebar.text_input("train number:")
            train_no = train_no.lower().strip()

            if train_no:
                info = TrainNoToName().train_no_to_name_info(train_no=train_no)
                if info:
                    st.sidebar.success(info)
                else:
                    st.sidebar.error("No station info found or invalid station name.")
        except IrisException as e:
            raise(e,sys)
