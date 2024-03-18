from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt

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
	profile: dict

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(len(users), data['username'], data['email'], data['password'], {})
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
			return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	user_id = jwt.decode(data['token'], 'secret', algorithms=['HS256'])['user_id']
	post = Post(len(posts), user_id, data['content'], 0, 0, [])
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post_id = data['post_id']
	if post_id in posts:
		posts[post_id].likes += 1
		return jsonify({'message': 'Post liked'}), 200
	else:
		return jsonify({'message': 'Post not found'}), 404

@app.route('/retweet', methods=['POST'])
def retweet():
	data = request.get_json()
	post_id = data['post_id']
	if post_id in posts:
		posts[post_id].retweets += 1
		return jsonify({'message': 'Post retweeted'}), 200
	else:
		return jsonify({'message': 'Post not found'}), 404

@app.route('/reply', methods=['POST'])
def reply():
	data = request.get_json()
	post_id = data['post_id']
	reply = data['reply']
	if post_id in posts:
		posts[post_id].replies.append(reply)
		return jsonify({'message': 'Reply posted'}), 200
	else:
		return jsonify({'message': 'Post not found'}), 404

@app.route('/posts', methods=['GET'])
def get_posts():
	return jsonify({'posts': [post.__dict__ for post in posts.values()]}), 200

if __name__ == '__main__':
	app.run(debug=True)
