from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: dict
	contacts: list
	blocked_contacts: list
	groups: list
	messages: list
	status: list

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	sessions[email] = 'Logged In'
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	sessions.pop(email, None)
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
