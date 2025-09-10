import streamlit as st
import sys
from utils.session_helper import get_or_set_api_key
from ai_services.ai_storyteller.story_generator import GenerateStory
from ai_services.smart_train_finder.translate_chain import get_translation_chain
from utils.custom_exception import IrisException

class RunStoryTeller:
    def __init__(self):
        try:
            api_key = get_or_set_api_key()
            if not api_key:
                st.error("Please provide a valid Groq API key.")
                return

            story_chain = GenerateStory(api_key)
            translation_chain = get_translation_chain(api_key)

            if "story_response" not in st.session_state:
                st.session_state.story_response = ""
            if "last_inputs" not in st.session_state:
                st.session_state.last_inputs = {"mood": "", "genre": "", "duration": ""}
            if "language" not in st.session_state:
                st.session_state.language = "None"

            st.title("📖 AI Story Generator")

            col1,col2,col3 = st.columns(3)
            with col1:
                mood = st.selectbox("🎭 Select Mood", ["Happy", "Sad", "Curious", "Romantic", "Adventurous", "Motivated", "Bored"])
            with col2:
                genre = st.selectbox("🎬 Select Genre", ["Thriller / Mystery", "Comedy", "Romance", "Sci-fi", "Historical", "Fantasy", "Inspirational", "Travel"])
            with col3:
                duration = st.selectbox("⏱️ Select Duration", ["Short (~2 mins)", "Medium (~5 mins)", "Long (~10+ mins)"])

            if st.button("✨ Generate Story"):
                try:
                    res = story_chain.generate_story(mood, genre, duration)
                    st.session_state.story_response = res
                    st.session_state.last_inputs = {"mood": mood, "genre": genre, "duration": duration}
                    st.session_state.language = "None"
                except Exception as e:
                    # st.error("Failed to generate story.")
                    raise IrisException(e, sys)

            if st.session_state.story_response:
                st.write("### 📝 Your Story:")
                st.write(st.session_state.story_response)

                selected_language = st.selectbox(
                    "🌐 Translate story to:",
                    ["None", "Hindi", "Marathi"],
                    index=["None", "Hindi", "Marathi"].index(st.session_state.language)
                )
                st.session_state.language = selected_language

                if selected_language != "None":
                    try:
                        translated = translation_chain.invoke({
                            "text": st.session_state.story_response,
                            "language": selected_language
                        })
                        st.write(f"### 🌐 Translated Story ({selected_language}):")
                        st.write(translated)
                    except Exception as e:
                        st.error("Translation failed.")
                        raise IrisException(e, sys)

        except Exception as e:
            st.error("Oops! Something went wrong.")
            # raise IrisException(e, sys)
