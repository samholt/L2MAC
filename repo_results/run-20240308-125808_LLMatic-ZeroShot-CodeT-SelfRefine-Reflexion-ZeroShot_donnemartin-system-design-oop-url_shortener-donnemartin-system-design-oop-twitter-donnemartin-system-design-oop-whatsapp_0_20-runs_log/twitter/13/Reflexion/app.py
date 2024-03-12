from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	username: str
	email: str
	password: str

@dataclass
class Post:
	user_id: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	posts[post.user_id] = post
	return jsonify({'message': 'Post created successfully'}), 201
