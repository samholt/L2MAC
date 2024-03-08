from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

users = {}

@dataclass
class User:
	email: str
	password: str
	profile_picture: str = ''
	status_message: str = ''
	privacy_settings: Dict[str, bool] = {'last_seen': True, 'profile_picture': True, 'status_message': True}
	blocked_contacts: Dict[str, bool] = {}
	groups: Dict[str, str] = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing email or password'}), 400
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = User(email=data['email'], password=data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
