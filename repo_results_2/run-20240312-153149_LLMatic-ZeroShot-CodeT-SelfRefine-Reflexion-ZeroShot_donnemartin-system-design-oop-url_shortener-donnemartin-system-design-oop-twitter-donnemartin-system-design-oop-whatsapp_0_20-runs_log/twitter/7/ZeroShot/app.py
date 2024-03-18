from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
import datetime

app = Flask(__name__)

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
	new_user = User(data['username'], data['email'], data['password'], {})
	users[data['username']] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	new_post = Post(data['user'], data['content'], 0, 0, [])
	posts[len(posts)] = new_post
	return jsonify({'message': 'Posted successfully'}), 200

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post = posts.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	post.likes += 1
	return jsonify({'message': 'Liked successfully'}), 200

@app.route('/retweet', methods=['POST'])
def retweet():
	data = request.get_json()
	post = posts.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	post.retweets += 1
	return jsonify({'message': 'Retweeted successfully'}), 200

@app.route('/reply', methods=['POST'])
def reply():
	data = request.get_json()
	post = posts.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 404
	post.replies.append(data['reply'])
	return jsonify({'message': 'Replied successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
