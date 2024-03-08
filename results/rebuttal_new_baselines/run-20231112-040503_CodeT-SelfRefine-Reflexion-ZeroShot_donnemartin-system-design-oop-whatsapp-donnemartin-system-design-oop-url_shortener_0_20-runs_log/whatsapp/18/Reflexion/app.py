from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
messages = {}
groups = {}
group_messages = {}

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: Dict
	blocked_contacts: Dict

@dataclass
class Message:
	id: str
	from_user: str
	to_user: str
	message: str
	read_receipt: bool
	encryption: bool

@dataclass
class Group:
	id: str
	name: str
	picture: str
	members: Dict
	admin: Dict

@dataclass
class GroupMessage:
	id: str
	from_user: str
	to_group: str
	message: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data.get('id'))
	if user and user.password == data.get('password'):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user = users.get(data.get('id'))
	if user and user.email == data.get('email'):
		# In a real application, send email to user with password reset link
		return jsonify({'message': 'Password reset link sent to email'}), 200
	return jsonify({'message': 'Invalid user'}), 404

if __name__ == '__main__':
	app.run(debug=True)
