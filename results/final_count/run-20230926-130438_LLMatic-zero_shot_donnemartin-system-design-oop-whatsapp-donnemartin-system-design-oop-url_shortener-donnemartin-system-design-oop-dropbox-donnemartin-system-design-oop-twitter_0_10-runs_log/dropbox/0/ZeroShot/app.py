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
	versions: list = None

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already registered'}), 400
	users[data['email']] = User(**data)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Login successful'}), 200

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
	user = users.get(data['owner'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	if user.storage_used + data['size'] > 1000:
		return jsonify({'message': 'Storage limit exceeded'}), 400
	user.storage_used += data['size']
	files[data['name']] = File(**data)
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	file_name = request.args.get('file_name')
	file = files.get(file_name)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	return jsonify(file.__dict__), 200

if __name__ == '__main__':
	app.run(debug=True)
