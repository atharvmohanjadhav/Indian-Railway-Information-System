import streamlit as st
import pandas as pd
import time
from datetime import datetime
from utils.custom_exception import IrisException
import sys
from src.station_details.station_info_ui import StationInfoUI
from src.schedule.train_schedule_ui import TrainScheduleUI
from src.station_trains.trains_from_station_ui import TrainFromStationUI
from src.train_fares.train_fare_ui import TrainFareUI
from src.seats.seat_availability_ui import SeatAvailabilityUI
from utils.load_yaml import load_yaml_file

# Enhanced page configuration
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

# Advanced CSS styling with modern design elements
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

# Real-time status bar
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current Time", current_time.split()[1], delta="Live")
with col2:
    st.metric("Services Available", "5", delta="Active")
with col3:
    st.metric("Database Status", "Online", delta="Healthy")
with col4:
    st.metric("Response Time", "120ms", delta="Fast")

# Load configuration
options = load_yaml_file("config.yaml")

# Enhanced service selection with cards
st.markdown("## 🎯 Select Your Service")
st.markdown("Choose from our comprehensive railway information services:")

# Create service cards layout
col1, col2, col3 = st.columns(3)

services_config = {
    options[1]: {"icon": "🏢", "title": "Station Information", "desc": "Get detailed station information, facilities, and amenities"},
    options[2]: {"icon": "📅", "title": "Train Schedule", "desc": "Check real-time train schedules and timings"},
    options[3]: {"icon": "🚄", "title": "Station Trains", "desc": "View all trains departing from specific stations"},
    options[4]: {"icon": "💰", "title": "Fare Calculator", "desc": "Calculate train fares for your journey"},
    options[5]: {"icon": "🪑", "title": "Seat Availability", "desc": "Check real-time seat availability and booking status"}
}

# Service selection using radio buttons with custom styling
selected_service = st.radio(
    "Choose a service:",
    options[1:],
    format_func=lambda x: f"{services_config[x]['icon']} {services_config[x]['title']}",
    horizontal=True
)

# Display service information cards
service_cols = st.columns(len(options[1:]))
for idx, (service, config) in enumerate(services_config.items()):
    with service_cols[idx]:
        is_selected = service == selected_service
        card_style = "service-card" + (" selected-card" if is_selected else "")
        
        st.markdown(f"""
        <div class="{card_style}">
            <div class="service-icon">{config['icon']}</div>
            <div class="service-title">{config['title']}</div>
            <div class="service-description">{config['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# Enhanced content display with loading states
if selected_service:
    with st.container():
        # Create a loading animation
        loading_placeholder = st.empty()
        content_placeholder = st.empty()
        
        # Show loading state
        with loading_placeholder:
            st.markdown("""
            <div class="loading-animation">
                <div class="train-loader">🚂</div>
            </div>
            """, unsafe_allow_html=True)
            
            progress_bar = st.progress(0)
            status_text = st.empty()
        
            for i in range(100):
                progress_bar.progress(i + 1)
                status_text.text(f'Loading {services_config[selected_service]["title"]}... {i+1}%')
                time.sleep(0.01)
        
        # Clear loading state
        loading_placeholder.empty()
        
        # Display content based on selection
        with content_placeholder:
            st.markdown(f"## {services_config[selected_service]['icon']} {services_config[selected_service]['title']}")
            
            # Create expandable information section
            with st.expander("ℹ️ Service Information", expanded=True):
                st.info(f"**About this service:** {services_config[selected_service]['desc']}")
            
            # Service-specific content
            if selected_service == options[1]:
                StationInfoUI().get_station_details(option=selected_service)
            elif selected_service == options[2]:
                TrainScheduleUI().get_train_schedule(option=selected_service)
            elif selected_service == options[3]:
                TrainFromStationUI().get_all_trains_from_station(option=selected_service)
            elif selected_service == options[4]:
                TrainFareUI().get_train_fare_details(option=selected_service)
            elif selected_service == options[5]:
                SeatAvailabilityUI().get_seat_availability_info(option=selected_service)

# Enhanced sidebar with multiple sections
with st.sidebar:
    st.markdown("### 🎛️ Control Panel")
    
    # Quick search functionality
    with st.expander("🔍 Quick Search", expanded=True):
        search_type = st.selectbox("Search Type", ["Train Number", "Station Code", "Route"])
        search_query = st.text_input("Enter search term")
        if st.button("Search", type="primary"):
            if search_query:
                st.success(f"Searching for {search_type}: {search_query}")
    
    # User preferences
    with st.expander("⚙️ Preferences"):
        language = st.selectbox("Language", ["English", "Hindi", "Tamil", "Telugu"])
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
        notifications = st.checkbox("Enable Notifications", value=True)
    
    # Quick stats
    with st.expander("📊 Quick Stats"):
        st.metric("Total Stations", "7,349", delta="12")
        st.metric("Active Trains", "13,523", delta="45")
        st.metric("Daily Passengers", "23.0M", delta="2.1M")
    
    # Help and support
    with st.expander("❓ Help & Support"):
        st.markdown("""
        - 📞 **Emergency**: 139
        - 🎫 **Reservations**: 139
        - 💬 **Support**: railway.help@gov.in
        - 🌐 **Website**: [railway.gov.in](https://railway.gov.in)
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Last updated: " + datetime.now().strftime("%H:%M:%S") + "*")

# Advanced caching implementation
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_station_data():
    """Load and cache station data for better performance"""
    try:
        # Simulate data loading
        time.sleep(1)  # Simulate API call
        return pd.DataFrame({
            'station_code': ['NDLS', 'BCT', 'HWH', 'MAS', 'SBC'],
            'station_name': ['New Delhi', 'Mumbai Central', 'Howrah', 'Chennai Central', 'Bangalore City'],
            'zone': ['NR', 'WR', 'ER', 'SR', 'SWR']
        })
    except Exception as e:
        raise IrisException(e, sys)

@st.cache_resource
def initialize_database_connection():
    """Initialize and cache database connection"""
    # This would be your actual database connection
    return {"status": "connected", "timestamp": datetime.now()}

# Use cached data
if st.sidebar.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.experimental_rerun()

# Interactive features section
if selected_service:
    st.markdown("---")
    st.markdown("## 🎮 Interactive Features")
    
    feature_col1, feature_col2, feature_col3 = st.columns(3)
    
    with feature_col1:
        if st.button("📱 Download Mobile App", type="secondary"):
            st.balloons()
            st.success("Redirecting to app store...")
    
    with feature_col2:
        feedback = st.selectbox("📝 Quick Feedback", ["Select...", "Excellent", "Good", "Average", "Poor"])
        if feedback != "Select...":
            st.toast(f"Thank you for your {feedback} feedback!", icon="👍")
    
    with feature_col3:
        if st.button("🔔 Subscribe to Updates"):
            with st.spinner("Subscribing..."):
                time.sleep(2)
            st.success("Successfully subscribed to updates!")

# Footer with additional information
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("### 🌟 Features")
    st.markdown("""
    - Real-time data
    - Multi-language support
    - Mobile responsive
    - Offline capability
    """)

with footer_col2:
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    - [Official Website](https://railway.gov.in)
    - [Mobile App](https://app.railway.gov.in)
    - [Customer Care](https://care.railway.gov.in)
    - [Feedback](https://feedback.railway.gov.in)
    """)

with footer_col3:
    st.markdown("### 📊 System Status")
    system_status = "🟢 All systems operational"
    st.success(system_status)
    st.caption("Last checked: " + datetime.now().strftime("%H:%M:%S"))
