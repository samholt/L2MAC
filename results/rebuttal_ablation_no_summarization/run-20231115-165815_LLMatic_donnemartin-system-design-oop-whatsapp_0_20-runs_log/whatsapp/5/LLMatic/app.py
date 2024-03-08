from flask import Flask, request
import time

app = Flask(__name__)

# Mock database
users = {}

@app.route('/')
def home():
	return 'Welcome to the User Management System!', 200

@app.route('/signup', methods=['POST'])
def signup():
	email = request.json.get('email')
	password = request.json.get('password')
	if email not in users:
		users[email] = {'password': password, 'blocked': [], 'groups': {}, 'messages': [], 'read_receipts': {}, 'statuses': [], 'online': False, 'queued_messages': []}
		return 'User created successfully', 201
	else:
		return 'User already exists', 400

@app.route('/online', methods=['POST'])
def online():
	email = request.json.get('email')
	online = request.json.get('online')
	if email in users:
		users[email]['online'] = online
		if online:
			users[email]['messages'].extend(users[email]['queued_messages'])
			users[email]['queued_messages'] = []
		return 'Online status updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_email = request.json.get('sender_email')
	recipient_email = request.json.get('recipient_email')
	message = request.json.get('message')
	if sender_email in users and recipient_email in users:
		if users[recipient_email]['online']:
			users[recipient_email]['messages'].append({'sender': sender_email, 'message': message})
		else:
			users[recipient_email]['queued_messages'].append({'sender': sender_email, 'message': message})
		return 'Message sent successfully', 200
	else:
		return 'User not found', 404

# Rest of the code...
