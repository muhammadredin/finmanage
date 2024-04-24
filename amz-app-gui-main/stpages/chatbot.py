import time
from stpages import be
import streamlit as st

def run():
    st.title("Q&A Chatbot")

    # if 'vector_index' not in st.session_state: 
    #     with st.spinner("Loading model..."): ###spinner message
    #         st.session_state.vector_index = be.call_claude() ### Your Index Function name from Backend File

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter prompt here"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # prompt = prompt_fixer(prompt)
            result = be.rag_setup(prompt)

            # Simulate stream of response with milliseconds delay
            for chunk in result.split(' '): # fix for https://github.com/streamlit/streamlit/issues/868
                full_response += chunk + ' '
                if chunk.endswith('\n'):
                    full_response += ' '
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
