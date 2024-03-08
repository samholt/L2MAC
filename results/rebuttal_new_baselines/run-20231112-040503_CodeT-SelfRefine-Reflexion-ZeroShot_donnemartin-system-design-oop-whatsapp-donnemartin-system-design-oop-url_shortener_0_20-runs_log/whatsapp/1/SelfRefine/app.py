from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

users = {}
sessions = {}

@dataclass
class User:
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
	contacts: list = None
	groups: list = None

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already exists'}), 400
	user = User(**data)
	users[data['email']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']].password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	if data['email'] in sessions:
		return jsonify({'message': 'User already logged in'}), 400
	sessions[data['email']] = True
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	if data['email'] not in sessions:
		return jsonify({'message': 'User not logged in'}), 400
	del sessions[data['email']]
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
