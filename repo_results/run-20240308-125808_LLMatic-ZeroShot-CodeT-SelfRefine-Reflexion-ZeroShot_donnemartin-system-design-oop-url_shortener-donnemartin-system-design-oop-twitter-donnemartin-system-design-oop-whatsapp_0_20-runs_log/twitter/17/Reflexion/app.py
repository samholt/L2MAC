from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
posts = {}

@dataclass
class User:
	username: str
	email: str
	password: str

@dataclass
class Post:
	user: str
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
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	username = data['username']
	content = data['content']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	posts[len(posts)] = Post(username, content)
	return jsonify({'message': 'Post created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
