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
	versions: list

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

@app.route('/profile', methods=['GET'])
def profile():
	email = request.args.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify(user.__dict__), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	user = users.get(data.get('email'))
	user.storage_used += file.size
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	filename = request.args.get('filename')
	file = files.get(filename)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify(file.__dict__), 200

@app.route('/version', methods=['POST'])
def version():
	data = request.get_json()
	filename = data.get('filename')
	version = data.get('version')
	file = files.get(filename)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	file.versions.append(version)
	return jsonify({'message': 'Version added successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
