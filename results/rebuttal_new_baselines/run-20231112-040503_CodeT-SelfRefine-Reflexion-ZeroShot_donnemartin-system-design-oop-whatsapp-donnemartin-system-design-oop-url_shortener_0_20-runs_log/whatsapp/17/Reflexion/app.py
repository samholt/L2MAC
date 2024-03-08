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

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = User(data['name'], data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	sessions[data['email']] = 'Logged In'
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	session = sessions.get(data['email'])
	if not session:
		return jsonify({'message': 'User not logged in'}), 400
	del sessions[data['email']]
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
