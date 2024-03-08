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
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['email']] = User(data['name'], data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	if user.storage_used + data['size'] > 1000:
		return jsonify({'message': 'Storage limit exceeded'}), 400
	user.storage_used += data['size']
	files[data['name']] = File(data['name'], data['size'], data['email'])
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	data = request.args
	file = files.get(data['name'])
	if not file or file.owner != data['email']:
		return jsonify({'message': 'File not found'}), 404
	return jsonify({'message': 'File downloaded successfully', 'file': file.name, 'size': file.size}), 200

if __name__ == '__main__':
	app.run(debug=True)
