from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

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
	versions: Dict[int, str] = {}

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
	if user and user.password == password:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
def profile():
	email = request.args.get('email')
	user = users.get(email)
	if user:
		return jsonify(user.__dict__), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	user = users.get(file.owner)
	user.storage_used += file.size
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	filename = request.args.get('filename')
	file = files.get(filename)
	if file:
		return jsonify(file.__dict__), 200
	return jsonify({'message': 'File not found'}), 404

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	filename = data.get('filename')
	recipient = data.get('recipient')
	file = files.get(filename)
	if file and recipient in users:
		return jsonify({'message': 'File shared successfully'}), 200
	return jsonify({'message': 'File or recipient not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
