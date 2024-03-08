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
	profile: Dict = None

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	likes: int = 0
	retweets: int = 0
	replies: int = 0

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.password == data['password']:
		return jsonify(user), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify(post), 201

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post = posts.get(data['post_id'])
	if post:
		post.likes += 1
		return jsonify(post), 200
	return {'message': 'Post not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
