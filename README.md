Chatbot with LLM Integration: Cooking and Kitchen Queries
This project implements a chatbot using the LLama3 model for processing natural language queries related to cooking and kitchen-related topics.

Overview
The chatbot leverages the LLama3 large language model to understand user queries about cooking, recipes, ingredients, and related topics. It provides contextually appropriate responses based on the input received.

Features
Natural Language Processing: Interacts with users through natural language queries.
LLama3 Integration: Utilizes the LLama3 model for understanding and generating responses.
Streamlit Interface: User-friendly interface powered by Streamlit for interacting with the chatbot.
Prompting Patterns: Implements various prompting patterns to engage users effectively.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/valecha-a/LLM_Assignment.git
cd [Llama](https://github.com/valecha-a/LLM_Assignment.git)
Setup Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Application:

bash
Copy code
streamlit run chatbot_app.py
Interact with the Chatbot:

Open your browser and navigate to http://localhost:8501.
Enter natural language queries related to cooking and kitchen queries.
Example Queries
User Query: "Hello, Can you tell me a recipe for vegan pasta?"

Bot Response: Provides a relevant vegan pasta recipe.
User Query: "What vegetables do I need for pasta?"

Bot Response: Lists vegetables required for pasta recipes.
User Query: "Types of Indian food"

Bot Response: Provides information about various Indian cuisines.
YouTube Video
Watch a demonstration of the chatbot's features on https://youtu.be/Zwkj9l9WsJo.

References
LLama3 GitHub Repository: [LLama3 GitHub](https://github.com/ollama/ollama)
Streamlit Documentation: [Streamlit](https://docs.streamlit.io/)
