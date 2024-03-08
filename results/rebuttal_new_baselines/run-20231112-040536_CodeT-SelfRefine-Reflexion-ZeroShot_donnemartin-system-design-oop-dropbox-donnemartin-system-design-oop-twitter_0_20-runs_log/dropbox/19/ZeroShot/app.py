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
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	users[file.owner].storage_used += file.size
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
	file = files.get(filename)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify({'message': 'File downloaded successfully', 'file': file}), 200

@app.route('/share/<filename>', methods=['POST'])
def share(filename):
	data = request.get_json()
	file = files.get(filename)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify({'message': 'File shared successfully', 'file': file}), 200

if __name__ == '__main__':
	app.run(debug=True)
