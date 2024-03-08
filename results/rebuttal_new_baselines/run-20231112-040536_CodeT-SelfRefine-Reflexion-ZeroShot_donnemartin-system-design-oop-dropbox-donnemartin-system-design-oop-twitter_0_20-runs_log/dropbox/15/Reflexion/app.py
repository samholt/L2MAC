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

@dataclass
class File:
	name: str
	content: str

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
	return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	user = users.get(data['email'])
	if user:
		return jsonify(user.__dict__), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file = files.get(data['name'])
	if file:
		return jsonify(file.__dict__), 200
	return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
