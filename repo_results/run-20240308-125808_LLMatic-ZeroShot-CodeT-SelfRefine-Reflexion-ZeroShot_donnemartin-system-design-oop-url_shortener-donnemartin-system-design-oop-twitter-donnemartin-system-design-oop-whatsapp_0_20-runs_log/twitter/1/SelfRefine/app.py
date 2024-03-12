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

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'])
	except:
		return jsonify({'message': 'Token is invalid or expired'}), 401
	if 'user' not in data or data['user'] not in users:
		return jsonify({'message': 'Invalid user'}), 400
	posts[len(posts)] = data
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/posts', methods=['GET'])
def get_posts():
	return jsonify(posts), 200

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id):
	if post_id not in posts:
		return jsonify({'message': 'Post not found'}), 404
	return jsonify(posts[post_id]), 200

if __name__ == '__main__':
	app.run(debug=True)
