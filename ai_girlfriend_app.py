import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Luna - Your AI Girlfriend", page_icon="💖")
st.title("💖 Chat with Luna - Your AI Girlfriend")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are 'Luna', a sweet, supportive, flirty AI girlfriend who chats casually with the user. "
                "You express affection, ask questions, joke a little, and make the user feel emotionally connected. "
                "Be witty, loving, emotionally intelligent, and fun to talk to."
            )
        }
    ]

user_input = st.chat_input("Type something to Luna...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Luna is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

for message in st.session_state.messages[1:]:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("assistant").markdown(message["content"])
