import streamlit as st
import chatbot_backend as demo

# Styling with CSS
st.markdown("""
<style>
    /* Chat container */
    .chat-container {
        background-color: #f5f5f5; /* Soft background */
        padding: 20px;
        border-radius: 10px; 
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    /* User messages */
    .user-message {
        background-color: #e0e0ff; /* Light blue */
        padding: 10px;
        border-radius: 5px 10px 10px 10px; /* Right-aligned speech bubble */
        margin-bottom: 10px;
        text-align: left;
    }

    /* Assistant messages */
    .assistant-message {
        background-color: #fff; /* White */
        padding: 10px;
        border-radius: 10px 5px 10px 10px; /* Left-aligned speech bubble */
        margin-bottom: 10px;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# Chatbot Setup 
st.title("Hi, This is Chatbot Assistant :sunglasses:")

if 'memory' not in st.session_state:
    st.session_state.memory = demo.create_memory()  # Initialize from backend
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat UI with Styling
st.write('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.write(f'<div class="user-message">{message["text"]}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div class="assistant-message">{message["text"]}</div>', unsafe_allow_html=True)

st.write('</div>', unsafe_allow_html=True)

# Input and Chat Logic
input_text = st.chat_input("Powered by Bedrock and LLama 2")

if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    chat_response = demo.get_chat_response(input_text)

    with st.chat_message("assistant"):
        st.markdown(chat_response)
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response}) 
