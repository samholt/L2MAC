from flask import Flask, request, jsonify
from dataclasses import dataclass

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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already in use'}), 400
	users[data['email']] = User(**data)
	return jsonify({'message': 'Registration successful'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']].password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	sessions[data['email']] = True
	return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
	app.run(debug=True)
