from flask import Flask, render_template, request, jsonify,session
from src.get_response import generate_visualization_html, return_response
import secrets

secret_key = secrets.token_hex(16)  # Generates a 32-character random hexadecimal string
print(secret_key)

# Create a flask app object
app = Flask(__name__)

app.secret_key = secret_key

@app.before_request
def before_request():
    if 'chat_history' not in session:
        session['chat_history'] = []
        
@app.route('/')
def home():
    #return render_template('chatbot_interface.html')
    chat_history = session.get('chat_history',[])
    print(chat_history)
    return render_template('chatbot_interface.html', chat_history=chat_history)

@app.route('/process_query', methods=['POST'])
def process_query():

    user_query = request.form['user_query']

    output_code = return_response(user_query)
    response = "Test case answer is given below."
    copilot_response = generate_visualization_html(response,output_code )
    session['chat_history'].append({'user_query': user_query, 'copilot_response': copilot_response})
    print(session['chat_history'])
    return jsonify({'response': copilot_response})
 
 
 
@app.route('/history')
def chat_history():
    # Retrieve chat history from session
    chat_history = session.get('chat_history',[])
    print(session)
    return jsonify({'chat_history': chat_history})
    #return render_template('chatbot_interface.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
