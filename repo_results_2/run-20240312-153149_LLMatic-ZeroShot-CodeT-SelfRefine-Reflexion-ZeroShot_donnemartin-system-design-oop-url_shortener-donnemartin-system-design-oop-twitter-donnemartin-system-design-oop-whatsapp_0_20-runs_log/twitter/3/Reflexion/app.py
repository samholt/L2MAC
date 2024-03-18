from flask import Flask, request, jsonify
import jwt
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

users = {}
posts = {}

@dataclass
class User:
	username: str
	email: str
	password: str
	following: List[str] = []

@dataclass
class Post:
	username: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = User(username, email, password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	token = data['token']
	content = data['content']
	try:
		username = jwt.decode(token, 'secret', algorithms=['HS256'])['username']
	except:
		return jsonify({'message': 'Invalid token'}), 400
	posts[len(posts)] = Post(username, content)
	return jsonify({'message': 'Post created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
