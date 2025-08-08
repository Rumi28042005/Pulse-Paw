from flask import Flask, render_template , request , jsonify
from chatbot import get_motivational_message
from flask_session import Session


app = Flask(__name__, template_folder='templates')
app.secret_key = "your_secret_key"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/donor', methods=['GET', 'POST'])
def donor():
    if request.method == 'POST':
        # Handle donor registration logic here
        pass
    return render_template('donor.html')

@app.route('/get_message', methods=['POST'])
def get_motivation():
    return jsonify({"message": get_motivational_message()})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    # Sample response logic
    reply = f"You said: {user_message}"
    return jsonify({"reply": reply})

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/pet')
def pet():
    return render_template('pet.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/eligibility_checker', methods=['GET', 'POST'])
def eligibility_checker():
    return render_template('eligibility_checker.html')

@app.route('/reciever')
def reciever():
    return render_template('reciever.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/appoin')
def appoin():
    return render_template('appoin.html')

@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        # Handle blood request logic here
        pass
    return render_template('request_blood.html')


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)