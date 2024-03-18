from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime
import hashlib

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
	if not data['username'] or not data['email'] or not data['password']:
		return jsonify({'message': 'Invalid input'}), 400
	hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
	new_user = User(data['username'], data['email'], hashed_password, {})
	users[data['username']] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
	if not user or user.password != hashed_password:
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

if __name__ == '__main__':
	app.run(debug=True)
