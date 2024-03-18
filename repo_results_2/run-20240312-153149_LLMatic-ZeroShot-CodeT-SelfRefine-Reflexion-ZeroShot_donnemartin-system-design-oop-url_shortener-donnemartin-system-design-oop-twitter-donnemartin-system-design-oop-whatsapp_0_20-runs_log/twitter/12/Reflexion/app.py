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

@dataclass
class Post:
	id: int
	user_id: int
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(len(users) + 1, data['username'], data['email'], data['password'])
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if len(data['content']) > 280:
		return jsonify({'message': 'Post content exceeds character limit'}), 400
	post = Post(len(posts) + 1, data['user_id'], data['content'])
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
