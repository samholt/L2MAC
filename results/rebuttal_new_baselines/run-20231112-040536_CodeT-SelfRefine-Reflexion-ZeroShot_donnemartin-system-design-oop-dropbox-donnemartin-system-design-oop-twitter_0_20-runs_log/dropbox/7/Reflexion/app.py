from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

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
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = File(**data)
	files[file.name] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	file_name = request.args.get('file_name')
	file = files.get(file_name)
	if file:
		return jsonify({'file_content': file.content}), 200
	return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
