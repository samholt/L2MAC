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
	user = users.get(data['username'])
	if not user or user['password'] != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'user': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'SECRET_KEY')
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if 'user' not in data or 'content' not in data:
		return jsonify({'message': 'Missing user or content'}), 400
	if len(data['content']) > 280:
		return jsonify({'message': 'Content too long'}), 400
	else:
		posts[len(posts)] = data
		return jsonify({'message': 'Post created'}), 200

@app.route('/posts', methods=['GET'])
def get_posts():
	return jsonify(posts), 200

if __name__ == '__main__':
	app.run(debug=True)
