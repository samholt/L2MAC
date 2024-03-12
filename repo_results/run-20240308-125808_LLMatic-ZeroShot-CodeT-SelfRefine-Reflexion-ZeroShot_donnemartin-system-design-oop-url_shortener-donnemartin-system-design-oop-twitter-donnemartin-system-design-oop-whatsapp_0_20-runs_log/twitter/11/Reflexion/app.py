from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	id: str
	username: str
	email: str
	password: str
	profile: Dict

@dataclass
class Post:
	id: str
	user_id: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data.get('id'))
	if user and user.password == data.get('password'):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post = posts.get(data.get('post_id'))
	if post:
		post.likes += 1
		return jsonify({'message': 'Post liked'}), 200
	return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
