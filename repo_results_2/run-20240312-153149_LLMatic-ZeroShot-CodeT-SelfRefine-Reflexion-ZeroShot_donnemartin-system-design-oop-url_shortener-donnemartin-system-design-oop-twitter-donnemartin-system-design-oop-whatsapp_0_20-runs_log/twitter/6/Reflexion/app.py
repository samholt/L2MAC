from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
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
	users[username] = User(username, email, password)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	username = data['username']
	content = data['content']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	posts[username] = Post(username, content)
	return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
