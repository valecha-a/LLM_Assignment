import streamlit as st
import requests
import json

# Function to convert session history to messages format
def convert_to_messages(history):
    messages = []
    for entry in history:
        if entry.startswith("You:"):
            messages.append({"role": "user", "content": entry[5:]})
        elif entry.startswith("Bot:"):
            messages.append({"role": "assistant", "content": entry[5:]})
    return messages

# Function to send request to the local model service
def get_model_response(prompt):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    messages = convert_to_messages(st.session_state.conversation)
    
    data = {
        "model": "phi3",
        "messages": messages,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    try:
        response_json = response.json()
        return response_json['message']['content']
    except json.JSONDecodeError as e:
        st.error(f"JSON decode error: {e}")
        return "Error: Invalid response from the model service."

# Streamlit app layout
st.title("Chat with Local LLM")

# Initialize conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# User input
user_input = st.text_input("You:", key="user_input")

# Check if user input is provided and the Send button is clicked
if st.button("Send"):
    if user_input:
        # Add user input to conversation history
        st.session_state.conversation.append(f"You: {user_input}")
        
        # Get model response
        response = get_model_response(user_input)
        
        # Add model response to conversation history
        st.session_state.conversation.append(f"Bot: {response}")
        
        # Clear the user input box by resetting its state
        user_input = ""

# Display current interaction (You: input / Bot: response)
if st.session_state.conversation:
    latest_interaction = st.session_state.conversation[-2:]
    st.subheader("Current Interaction")
    for message in latest_interaction:
        st.write(message)

# Display conversation history
st.subheader("Conversation History")
conversation_history = "\n".join(st.session_state.conversation)
st.text_area("History", value=conversation_history, height=300, disabled=True)

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.conversation = []
