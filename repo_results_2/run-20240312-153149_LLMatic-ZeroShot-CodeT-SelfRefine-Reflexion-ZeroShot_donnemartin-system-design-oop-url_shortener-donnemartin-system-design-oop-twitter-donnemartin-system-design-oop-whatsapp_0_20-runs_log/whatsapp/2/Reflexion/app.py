from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}

@dataclass
class User:
	email: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if email in users:
		return jsonify({'message': 'Email already in use'}), 400
	users[email] = User(email, password)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
