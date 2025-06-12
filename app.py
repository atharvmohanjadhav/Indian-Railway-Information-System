import streamlit as st
import pandas as pd
from utils.custom_exception import IrisException
import sys
from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare_ui import TrainFareUI
from src.seats.seat_availability_ui import SeatAvailabilityUI
from scripts.station_code.station_to_code_ui import StationToCodeUI
from utils.load_yaml import load_yaml_file
from datetime import datetime

st.set_page_config(
    page_title="Indian Railway Info Portal",
    page_icon="🚂",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://railway.gov.in',
        'Report a bug': "mailto:support@railwayportal.com",
        'About': "# Indian Railway Info Portal\nYour comprehensive railway information system!"
    }
)

st.markdown("""
<style>
    /* Main application styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Custom header with gradient background */
    .railway-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: white;
    }
    
    .railway-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .railway-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    /* Service cards styling */
    .service-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e6ed;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
    
    .service-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }
    
    .service-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .service-description {
        color: #7f8c8d;
        text-align: center;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: white;
    }
    
    /* Custom metrics styling */
    .metric-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Loading animation */
    .loading-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }
    
    .train-loader {
        font-size: 3rem;
        animation: move 2s linear infinite;
    }
    
    @keyframes move {
        0% { transform: translateX(-100px); }
        100% { transform: translateX(100px); }
    }
</style>
""", unsafe_allow_html=True)
# Enhanced header with logo and dynamic content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="railway-header">
        <div class="railway-title">🚂 Indian Railway Info Portal</div>
        <div class="railway-subtitle">Your Gateway to Real-time Railway Information</div>
    </div>
    """, unsafe_allow_html=True)

options = load_yaml_file("config.yaml")

st.sidebar.subheader("Select which service do you want")
option = st.sidebar.selectbox(label="Select service", options=options)

StationToCodeUI()

if option == options[1]:
    StationInfoUI().get_station_details(option=option)
elif option == options[2]:
    TrainScheduleUI().get_train_schedule(option=option)
elif option == options[3]:
    TrainFromStationUI().get_all_trains_from_station(option=option)
elif option == options[4]:
    TrainFareUI().get_train_fare_details(option=option)
elif option == options[5]:
    SeatAvailabilityUI().get_seat_availability_info(option=option)



