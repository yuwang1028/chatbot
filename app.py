import streamlit as st
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

# Initialize floating features for the interface
float_init()


# Initialize session state for managing chat messages
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]


initialize_session_state()

st.title("OpenAI Conversational Chatbot 🤖")

# Create a container for the microphone and audio recording
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            final_response = get_answer(st.session_state.messages)
        with st.spinner("Generating audio response..."):
            audio_file = text_to_speech(final_response)
            autoplay_audio(audio_file)
        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        os.remove(audio_file)


