from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: Dict
	blocked_contacts: Dict
	groups: Dict

@dataclass
class Message:
	id: str
	from_user: str
	to_user: str
	content: str
	read_receipt: bool
	encryption: bool

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		return jsonify({'message': 'Logout successful'}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = users.get(data['id'])
	if user:
		user.password = data['new_password']
		return jsonify({'message': 'Password reset successful'}), 200
	return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
