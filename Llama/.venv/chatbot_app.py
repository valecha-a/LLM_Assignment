#------------------------------Basic Python code-------------------------
# import streamlit as st
# import requests
# import json

# # Function to convert session history to messages format
# def convert_to_messages(history):
#     messages = []
#     for entry in history:
#         if entry.startswith("You:"):
#             messages.append({"role": "user", "content": entry[5:]})
#         elif entry.startswith("Bot:"):
#             messages.append({"role": "assistant", "content": entry[5:]})
#     return messages

# # Function to send request to the local model service
# def get_model_response(prompt):
#     url = "http://localhost:11434/api/chat"
#     headers = {"Content-Type": "application/json"}
#     messages = convert_to_messages(st.session_state.conversation)
    
#     data = {
#         "model": "phi3",
#         "messages": messages,
#         "stream": False
#     }
    
#     response = requests.post(url, headers=headers, data=json.dumps(data))
    
#     try:
#         response_json = response.json()
#         return response_json['message']['content']
#     except json.JSONDecodeError as e:
#         st.error(f"JSON decode error: {e}")
#         return "Error: Invalid response from the model service."

# # Streamlit app layout
# st.title("Chat with Local LLM")

# # Initialize conversation history
# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []

# # User input
# user_input = st.text_input("You:", key="user_input")

# # Check if user input is provided and the Send button is clicked
# if st.button("Send"):
#     if user_input:
#         # Add user input to conversation history
#         st.session_state.conversation.append(f"You: {user_input}")
        
#         # Get model response
#         response = get_model_response(user_input)
        
#         # Add model response to conversation history
#         st.session_state.conversation.append(f"Bot: {response}")
        
#         # Clear the user input box by resetting its state
#         user_input = ""

# # Display current interaction (You: input / Bot: response)
# if st.session_state.conversation:
#     latest_interaction = st.session_state.conversation[-2:]
#     st.subheader("Current Interaction")
#     for message in latest_interaction:
#         st.write(message)

# # Display conversation history
# st.subheader("Conversation History")
# conversation_history = "\n".join(st.session_state.conversation)
# st.text_area("History", value=conversation_history, height=300, disabled=True)

# # Clear conversation button
# if st.button("Clear Conversation"):
#     st.session_state.conversation = []


#-----------------------------Cooking and Kitchen Chatbot python code--------------------
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

# Function to classify if a query is cooking or kitchen-related
def is_cooking_query(query):
    cooking_keywords = [
        "cook", "cooking", "recipe", "make", "prepare", "baking", "bake", "chef",
        "culinary", "cuisine", "dish", "meal", "ingredient", "food", "flavor",
        "taste", "spice", "seasoning", "marinate", "sauté", "stir-fry", "roast",
        "grill", "barbecue", "boil", "simmer", "steam", "poach", "fry", "deep fry",
        "pan fry", "broil", "braise", "sear", "blanch", "whip", "blend", "mix",
        "chop", "mince", "slice", "dice", "julienne", "grate", "peel", "core",
        "zest", "knead", "dough", "pastry", "oven", "stove", "cooktop", "microwave",
        "refrigerator", "freezer", "dishwasher", "sink", "faucet", "countertop",
        "cutting board", "knife", "chef's knife", "paring knife", "serrated knife",
        "cleaver", "blender", "food processor", "mixer", "whisk", "spatula", "ladle",
        "tongs", "slotted spoon", "colander", "sieve", "grater", "peeler", "mandoline",
        "rolling pin", "measuring cup", "measuring spoon", "scale", "timer", "thermometer",
        "pot", "pan", "skillet", "saucepan", "Dutch oven", "wok", "griddle", "bakeware",
        "baking sheet", "cake pan", "muffin tin", "casserole dish", "mixing bowl", "salad spinner",
        "braising", "grilling", "smoking", "slow cooking", "pressure cooking", "sous vide",
        "fermenting", "canning", "pickling", "preserving", "curing", "dehydration", "blanching",
        "flash-frying", "poaching", "steaming", "infusing", "emulsifying", "clarifying", "reducing",
        "deglazing", "caramelizing", "tempering", "folding", "appetizer", "soup", "salad", "entree",
        "main course", "side dish", "dessert", "bread", "pasta", "rice", "grain", "noodle", "pizza",
        "sandwich", "burger", "sushi", "seafood", "meat", "poultry", "beef", "chicken", "pork", "lamb",
        "fish", "vegan", "vegetarian", "gluten-free", "dairy-free", "low-carb", "keto", "paleo", "whole30",
        "plant-based", "flexitarian", "pescatarian", "allergen-free", "nut-free", "soy-free", "egg-free",
        "shellfish-free", "meal planning", "weekly meal prep", "batch cooking", "quick meals", "one-pot meals",
        "family meals", "holiday meals", "party food", "brunch", "breakfast", "lunch", "dinner", "snacks",
        "appetizers", "mise en place", "al dente", "al forno", "au gratin", "au jus", "bain-marie", "béchamel",
        "brine", "chiffonade", "degustation", "flambé", "hors d'oeuvre", "mirepoix", "nappe", "panade", "pavé",
        "quenelle", "ramekin", "tartare", "add", "pour", "eat", "ate", "eaten", "sour", "salty", "tasty", "spicy","sweet", "Hello", "Hi"
    ]
    
    non_cooking_keywords = [
        "countries", "boil", "name", "music", "sports", "history", "art", "science",
        "tech", "philosophy"
    ]
    
    query_lower = query.lower()
    
    # Check if any non-cooking keywords are present
    for keyword in non_cooking_keywords:
        if keyword in query_lower:
            return False
    
    # Check if any cooking keywords are present
    for keyword in cooking_keywords:
        if keyword in query_lower:
            return True
    
    # Default to False if neither set of keywords is found
    return False

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
st.title("Cooking and Kitchen Chatbot")

# Initialize conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Initialize user input state
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# User input
user_input = st.text_input("You:", value=st.session_state.user_input, key="input_box")

# Check if user input is provided and the Send button is clicked
if st.button("Send"):
    if user_input:
        # Add user input to conversation history
        st.session_state.conversation.append(f"You: {user_input}")
        
        # Determine if the query is cooking-related
        if is_cooking_query(user_input):
            # Get model response for cooking-related queries
            response = get_model_response(user_input)
            st.session_state.conversation.append(f"Bot: {response}")
        else:
            # Respond that the bot can only answer cooking-related queries
            st.session_state.conversation.append("Bot: I can only answer cooking and kitchen-related queries.")
        
        # Clear the user input box by updating session state
        st.session_state.user_input = ""  # Resetting for future use
        st.rerun()  # Rerun to reset the input field

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

# Instructions for users
st.sidebar.subheader("Instructions")
st.sidebar.write("""
- Enter your queries about cooking and kitchen-related topics in the input box.
- Click 'Send' to get a response from the chatbot.
- You can clear the conversation history using the 'Clear Conversation' button.
""")
