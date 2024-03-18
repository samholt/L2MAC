from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = User(**data)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']].password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	sessions[data['email']] = True
	return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	if data['email'] not in sessions:
		return jsonify({'message': 'User not logged in'}), 400
	del sessions[data['email']]
	return jsonify({'message': 'User logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
