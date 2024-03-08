from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {}
posts = {}

SECRET_KEY = 'secret'

@dataclass
class User:
	username: str
	email: str
	password: str
	profile: dict

@dataclass
class Post:
	user: str
	content: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_user = User(data['username'], data['email'], hashed_password, {})
	users[data['username']] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or not check_password_hash(user.password, data['password']):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	user = users.get(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	new_post = Post(user.username, data['content'], 0, 0, [])
	posts[len(posts)] = new_post
	return jsonify({'message': 'Posted successfully'}), 200

@app.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
	data = request.get_json()
	post = posts.get(post_id)
	if not post or post.user != data['username']:
		return jsonify({'message': 'Post not found or unauthorized'}), 404
	post.content = data['content']
	return jsonify({'message': 'Post updated successfully'}), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	data = request.get_json()
	post = posts.get(post_id)
	if not post or post.user != data['username']:
		return jsonify({'message': 'Post not found or unauthorized'}), 404
	del posts[post_id]
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
