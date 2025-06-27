import streamlit as st 
from utils.custom_exception import IrisException
import sys
from src.train_fares.train_fare import TrainFare

class TrainFareUI:

    def get_train_fare_details(self,option):
        try:
            col1,col2 = st.columns(2)
            col3,col4 = st.columns(2)
            with col1:
                train_no = st.text_input("Enter train number:")
            with col2:
                src_station = st.text_input("Enter source station: ")
            with col3:
                dest_station = st.text_input("Enter destination station")
            with col4:
                quota = st.text_input("Enter quata (e.g GN,CK): ")
            src_station = src_station.lower().strip()
            dest_station = dest_station.lower().strip()
            quota = quota.upper().strip()

            if train_no and src_station and dest_station and quota:
                info = TrainFare().train_fare_datail(train_no=train_no,src_station=src_station,dest_station=dest_station,quata=quota)
                try:
                    if info and isinstance(info, (list, dict)) and len(info) > 0:
                        st.dataframe(info, use_container_width=True)
                    else:
                        st.json({
                            "ResponseCode": "202",
                            "Message": "Server busy. Try again after 5 Min."
                        })
                except Exception as e:
                    raise IrisException(e,sys)
        except Exception as e:
            raise IrisException(e,sys)

