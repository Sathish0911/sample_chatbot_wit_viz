from flask import Flask, render_template, request, jsonify
from src.get_response import generate_visualization_html, return_response

# Create a flask app object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chatbot_interface.html')

@app.route('/process_query', methods=['POST'])
def process_query():

    user_query = request.form['user_query']

    output_code = return_response(user_query)
    response = "Test case answer is given below."
    copilot_response = generate_visualization_html(response,output_code )
    
    return jsonify({'response': copilot_response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
