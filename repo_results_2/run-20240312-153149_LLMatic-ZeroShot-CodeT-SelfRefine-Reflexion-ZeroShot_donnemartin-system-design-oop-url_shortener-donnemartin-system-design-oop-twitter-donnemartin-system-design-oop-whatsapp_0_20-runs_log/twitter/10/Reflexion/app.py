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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(len(users), data['username'], data['email'], data['password'], {})
	users[user.id] = user
	return jsonify({'id': user.id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'id': user.id}), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/users/<int:user_id>', methods=['GET', 'PUT'])
def user(user_id):
	user = users.get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	if request.method == 'PUT':
		data = request.get_json()
		user.profile = data.get('profile', user.profile)
	return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'profile': user.profile}), 200

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(len(posts), data['user_id'], data['content'], 0)
	posts[post.id] = post
	return jsonify({'id': post.id}), 201

@app.route('/posts/<int:post_id>', methods=['GET', 'DELETE'])
def post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'error': 'Post not found'}), 404
	if request.method == 'DELETE':
		del posts[post_id]
		return '', 204
	return jsonify({'id': post.id, 'user_id': post.user_id, 'content': post.content, 'likes': post.likes}), 200

if __name__ == '__main__':
	app.run(debug=True)
