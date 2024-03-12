from flask import Blueprint, request, jsonify
from models import User, Post, users_db, posts_db
import uuid
import collections

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return 'Hello, World!'

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['email'], data['username'], data['password'])
	users_db[data['email']] = new_user
	return jsonify({'message': 'User registered successfully'}), 200

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@views.route('/reset-password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		token = str(uuid.uuid4())
		user.reset_token = token
		return jsonify({'message': 'Password reset token generated', 'token': token}), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/confirm-reset', methods=['POST'])
def confirm_reset():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and user.reset_token == data['token']:
		user.reset_password(data['new_password'])
		return jsonify({'message': 'Password reset successfully'}), 200
	return jsonify({'message': 'Invalid token or user not found'}), 404

@views.route('/update-profile', methods=['PUT'])
def update_profile():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		user.update_profile(data['profile_picture'], data['bio'], data['website_link'], data['location'])
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/create-post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user:
		new_post = Post(user, data['text'], data['images'])
		posts_db[str(uuid.uuid4())] = new_post
		return jsonify({'message': 'Post created successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@views.route('/delete-post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	if user and data['post_id'] in posts_db:
		del posts_db[data['post_id']]
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Post not found'}), 404

@views.route('/like-post', methods=['POST'])
def like_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	post = posts_db.get(data['post_id'])
	if user and post:
		post.like(user)
		return jsonify({'message': 'Post liked successfully'}), 200
	return jsonify({'message': 'Post or user not found'}), 404

@views.route('/retweet-post', methods=['POST'])
def retweet_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	post = posts_db.get(data['post_id'])
	if user and post:
		post.retweet(user)
		return jsonify({'message': 'Post retweeted successfully'}), 200
	return jsonify({'message': 'Post or user not found'}), 404

@views.route('/reply-post', methods=['POST'])
def reply_post():
	data = request.get_json()
	user = users_db.get(data['email'])
	post = posts_db.get(data['post_id'])
	if user and post:
		post.reply(user, data['text'])
		return jsonify({'message': 'Reply posted successfully'}), 200
	return jsonify({'message': 'Post or user not found'}), 404

@views.route('/search', methods=['GET'])
def search():
	query = request.args.get('query')
	matching_users = [user for user in users_db.values() if query in user.username]
	matching_posts = [post for post in posts_db.values() if query in post.text]
	return jsonify({'users': [user.to_dict() for user in matching_users], 'posts': [post.to_dict() for post in matching_posts]}), 200

@views.route('/filter', methods=['GET'])
def filter():
	filter_type = request.args.get('type')
	filter_value = request.args.get('value')
	if filter_type == 'hashtags':
		matching_posts = [post for post in posts_db.values() if filter_value in post.text.split()]
	elif filter_type == 'user_mentions':
		matching_posts = [post for post in posts_db.values() if filter_value in post.text.split()]
	elif filter_type == 'trending_topics':
		# For simplicity, assume that the trending topics are the most common words in the posts
		words = [word for post in posts_db.values() for word in post.text.split()]
		trending_topics = [word for word, count in collections.Counter(words).most_common(10)]
		matching_posts = [post for post in posts_db.values() if filter_value in trending_topics]
	else:
		return jsonify({'message': 'Invalid filter type'}), 400
	return jsonify({'posts': [post.to_dict() for post in matching_posts]}), 200
