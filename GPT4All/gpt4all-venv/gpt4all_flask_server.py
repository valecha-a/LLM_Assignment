from gpt4all import GPT4All
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Initialize GPT4All model
model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf')

# Endpoint to generate responses
@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Get prompt from JSON data in the request
        data = request.json
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        # Generate response using GPT4All model
        with model.chat_session():
            response = model.generate(prompt, temp=0)
        
        # Return the response as JSON
        return jsonify({"response": response})
    
    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({"error": str(e)}), 500

# Endpoint for testing
@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5050)
