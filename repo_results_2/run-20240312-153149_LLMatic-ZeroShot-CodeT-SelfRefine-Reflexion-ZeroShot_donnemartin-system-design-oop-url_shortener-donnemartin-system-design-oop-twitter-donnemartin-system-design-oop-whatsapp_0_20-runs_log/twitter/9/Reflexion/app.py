from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
posts = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@dataclass
class Post:
	user: User
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['name'], data['email'], data['password'])
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/update_profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		user.name = data['name']
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users.get(data['email'])
	if user and user.password == data['password']:
		post = Post(user, data['content'])
		posts[len(posts)] = post
		return jsonify({'message': 'Post created successfully'}), 201
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
