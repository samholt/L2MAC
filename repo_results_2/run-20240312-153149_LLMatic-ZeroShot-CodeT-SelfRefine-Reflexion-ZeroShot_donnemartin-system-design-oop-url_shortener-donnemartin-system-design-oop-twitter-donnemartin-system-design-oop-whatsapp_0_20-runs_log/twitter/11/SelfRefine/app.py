from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

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
	if data['username'] in users:
		return jsonify({'message': 'Username already exists'}), 400
	new_user = User(data['username'], data['email'], data['password'], {})
	users[data['username']] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	content = request.get_json().get('content')
	new_post = Post(data['user'], content, 0, 0, [])
	posts[len(posts)] = new_post
	return jsonify({'message': 'Posted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
