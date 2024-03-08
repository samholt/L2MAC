from flask import Flask, request, jsonify
from models import User

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	user = User(id=len(users), username=username, password=password)
	users[username] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users.get(username)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200
