import streamlit as st
import traceback

def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # Log the traceback to console (for developers)
        traceback.print_exc()

        # Show a friendly message to the user
        st.error(
            "🚧 Oops! Something went wrong while processing your request. "
            "Please try again or contact support if the problem persists."
        )

        # Optionally, return a fallback value
        return None
