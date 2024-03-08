from flask import Flask, request, jsonify
from user import User
from file_manager import FileManager

app = Flask(__name__)

users = {}
files = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['name'], data['email'], data['password'])
	users[data['email']] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email in users and users[email].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = FileManager(data['filename'], data['content'], data['user'])
	files[data['filename']] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
