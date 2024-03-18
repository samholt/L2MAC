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
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		sessions[user.email] = 'Logged In'
		return jsonify({'message': 'Logged In'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	sessions.pop(data['email'], None)
	return jsonify({'message': 'Logged Out'}), 200

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users.get(data['email'])
	if user and sessions.get(user.email):
		user.profile_picture = data.get('profile_picture')
		user.status_message = data.get('status_message')
		user.privacy_settings = data.get('privacy_settings')
		return jsonify({'message': 'Profile updated'}), 200
	return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
	app.run(debug=True)
