from flask import Flask, request, jsonify
from dataclasses import dataclass

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
	user = User(len(users) + 1, data['username'], data['email'], data['password'], {})
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/profile/<int:user_id>', methods=['GET', 'PUT'])
def profile(user_id):
	user = users.get(user_id)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	if request.method == 'PUT':
		data = request.get_json()
		user.profile = data
	return jsonify(user.profile), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(len(posts) + 1, data['user_id'], data['content'], 0, 0, [])
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def get_post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	if request.method == 'DELETE':
		del posts[post_id]
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'id': post.id, 'user_id': post.user_id, 'content': post.content, 'likes': post.likes, 'retweets': post.retweets, 'replies': post.replies}), 200

if __name__ == '__main__':
	app.run(debug=True)
