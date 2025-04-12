import streamlit as st
import google.generativeai as ai

# API Key
API_KEY = "AIzaSyDvYQrhDJ23YGWVJc73ZWCF97tn-8HAZXg"

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-1.5-pro-latest")

chat = model.start_chat()

# Streamlit UI
st.title("Chatbot ")
st.write("Talk to the chatbot below:")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.text_input("You:", "", key="user_input")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get chatbot response
    response = chat.send_message(user_input)
    chatbot_reply = response.text
    
    # Display chatbot response
    st.session_state.messages.append({"role": "bot", "content": chatbot_reply})
    with st.chat_message("bot"):
        st.write(chatbot_reply)
