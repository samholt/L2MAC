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
	version: int = 1

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	user = users.get(data['email'])
	if user:
		return jsonify(user.__dict__), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/change_password', methods=['POST'])
def change_password():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['old_password']:
		user.password = data['new_password']
		return jsonify({'message': 'Password changed successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/upload_file', methods=['POST'])
def upload_file():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	user = users.get(file.owner)
	user.storage_used += file.size
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download_file', methods=['GET'])
def download_file():
	data = request.get_json()
	file = files.get(data['file_name'])
	if file:
		return jsonify(file.__dict__), 200
	return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
