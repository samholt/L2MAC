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
	user = User(len(users), data['username'], data['email'], data['password'])
	users[user.id] = user
	return jsonify({'id': user.id}), 201

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(len(posts), data['user_id'], data['content'])
	posts[post.id] = post
	return jsonify({'id': post.id}), 201

if __name__ == '__main__':
	app.run(debug=True)
