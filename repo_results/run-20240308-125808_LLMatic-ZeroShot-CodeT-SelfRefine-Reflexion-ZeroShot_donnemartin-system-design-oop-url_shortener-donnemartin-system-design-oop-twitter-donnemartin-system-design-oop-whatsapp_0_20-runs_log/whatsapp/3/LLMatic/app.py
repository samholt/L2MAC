from flask import Flask, request, render_template
import mock_db
from user import User
from message import Message
from contact import Contact
from group_chat import GroupChat

app = Flask(__name__)
db = mock_db.MockDB()

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		data = request.get_json()
		user = User(data['email'], data['password'], data.get('profile_picture'), data.get('status_message'), data.get('privacy_settings'))
		db.add(user.email, user)
		return 'User registered successfully', 201
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		user = db.retrieve(data['email'])
		if user and user.password == data['password']:
			return 'Login successful', 200
		else:
			return 'Invalid email or password', 401
	return render_template('login.html')

@app.route('/chat', methods=['GET'])
def chat():
	return render_template('chat.html')

@app.route('/status', methods=['GET'])
def status():
	return render_template('status.html')

@app.route('/online', methods=['POST'])
def online():
	data = request.get_json()
	user = db.retrieve(data['email'])
	if user:
		user.go_online()
		return 'User is online', 200
	else:
		return 'User not found', 404

@app.route('/offline', methods=['POST'])
def offline():
	data = request.get_json()
	user = db.retrieve(data['email'])
	if user:
		user.go_offline()
		return 'User is offline', 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
