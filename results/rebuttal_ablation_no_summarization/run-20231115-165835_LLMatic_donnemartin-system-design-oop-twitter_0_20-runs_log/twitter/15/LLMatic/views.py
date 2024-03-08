from flask import Blueprint, request, jsonify
from models import User, Post

views = Blueprint('views', __name__)

mock_db = {'users': {}, 'posts': {}}

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['username'] in mock_db['users']:
		return jsonify({'message': 'Username already exists'}), 400
	mock_db['users'][data['username']] = User(len(mock_db['users']), data['email'], data['username'], data['password'], '', '', '', '')
	return jsonify({'message': 'User registered successfully'}), 200

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db['users'].get(data['username'])
	if user and user.check_password(data['password']):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid username or password'}), 400

@views.route('/profile/<username>', methods=['GET'])
def profile(username):
	user = mock_db['users'].get(username)
	if user:
		return jsonify(user.__dict__), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	user = mock_db['users'].get(data['username'])
	if user:
		post = Post(len(mock_db['posts']), user.id, data['text'], data['image'])
		user.posts.append(post)
		mock_db['posts'][post.id] = post
		return jsonify({'message': 'Post created'}), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/posts/<username>', methods=['GET'])
def user_posts(username):
	user = mock_db['users'].get(username)
	if user:
		return jsonify([post.__dict__ for post in user.posts]), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = mock_db['users'].get(data['username'])
	follow_user = mock_db['users'].get(data['follow_username'])
	if user and follow_user:
		user.follow(follow_user)
		return jsonify({'message': 'Followed user'}), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = mock_db['users'].get(data['username'])
	unfollow_user = mock_db['users'].get(data['unfollow_username'])
	if user and unfollow_user:
		user.unfollow(unfollow_user)
		return jsonify({'message': 'Unfollowed user'}), 200
	return jsonify({'message': 'User not found'}), 404
