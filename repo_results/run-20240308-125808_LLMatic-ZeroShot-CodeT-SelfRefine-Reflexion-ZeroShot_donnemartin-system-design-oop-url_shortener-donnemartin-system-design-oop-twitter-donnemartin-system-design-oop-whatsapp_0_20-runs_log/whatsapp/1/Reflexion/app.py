from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: Dict = None
	contacts: Dict = None
	groups: Dict = None
	messages: Dict = None

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
	return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = users.get(data['email'])
	if user:
		user.password = data['new_password']
		return jsonify({'message': 'Password reset successful'}), 200
	return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
