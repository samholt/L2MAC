from flask import Blueprint, request, jsonify
from models import User, Post
from database import users, posts
from collections import Counter

views = Blueprint('views', __name__)


@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['email'], data['username'], data['password'])
	users[new_user.email] = new_user
	return jsonify({'message': 'Registered successfully'}), 200


@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or not user.check_password(data['password']):
		return jsonify({'error': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200


@views.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = users.get(data['email'])
	to_follow = users.get(data['to_follow'])
	if not user or not to_follow:
		return jsonify({'error': 'User not found'}), 404
	user.follow(to_follow)
	return jsonify({'message': 'Followed successfully'}), 200


@views.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = users.get(data['email'])
	to_unfollow = users.get(data['to_unfollow'])
	if not user or not to_unfollow:
		return jsonify({'error': 'User not found'}), 404
	user.unfollow(to_unfollow)
	return jsonify({'message': 'Unfollowed successfully'}), 200


@views.route('/following_posts', methods=['GET'])
def following_posts():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 404
	posts = [post.content for follow in user.following for post in follow.posts]
	return jsonify({'posts': posts}), 200


@views.route('/search', methods=['POST'])
def search():
	keyword = request.get_json().get('keyword')
	search_results = {'users': [user.email for user in users.values() if keyword in user.username], 'posts': [post.content for post in posts if keyword in post.content]}
	return jsonify(search_results), 200


@views.route('/trending', methods=['GET'])
def trending():
	hashtags = [hashtag for post in posts for hashtag in post.hashtags]
	trending_topics = [item[0] for item in Counter(hashtags).most_common(3)]
	return jsonify({'trending': trending_topics}), 200


@views.route('/recommend', methods=['GET'])
def recommend():
	email = request.json.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	recommendations = sorted([u for u in users.values() if u != user and u not in user.following], key=lambda u: (len(set(user.following) & set(u.followers)), len(u.posts), len(set(hashtag for post in u.posts for hashtag in post.hashtags) & set(hashtag for post in user.posts for hashtag in post.hashtags))), reverse=True)[:3]
	return jsonify({'recommendations': [u.email for u in recommendations]}), 200
