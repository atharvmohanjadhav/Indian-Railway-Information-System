import streamlit as st
from datetime import datetime
from utils.load_yaml import load_yaml_file

from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare_ui import TrainFareUI
from src.seats.seat_availability_ui import SeatAvailabilityUI

from src.trains.special_trains.special_trains_info_ui import SpeacialTrainsUI
from src.trains.premium_trains.premium_trains_info_ui import PremiumTrainsUI
from src.trains.rajdhani_trains.rajdhani_trains_info_ui import RajdhaniTrainsUI
from src.trains.super_fast_trains.superfast_trains_info_ui import SuperfastTrainsUI

from scripts.station_code.station_to_code_ui import StationToCodeUI
from scripts.train_no_to_name.train_numer_to_name_ui import TrainNoToNameUI
from scripts.feedback.review_ui import Feedback


# ---------------------- Streamlit Config ---------------------- #
st.set_page_config(
    page_title="Indian Railway Info Portal",
    page_icon="🚂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- Custom CSS ---------------------- #
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1300px;
    }

    .railway-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }

    .railway-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }

    .railway-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-bottom: 0;
    }

    .stButton button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(to right, #2980b9, #6dd5fa);
        color: white;
        font-weight: 600;
        height: 3rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Rail Service"

# ---------------------- Header ---------------------- #
st.markdown("""
    <div class="railway-header">
        <div class="railway-title">🚂 Indian Railway Info Portal</div>
        <div class="railway-subtitle">Your Gateway to Real-time Railway Information & AI StudyMate</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------- Tab Simulation ---------------------- #
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🚂 Rail Service"):
        st.session_state.active_tab = "Rail Service"
with col2:
    if st.button("🤖 AI Service"):
        st.session_state.active_tab = "AI Service"

# ---------------------- RAIL SERVICE TAB ---------------------- #
if st.session_state.active_tab == "Rail Service":
    with st.sidebar:
        st.subheader("🚂 Railway Service Panel")
        options = load_yaml_file("config.yaml")
        menu_options = options["menu_options"]
        option = st.selectbox("Select service", menu_options)

    if option == menu_options[1]:
        StationInfoUI().get_station_details(option=option)
    elif option == menu_options[2]:
        TrainScheduleUI().get_train_schedule(option=option)
    elif option == menu_options[3]:
        TrainFromStationUI().get_all_trains_from_station(option=option)
    elif option == menu_options[4]:
        TrainFareUI().get_train_fare_details(option=option)
    elif option == menu_options[5]:
            SeatAvailabilityUI().get_seat_availability_info(option=option)
    with st.sidebar:
        st.markdown("### 🛤️ Trains Panel")
        sp_trains_options = options["special_trains"]
        with st.expander("🚅 Search Trains", expanded=True):
            search_type = st.selectbox("Train Type", sp_trains_options)
    if st.sidebar.button("Search Trains"):
        if search_type == sp_trains_options[0]:
            st.markdown("## 🚅 Special Trains")
            SpeacialTrainsUI()
        elif search_type == sp_trains_options[1]:
            st.markdown("## 🚄 Premium Trains")
            PremiumTrainsUI()
        elif search_type == sp_trains_options[2]:
            st.markdown("## 🚄 Rajdhani Trains")
            RajdhaniTrainsUI()
        elif search_type == sp_trains_options[3]:
            st.markdown("## 🚄 Superfast Trains")
            SuperfastTrainsUI()
    with st.sidebar:
        st.markdown("### 🎛️ Quick Tools")
        script_options = options["script_menu"]
        with st.expander("🔍 Quick Search", expanded=True):
            search_type = st.selectbox("Search Type", script_options)
            search_query = st.text_input(f"Enter {search_type}")
    if st.sidebar.button("Search"):
        if search_type == script_options[0]:
            StationToCodeUI(station_name=search_query)
        elif search_type == script_options[1]:
            TrainNoToNameUI(train_no=search_query)

    Feedback()

# ---------------------- AI SERVICE TAB ---------------------- #
elif st.session_state.active_tab == "AI Service":
    with st.sidebar:
        st.subheader("🤖 AI StudyMate Panel")
        ai_task = st.radio("Choose AI Tool", ["Notes Generator", "Quiz Maker", "Mind Map", "Syllabus Navigator"])
        user_input = st.text_area("Enter your topic/query")
        if st.button("Run AI"):
            st.success(f"Running: {ai_task} for topic '{user_input}'")

    st.markdown("## 🤖 Welcome to AI StudyMate")
    st.write("""
        Use this panel to interact with AI-powered learning tools:
        - ✍️ **Notes Generator**
        - 🧠 **Mind Map Visualizer**
        - 📚 **Syllabus Navigator**
        - ❓ **Quiz Generator**

        Each tool helps personalize and speed up your learning!
    """)
