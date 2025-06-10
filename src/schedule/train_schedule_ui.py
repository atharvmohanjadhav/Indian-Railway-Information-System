import streamlit as st
import pandas as pd
from iris_custom_exception.custom_exception import IrisException
from src.schedule.train_schedule import TrainSchedule
import sys

class TrainScheduleUI:

    def get_train_schedule(self,option):
        try:
            st.sidebar.write("You selected:", option)
            train_no = st.text_input("Enter Train Number:")

            if train_no:
                info = TrainSchedule().get_info(train_number=train_no)
                if info:
                    st.dataframe(info)
                    # st.table(df)
                else:
                    st.error("invalid train number or No schedule found.")
        except IrisException as e:
            raise(e,sys)
        