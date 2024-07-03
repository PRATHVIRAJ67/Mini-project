import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

MISTRAL_API_KEY = os.environ['MISTRAL_API_KEY']

client = Groq(api_key=MISTRAL_API_KEY)

st.title("Medical ChatBot")

chat_container = st.container()

with chat_container:
    pass  

user_input = st.text_area("Type your message here", key="user_input")

def get_response_from_mistral(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""You are an Medical Chatbot you should answer only medical related question if anyone asks other than medical field u should i dont have expertice other than medical field
                User: {user_input}"""
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

if st.button("SUBMIT", key="send_btn"):
    st.write(f"User message: {user_input}")
    
    if user_input:
        with st.spinner("Generating response..."):
            response = get_response_from_mistral(user_input)
            st.write(f"Medical ChatBot: {response}")

st.markdown(
    """
    <style>
        .container {
            margin-top: 5rem;
        }

        .chat-box {
            margin-top: 3rem;
        }

        .form-group {
            margin-top: 3rem;
        }

        #message-input {
            width: 100%;
        }

        #send-btn {
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)