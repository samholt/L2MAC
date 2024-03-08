from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)

# Mock database
users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[data['username']] = data
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['username'] not in users or users[data['username']]['password'] != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	users[username].update(data)
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	posts[len(posts)] = data
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	if post_id not in posts:
		return jsonify({'message': 'Post not found'}), 404
	del posts[post_id]
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
