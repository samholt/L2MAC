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
	version: int

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already exists'}), 400
	users[data['email']] = User(data['name'], data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/profile', methods=['GET'])
def profile():
	data = request.args
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify({'name': user.name, 'email': user.email}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	files[data['name']] = File(data['name'], data['content'], 1)
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	data = request.args
	file = files.get(data['name'])
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify({'name': file.name, 'content': file.content, 'version': file.version}), 200

if __name__ == '__main__':
	app.run(debug=True)
