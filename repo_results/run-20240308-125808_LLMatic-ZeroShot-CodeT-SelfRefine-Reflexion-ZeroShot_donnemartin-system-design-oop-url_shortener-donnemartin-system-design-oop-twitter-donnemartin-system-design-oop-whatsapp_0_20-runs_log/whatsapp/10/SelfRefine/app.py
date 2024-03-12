from flask import Flask, request, jsonify
from dataclasses import dataclass
import hashlib

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already in use'}), 400
	data['password'] = hashlib.sha256(data['password'].encode()).hexdigest()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	if email not in users:
		return jsonify({'message': 'User not found'}), 404
	password = hashlib.sha256(data.get('password').encode()).hexdigest()
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	sessions[email] = 'Logged In'
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	if email not in users:
		return jsonify({'message': 'User not found'}), 404
	sessions.pop(email, None)
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
