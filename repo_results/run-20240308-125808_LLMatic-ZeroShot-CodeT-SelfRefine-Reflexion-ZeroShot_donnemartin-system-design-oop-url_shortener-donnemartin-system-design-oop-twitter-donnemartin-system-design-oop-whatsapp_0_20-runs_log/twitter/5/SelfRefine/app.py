from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt

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
	profile: dict

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] or user.email == data['email']:
			return jsonify({'message': 'Username or email already in use'}), 400
	user = User(len(users), data['username'], data['email'], data['password'], {})
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
			return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(len(posts), data['user_id'], data['content'], 0, 0, [])
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
