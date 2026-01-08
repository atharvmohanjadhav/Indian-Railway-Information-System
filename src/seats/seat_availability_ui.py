import streamlit as st
from utils.custom_exception import IrisException
import sys
from src.seats.seat_availability import SeatAvailability

class SeatAvailabilityUI:

    def get_seat_availability_info(self):
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
                class_code = st.text_input("Enter quata (e.g 1A/2A/3A/SL): ")
            reserv_date = st.date_input(label="Select a date",min_value="today")

            src_station = src_station.lower().strip()
            dest_station = dest_station.lower().strip()
            class_code = class_code.upper().strip()
            d = str(reserv_date)
            d = d.split("-")
            d = "".join(d)

            if train_no and src_station and dest_station and class_code and d:
                info = SeatAvailability().get_seat_availability_info(train_no=train_no,src_station=src_station,dest_station=dest_station,
                                                                reservation_date=d,class_code=class_code)
                
                if info and isinstance(info, (list, dict)) and len(info) > 0:
                    st.dataframe(info, use_container_width=True)
                else:
                    st.json({
                        "ResponseCode": "202",
                        "Message": "Server busy. Try again after 5 Min."
                    })

        except Exception as e:
            raise IrisException(e,sys)
        