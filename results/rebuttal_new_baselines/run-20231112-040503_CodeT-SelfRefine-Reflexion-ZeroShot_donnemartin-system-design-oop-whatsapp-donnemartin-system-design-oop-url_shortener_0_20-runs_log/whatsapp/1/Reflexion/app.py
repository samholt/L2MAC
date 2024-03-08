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
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	sessions[user.email] = True
	return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
