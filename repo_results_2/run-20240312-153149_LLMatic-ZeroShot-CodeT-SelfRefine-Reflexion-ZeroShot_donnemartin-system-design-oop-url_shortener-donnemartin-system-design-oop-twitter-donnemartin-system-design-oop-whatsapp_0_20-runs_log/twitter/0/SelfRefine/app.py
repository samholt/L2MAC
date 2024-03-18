from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[data['username']] = {
		'password': generate_password_hash(data['password']),
		'email': data['email'],
		'profile': {}
	}
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['username'] not in users or not check_password_hash(users[data['username']]['password'], data['password']):
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	users[username]['profile'] = data['profile']
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	posts[len(posts)] = {
		'user': username,
		'text': data['text'],
		'likes': 0,
		'retweets': 0,
		'replies': []
	}
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	data = request.get_json()
	username = jwt.decode(data['token'], app.config['SECRET_KEY'])['user']
	if post_id not in posts or posts[post_id]['user'] != username:
		return jsonify({'message': 'Invalid post id'}), 400
	del posts[post_id]
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
