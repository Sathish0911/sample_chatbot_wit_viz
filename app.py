from flask import Flask, render_template, request, jsonify, session
from src.get_response import generate_visualization_html, return_response
import secrets
from flask_session import Session

# Generates a 32-character random hexadecimal string
secret_key = secrets.token_hex(16)
print(secret_key)


app = Flask(__name__)




# Configuring Session
#app.config['PERMANENT_SESSION_LIFETIME'] = 60  # Session Lifetime
app.config['SESSION_TYPE'] = "filesystem"  # Session Storage Type
app.config['SESSION_PERMANENT'] = False 
app.config['SESSION_FILE_DIR'] = "session_data"
app.config['SECRET_KEY'] = secret_key
 
# Initializing the Session Extension
Session(app)
# Create a flask app object




@app.before_request
def before_request():
    if 'chat_history' not in session:
        session['chat_history'] = []


@app.route('/')
def home():
    if 'chat_history' in session:
        print(chat_history)
        return render_template('chatbot_interface.html', chat_history=chat_history)
    return render_template('chatbot_interface.html')


@app.route('/process_query', methods=['POST'])
def process_query():
    user_query = request.form['user_query']
    output_code = return_response(user_query)
    response = "Test case answer is given below."
    copilot_response = generate_visualization_html(response, output_code)
    session['chat_history'].append(
        {'user_query': user_query, 'copilot_response': copilot_response})
    print(session['chat_history'])
    return jsonify({'response': copilot_response})


@app.route('/history', methods=['GET'])
def chat_history():
    # Retrieve chat history from session
    chat_history = session['chat_history']
    print(session['chat_history'])
    return jsonify({'chat_history': chat_history})
    # return render_template('chatbot_interface.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
