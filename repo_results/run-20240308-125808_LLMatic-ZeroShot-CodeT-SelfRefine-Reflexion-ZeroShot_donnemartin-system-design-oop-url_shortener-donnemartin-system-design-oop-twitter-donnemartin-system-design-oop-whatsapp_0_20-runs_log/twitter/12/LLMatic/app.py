from flask import Flask, request, jsonify
from user import User
from post import Post
from notification import Notification

app = Flask(__name__)

users = {}
posts = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['id'])
	if user and user.check_password(data['password']):
		return jsonify({'auth_token': user.generate_auth_token('secret_key')})
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(**data)
	posts[post.id] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/like', methods=['POST'])
def like():
	data = request.get_json()
	post = posts.get(data['post_id'])
	if post:
		post.like()
		return jsonify({'message': 'Post liked'}), 200
	return jsonify({'message': 'Post not found'}), 404

@app.route('/notifications', methods=['GET'])
def notifications():
	user_id = request.args.get('user_id')
	return jsonify([notification.__dict__ for notification in Notification.view_notifications(user_id)]), 200

@app.route('/trending', methods=['GET'])
def trending():
	return jsonify({'trending_hashtags': Post.get_trending_hashtags(posts.values())}), 200

if __name__ == '__main__':
	app.run()

