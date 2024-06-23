LLama3 ReadMe

Anmol Valecha June 2024

Introduction

This document provides a step-by-step guide for downloading, installing, and running the Llama3 model on an M1 Mac. Additionally, it includes instructions for setting up a Python environment, installing Streamlit, and creating a chatbot to interact with the model.

Prerequisites

• M1 Mac

• Python installed

• Visual Studio Code (VS Code) installed

• Internet connection

Step-by-Step Instructions

1. Setting Up Python Virtual Environment

1. Create a New Folder:

• Create a new folder named Assignment3 and navigate into it:

mkdir Assignment3 cd Assignment3

2. Create a Virtual Environment:

• Run the following command to create a virtual environment:

python3 −m venv

. venv

3. Activate the Virtual Environment:

1 • Activate the virtual environment with:

source . venv/ bin / activate

4. Install Streamlit:

• Inside the activated virtual environment, install Streamlit using pip:

pip i n s t a l l s t r e a m l i t

2. Download and Install Llama3

1. Download Ollama from GitHub:

• Visit the Llama3 GitHub repository.

• Download the ZIP file and extract it.

2. Install Ollama:

• Open the terminal and navigate to the extracted folder.

• Run the following command to install Ollama:

./ i n s t a l l . sh

• To verify the installation, run:

ollama −−version

3. Run Llama3 Model:

• To run the model, use the command:

ollama run phi3

• This will download and start the model in the terminal.

4. Check if Llama3 is Running:

• Open a new terminal window and run:

l s o f −i tcp :11434

• This command checks if the Llama3 service is running on port 11434.

5. Close the Chat:

• To close the chat, use the following command in the terminal:

/bye

2 3. Code for the Chatbot

Listing 1: chatbot.py

import s t r e a m l i t import requests import json

as

st

# Function to convert session h i s t o r y

def convert to messages ( history ) :

to

messages

format

messages = [ ] for entry in history :

i f entry . startswith ( ”You : ” ) :

messages . append ( { ” r o l e ” : ” user ” , ” content ” : entry [ 5 : ] } ) e l i f entry . startswith ( ”Bot : ” ) :

messages . append ( { ” r o l e ” : ” a s s i s t a n t ” , ” content ” : entry [ 5 : ] } ) return messages

# Function to send request to the l o c a l model s e r v i c e

def get model response ( prompt ) :

url = ” http :// l o c a l h o s t :11434/ api / chat ” headers = { ”Content−Type” : ” application / json ” } messages = convert to messages ( st . s e s s i o n s t a t e . conversation )

data = {

”model” : ” phi3 ” , ”messages ” : messages , ”stream” : False

}

response = requests . post ( url ,

try :

headers=headers ,

response json = response . json () return response json [ ’ message ’ ] [ ’ content ’ ] except json . JSONDecodeError as e :

data=json . dumps( data ))

st . error ( f ”JSON decode error : { e } ” ) return ” Error : Invalid response from the model

service . ”

# Streamlit app layout st . t i t l e ( ”Chat with Local LLM” )

# I n i t i a l i z e conversation i f ’ conversation ’ not in

history st . s e s s i o n s t a t e :

st . s e s s i o n s t a t e . conversation = [ ]

3 # User input user input = st . text input ( ”You : ” ,

# Check i f user input

is

provided

i f st . button ( ”Send” ) :

key=” user input ” )

and the Send button

# Add user input to conversation h i s t o r y st . s e s s i o n s t a t e . conversation . append ( f ”You :

{

is

clicked

i f user input :

user input } ” )

# Get model response response = get model response ( user input )

# Add model response to conversation h i s t o r y st . s e s s i o n s t a t e . conversation . append ( f ”Bot :

# Clear the user input user input = ””

box by

resetting

its

{

response } ” )

state

# Display current i n t e r a c t i o n (You: i f st . s e s s i o n s t a t e . conversation :

input / Bot :

response )

l a t e s t i n t e r a c t i o n = st . s e s s i o n s t a t e . conversation [ −2:]

st . subheader ( ”Current I nte rac tion ” ) for message in l a t e s t i n t e r a c t i o n :

st . write ( message )

# Display conversation h i s t o r y

st . subheader ( ” Conversation History ” ) conversation history = ” \ n” . j o i n ( st . s e s s i o n s t a t e . conversation ) st . text area ( ” History ” , value=conversation history , height =300,

# Clear conversation button i f st . button ( ” Clear Conversation ” ) :

disabled=True )

st . s e s s i o n s t a t e . conversation = [ ]

4. Running the Chatbot

1. Start Streamlit:

• In the terminal, run:

streamlit

run chatbot . py

2. Interact with the Model:

• Open the provided local URL in a web browser.

• Interact with the chatbot interface, which sends requests to the Llama3 model running locally.

4 5. Setting Up Llama3 User Interface

1. Download the UI:

• Follow the instructions provided in the Llama3 GitHub repository to download the user interface.

2. Install Dependencies:

• Navigate to the UI folder and install the required dependencies:

cd llama3−ui npm i n s t a l l

3. Start the User Interface:

• Run the UI:

npm s t a r t

4. Access the UI:

• Open the provided local URL in a web browser to access the Llama3 user interface.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


GPT4all ReadMe

Anmol Valecha June 2024

Introduction

This document provides a step-by-step guide for downloading, installing, and running the GPT4all model on an M1 Mac using Flask for the web interface.

Prerequisites

• M1 Mac

• Python installed

• Visual Studio Code (VS Code) installed

• Internet connection

Step-by-Step Instructions

1. Setting Up Python Virtual Environment

1. Create a New Folder:

• Create a new folder named GPT4all Assignment and navigate into it:

mkdir GPT4all Assignment cd GPT4all Assignment

2. Create a Virtual Environment:

• Run the following command to create a virtual environment:

python3 −m venv

. venv

3. Activate the Virtual Environment:

• Activate the virtual environment with:

1 source

. venv/ bin / activate

4. Install GPT4all:

• Install GPT4all using pip in the activated virtual environment:

pip

install

gpt4all

5. Install Flask:

• Install Flask using pip in the activated virtual environment:

pip

install

flask

2. Download User Interface

• Download the GPT4all user interface from the official website: https:

//gpt4all.io/

• Follow the installation instructions provided on the website to set up the user interface on your local machine.

3. Setting Up Flask Web Interface

1. Create Flask Application:

• In your project directory, create a Python file (e.g., ‘app.py‘) for your Flask application.

2. Write Flask Application Code:

• Implement Flask routes and logic to interact with the GPT4all model.

Here’s an example based on your provided code:

Listing 1: app.py

from f l a s k import Flask , request , from g p t 4 a l l import GPT4All

name

app = Flask (

)

jsonify

model = GPT4All( model name=’ orca−mini−3b−gguf2−q4 0 . gguf ’ )

@app . route ( ’ / api / generate ’ , def generate ( ) :

methods=[ ’POST’ ] )

try :

data = request . json prompt = data . get ( ’ prompt ’ ) i f not prompt :

return j s o n i f y ( { ” error ” : ”No prompt provided ” } ) ,

400

2 with model . c h a t s e s s i o n ( ) :

response = model . generate ( prompt ,

j s o n i f y ( { ” response ” :

response } )

return

temp=0)

except Exception as e :

return j s o n i f y ( { ” error ” :

@app . route ( ’ / ’ , methods=[ ’GET’ ] )

def h e l l o ( ) :

return ” Hello ,

World ! ”

if

name == ’ main app . run ( debug=True ,

’:

str ( e ) } ) , 500

port =5050)

3. Run Flask Application:

• Start the Flask server:

python app . py

4. Access the Web Interface:

• Open a web browser and go to ‘http://localhost:5050‘ to interact with the GPT4all model through the Flask interface.

4. Interacting with GPT4all

• Using Curl:

– Use the following curl command on another terminal to interact with GPT4all via Flask:

curl −X POST http :// l o c a l h o s t :5050/ api / generate \ −H ”Content−Type : application / json ” \ −d ’ { ”prompt ”: ”Your Question ” } ’

• Using User Interface:

– Open the installed GPT4all user interface on your machine.

– Select the desired model (e.g.,gpt4all, phi3) from the interface.

– Click on ”New Chat” to start a new chat session and interact with the model.
