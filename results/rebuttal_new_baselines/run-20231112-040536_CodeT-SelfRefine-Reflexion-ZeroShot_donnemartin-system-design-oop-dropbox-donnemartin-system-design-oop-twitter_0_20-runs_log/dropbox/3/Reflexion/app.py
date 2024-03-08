from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
files = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	storage_used: int = 0

@dataclass
class File:
	name: str
	size: int
	owner: str

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
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	owner = users.get(file.owner)
	if not owner:
		return jsonify({'message': 'User not found'}), 404
	owner.storage_used += file.size
	files[file.name] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
