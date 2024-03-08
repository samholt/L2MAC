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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], password=data['password'])
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
	files[data['filename']] = data['filecontent']
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	filename = request.args.get('filename')
	filecontent = files.get(filename)
	if filecontent:
		return jsonify({'filecontent': filecontent}), 200
	return jsonify({'message': 'File not found'}), 404
