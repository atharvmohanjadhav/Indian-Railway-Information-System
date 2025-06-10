import streamlit as st 
from iris_custom_exception.custom_exception import IrisException
import sys
from train_fares.train_fare import TrainFare

class TrainFareUI:

    def get_train_fare_details(self,option):
        st.write("You have select:",option)
        train_no = st.text_input("Enter train number:")
        src_station = st.text_input("Enter source station: ")
        dest_station = st.text_input("Enter destination station")
        quota = st.text_input("Enter quata (e.g GN,CK): ")

        if train_no and src_station and dest_station and quota:
            info = TrainFare().train_fare_datail(train_no=train_no,src_station=src_station,dest_station=dest_station,quata=quota)
            try:
                st.write(info)
            except IrisException as e:
                raise (e,sys)

