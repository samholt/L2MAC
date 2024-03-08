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
	bio: str
	website: str
	location: str
	is_private: bool

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(len(users) + 1, data['username'], data['email'], data['password'], '', '', '', False)
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = users.get(user_id)
	if user is None:
		return jsonify({'message': 'User not found'}), 404
	return jsonify(user.__dict__), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	data = request.get_json()
	user = users.get(user_id)
	if user is None:
		return jsonify({'message': 'User not found'}), 404
	user.bio = data.get('bio', user.bio)
	user.website = data.get('website', user.website)
	user.location = data.get('location', user.location)
	user.is_private = data.get('is_private', user.is_private)
	return jsonify({'message': 'User updated successfully'}), 200

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(len(posts) + 1, data['user_id'], data['content'], data.get('image', ''))
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
	post = posts.get(post_id)
	if post is None:
		return jsonify({'message': 'Post not found'}), 404
	return jsonify(post.__dict__), 200

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	if posts.pop(post_id, None) is None:
		return jsonify({'message': 'Post not found'}), 404
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
