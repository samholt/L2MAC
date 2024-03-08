from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	username: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if user is None or user.password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200
