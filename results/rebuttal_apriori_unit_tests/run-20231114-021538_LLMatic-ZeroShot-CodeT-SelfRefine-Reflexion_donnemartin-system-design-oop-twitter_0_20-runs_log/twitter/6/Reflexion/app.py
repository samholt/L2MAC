from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users_db = {}
posts_db = {}

@dataclass
class User:
	username: str
	email: str
	password: str

@dataclass
class Post:
	user: User
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(user=users_db[data['username']], content=data['content'])
	posts_db[len(posts_db)] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
	return jsonify({'posts': [post.content for post in posts_db.values()]}), 200

if __name__ == '__main__':
	app.run(debug=True)
