from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	profile: Dict

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	likes: int
	retweets: int
	replies: Dict

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(id=len(users)+1, username=data['username'], email=data['email'], password=data['password'], profile={})
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(id=len(posts)+1, user_id=data['user_id'], content=data['content'], likes=0, retweets=0, replies={})
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
