from flask import Flask, request, jsonify
import hashlib
import jwt
import datetime
from dataclasses import dataclass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Mock databases
users_db = {}
posts_db = {}
notifications_db = {}
trending_db = {}

# User dataclass
class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website=None, location=None, private=False, followers=None, following=None):
		self.email = email
		self.username = username
		self.password = hashlib.sha256(password.encode()).hexdigest()
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.private = private
		self.followers = followers if followers else []
		self.following = following if following else []

# Post dataclass
class Post:
	def __init__(self, text, images, username):
		self.text = text
		self.images = images
		self.username = username

# Notification dataclass
class Notification:
	def __init__(self, text, username):
		self.text = text
		self.username = username

# TrendingTopic dataclass
class TrendingTopic:
	def __init__(self, text, mentions):
		self.text = text
		self.mentions = mentions

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	users_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/toggle_privacy', methods=['POST'])
def toggle_privacy():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		user.private = not user.private
		return jsonify({'message': 'Privacy setting updated', 'private': user.private}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		post = Post(data['text'], data['images'], data['username'])
		posts_db[len(posts_db)] = post
		return jsonify({'message': 'Post created successfully'}), 201
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/view_posts', methods=['GET'])
def view_posts():
	return jsonify({'posts': [{i: {'text': post.text, 'images': post.images, 'username': post.username}} for i, post in posts_db.items()]}), 200

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		del posts_db[data['post_id']]
		return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	results = [post for post in posts_db.values() if keyword in post.text]
	return jsonify({'results': [{'text': post.text, 'images': post.images, 'username': post.username} for post in results]}), 200

@app.route('/filter', methods=['GET'])
def filter():
	filter = request.args.get('filter')
	results = [post for post in posts_db.values() if filter in post.text]
	return jsonify({'results': [{'text': post.text, 'images': post.images, 'username': post.username} for post in results]}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = users_db.get(data['username'])
	to_follow = users_db.get(data['to_follow'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		if to_follow and not user.private:
			user.following.append(to_follow.username)
			to_follow.followers.append(user.username)
			return jsonify({'message': 'Followed successfully'}), 200
		return jsonify({'message': 'User not found or user is private'}), 400
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = users_db.get(data['username'])
	to_unfollow = users_db.get(data['to_unfollow'])
	if user and user.password == hashlib.sha256(data['password'].encode()).hexdigest():
		if to_unfollow and to_unfollow.username in user.following:
			user.following.remove(to_unfollow.username)
			to_unfollow.followers.remove(user.username)
			return jsonify({'message': 'Unfollowed successfully'}), 200
		return jsonify({'message': 'User not found or not following'}), 400
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/timeline', methods=['GET'])
def timeline():
	username = request.args.get('username')
	user = users_db.get(username)
	if user:
		timeline_posts = [post for post in posts_db.values() if post.username in user.following]
		return jsonify({'timeline': [{'text': post.text, 'images': post.images, 'username': post.username} for post in timeline_posts]}), 200
	return jsonify({'message': 'User not found'}), 400

@app.route('/notifications', methods=['GET'])
def notifications():
	username = request.args.get('username')
	user_notifications = [notification for notification in notifications_db.values() if notification.username == username]
	return jsonify({'notifications': [{'text': notification.text, 'username': notification.username} for notification in user_notifications]}), 200

@app.route('/trending', methods=['GET'])
def trending():
	return jsonify({'trending': [{'text': topic.text, 'mentions': topic.mentions} for topic in trending_db.values()]}), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	username = request.args.get('username')
	user = users_db.get(username)
	if user:
		recommendations = [u for u in users_db.values() if u.username != user.username and len(set(user.following) & set(u.followers)) > 0]
		return jsonify({'recommendations': [u.username for u in recommendations]}), 200
	return jsonify({'message': 'User not found'}), 400

if __name__ == '__main__':
	app.run(debug=True)
