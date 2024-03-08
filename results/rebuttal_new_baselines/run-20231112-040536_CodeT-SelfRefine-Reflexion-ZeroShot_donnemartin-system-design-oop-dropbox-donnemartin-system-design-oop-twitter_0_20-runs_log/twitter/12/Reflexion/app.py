from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

app = Flask(__name__)
app.config.from_object('config.Config')
jwt = JWTManager(app)

# Mock database
users = {}
posts = {}

@dataclass
class User:
	username: str
	password: str
	email: str

@dataclass
class Post:
	user: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	email = data.get('email')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, generate_password_hash(password), email)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if not user or not check_password_hash(user.password, password):
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	username = data.get('username')
	content = data.get('content')
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	posts[len(posts)] = Post(username, content)
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	post_id = data.get('post_id')
	if post_id not in posts:
		return jsonify({'message': 'Post does not exist'}), 400
	del posts[post_id]
	return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
