import streamlit as st

def get_or_set_api_key():
    if "groq_api_key" not in st.session_state:
        st.sidebar.subheader("Enter your Groq API Key")
        api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
        if api_key:
            st.session_state["groq_api_key"] = api_key
            st.sidebar.success("API Key saved!")
    return st.session_state.get("groq_api_key", None)

def reset_api_key():
    st.session_state.pop("groq_api_key", None)
    st.sidebar.warning("API Key cleared. Please re-enter.")
