from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
messages = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@dataclass
class Message:
	from_user: str
	to_user: str
	message: str
	read: bool = False

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/update_profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		user.profile_picture = data.get('profile_picture')
		user.status_message = data.get('status_message')
		user.privacy_settings = data.get('privacy_settings')
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(**data)
	messages.setdefault(message.to_user, []).append(message)
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/get_messages', methods=['GET'])
def get_messages():
	to_user = request.args.get('to_user')
	user_messages = messages.get(to_user, [])
	for message in user_messages:
		message.read = True
	return jsonify([message.__dict__ for message in user_messages]), 200

if __name__ == '__main__':
	app.run(debug=True)
