import streamlit as st
from ui.train_service_ui import TrainService
from ui.ai_service_ui import AiService
from scripts.news.rail_news_ui import RunNewsChain

st.set_page_config(
    page_title="Indian Railway Info Portal",
    page_icon="🚂",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

st.markdown("""
    <div class="railway-header">
        <div class="railway-title">🚂 Indian Railway Info Portal</div>
        <div class="railway-subtitle">Your Gateway to Real-time Railway Information with Integrated AI system</div>
    </div>
""", unsafe_allow_html=True)

col1, col2,col3 = st.columns([1, 1,1])
with col1:
    if st.button("🚂 Rail Service"):
        st.session_state.active_tab = "Rail Service"
with col2:
    if st.button("🤖 AI Service"):
        st.session_state.active_tab = "AI Service"
with col3:
    if st.button("📰 Rail News"):
        st.session_state.active_tab = "Rail News"

if st.session_state.active_tab == "Rail Service":
    TrainService()
elif st.session_state.active_tab == "AI Service":
    AiService()
else:
    RunNewsChain()