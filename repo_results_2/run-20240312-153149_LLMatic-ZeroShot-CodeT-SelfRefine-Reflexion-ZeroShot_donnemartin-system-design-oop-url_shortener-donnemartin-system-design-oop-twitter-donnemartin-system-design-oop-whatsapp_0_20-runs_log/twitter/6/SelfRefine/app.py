from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import hashlib
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Mock database
users = {}
posts = {}

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
	if not data or 'username' not in data or 'email' not in data or 'password' not in data:
		raise BadRequest('Invalid request data')
	username = data['username']
	email = data['email']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username in users or any(user.email == email for user in users.values()):
		return jsonify({'message': 'Username or email already exists'}), 400
	users[username] = User(username, email, password, {})
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'username' not in data or 'password' not in data:
		raise BadRequest('Invalid request data')
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	if not data or 'username' not in data or 'content' not in data:
		raise BadRequest('Invalid request data')
	username = data['username']
	content = data['content']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	posts[len(posts)] = Post(username, content, 0, 0, [])
	return jsonify({'message': 'Post created successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
