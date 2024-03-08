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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

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

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user or email not in sessions:
		return jsonify({'message': 'User not logged in'}), 401
	user.profile_picture = data.get('profile_picture', user.profile_picture)
	user.status_message = data.get('status_message', user.status_message)
	return jsonify({'message': 'Profile updated successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
