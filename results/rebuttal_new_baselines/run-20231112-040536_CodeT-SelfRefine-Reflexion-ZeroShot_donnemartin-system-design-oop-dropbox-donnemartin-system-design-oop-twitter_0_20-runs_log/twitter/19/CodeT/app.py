from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt

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
	username = data['username']
	email = data['email']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = User(username, email, password, {})
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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	data = request.get_json()
	username = data['username']
	if 'token' not in data or jwt.decode(data['token'], 'secret', algorithms=['HS256'])['username'] != username:
		return jsonify({'message': 'Invalid token'}), 400
	if request.method == 'GET':
		return jsonify(users[username].profile), 200
	elif request.method == 'POST':
		users[username].profile = data['profile']
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	username = data['username']
	content = data['content']
	if 'token' not in data or jwt.decode(data['token'], 'secret', algorithms=['HS256'])['username'] != username:
		return jsonify({'message': 'Invalid token'}), 400
	posts[len(posts)] = Post(username, content, 0, 0, [])
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post_id = data['post_id']
	if post_id not in posts:
		return jsonify({'message': 'Post not found'}), 404
	posts[post_id].likes += 1
	return jsonify({'message': 'Post liked successfully'}), 200

@app.route('/retweet', methods=['POST'])
def retweet():
	data = request.get_json()
	post_id = data['post_id']
	if post_id not in posts:
		return jsonify({'message': 'Post not found'}), 404
	posts[post_id].retweets += 1
	return jsonify({'message': 'Post retweeted successfully'}), 200

@app.route('/reply', methods=['POST'])
def reply():
	data = request.get_json()
	post_id = data['post_id']
	reply = data['reply']
	if post_id not in posts:
		return jsonify({'message': 'Post not found'}), 404
	posts[post_id].replies.append(reply)
	return jsonify({'message': 'Reply posted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
