from flask import Flask, request, render_template
import random
import string
from cryptography.fernet import Fernet

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'messages': {},
	'groups': {},
	'statuses': {},
	'blocked_contacts': {},
	'message_queue': {}
}

# Encryption key
key = Fernet.generate_key()

@app.route('/')
def home():
	return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.json.get('email')
		password = request.json.get('password')
		if email in DATABASE['users']:
			return 'User already exists', 400
		DATABASE['users'][email] = {'password': password, 'profile_picture': '', 'status_message': '', 'privacy_settings': 'public', 'online': False}
		DATABASE['blocked_contacts'][email] = []
		DATABASE['message_queue'][email] = []
		return 'User created', 201
	else:
		return render_template('signup.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
	if request.method == 'POST':
		sender = request.json.get('sender')
		receiver = request.json.get('receiver')
		message = request.json.get('message')
		if DATABASE['users'][receiver]['online']:
			DATABASE['messages'][receiver] = {'sender': sender, 'message': message}
		else:
			DATABASE['message_queue'][receiver].append({'sender': sender, 'message': message})
		return 'Message sent', 201
	else:
		return render_template('messages.html')

@app.route('/groups')
def groups():
	return render_template('groups.html')

@app.route('/statuses')
def statuses():
	return render_template('statuses.html')

@app.route('/online', methods=['POST'])
def online():
	user = request.json.get('user')
	status = request.json.get('status')
	DATABASE['users'][user]['online'] = status
	if status:
		for message in DATABASE['message_queue'][user]:
			DATABASE['messages'][user] = message
		DATABASE['message_queue'][user] = []
	return 'Status updated', 200

if __name__ == '__main__':
	app.run(debug=True)
