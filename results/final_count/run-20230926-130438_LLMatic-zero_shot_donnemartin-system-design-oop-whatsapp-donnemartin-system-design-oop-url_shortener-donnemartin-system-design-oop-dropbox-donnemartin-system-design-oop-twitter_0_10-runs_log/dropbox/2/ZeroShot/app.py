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
	versions: list = []

@app.route('/register', methods=['POST'])
def register():
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
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify({'name': user.name, 'email': user.email, 'storage_used': user.storage_used}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	file = File(data['name'], data['size'], data['email'])
	files[data['name']] = file
	user.storage_used += data['size']
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file = files.get(data['name'])
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify({'message': 'File downloaded successfully', 'file': file.__dict__}), 200

if __name__ == '__main__':
	app.run(debug=True)
