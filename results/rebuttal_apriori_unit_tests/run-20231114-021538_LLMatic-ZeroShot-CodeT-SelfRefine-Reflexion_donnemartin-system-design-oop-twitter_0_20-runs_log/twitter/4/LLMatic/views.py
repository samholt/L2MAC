from flask import Flask, request, jsonify
from models import User, users_db, register_user, authenticate_user, edit_user_profile, create_post, delete_post, like_post, retweet_post, create_reply
from utils import search_users, search_posts
import jwt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	email = data['email']
	password = data['password']
	if register_user(username, email, password):
		return jsonify({'message': 'User registered successfully'}), 201
	return jsonify({'message': 'Registration failed'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if authenticate_user(email, password):
		for user in users_db.values():
			if user.email == email:
				token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
				return jsonify({'token': token.decode('UTF-8')}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user_id = data['user_id']
	profile_picture = data['profile_picture']
	bio = data['bio']
	website = data['website']
	location = data['location']
	if edit_user_profile(user_id, profile_picture, bio, website, location):
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Profile update failed'}), 400

@app.route('/create_post', methods=['POST'])
def create_post_route():
	data = request.get_json()
	user_id = data['user_id']
	content = data['content']
	if create_post(user_id, content):
		return jsonify({'message': 'Post created successfully'}), 201
	return jsonify({'message': 'Post creation failed'}), 400

@app.route('/delete_post', methods=['DELETE'])
def delete_post_route():
	data = request.get_json()
	user_id = data['user_id']
	post_id = data['post_id']
	if delete_post(user_id, post_id):
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Post deletion failed'}), 400

@app.route('/like_post', methods=['POST'])
def like_post_route():
	data = request.get_json()
	user_id = data['user_id']
	post_id = data['post_id']
	if like_post(user_id, post_id):
		return jsonify({'message': 'Post liked successfully'}), 200
	return jsonify({'message': 'Failed to like post'}), 400

@app.route('/retweet_post', methods=['POST'])
def retweet_post_route():
	data = request.get_json()
	user_id = data['user_id']
	post_id = data['post_id']
	if retweet_post(user_id, post_id):
		return jsonify({'message': 'Post retweeted successfully'}), 200
	return jsonify({'message': 'Failed to retweet post'}), 400

@app.route('/reply_to_post', methods=['POST'])
def reply_to_post_route():
	data = request.get_json()
	user_id = data['user_id']
	post_id = data['post_id']
	content = data['content']
	if create_reply(user_id, post_id, content):
		return jsonify({'message': 'Reply created successfully'}), 201
	return jsonify({'message': 'Failed to create reply'}), 400

@app.route('/search_users', methods=['GET'])
def search_users_route():
	keyword = request.args.get('keyword')
	results = search_users(keyword)
	return jsonify({'results': [user.to_dict() for user in results]}), 200

@app.route('/search_posts', methods=['GET'])
def search_posts_route():
	keyword = request.args.get('keyword')
	results = search_posts(keyword)
	return jsonify({'results': [post.to_dict() for post in results]}), 200
