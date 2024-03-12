from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt
from collections import Counter
import re

app = Flask(__name__)

# Mock databases
users_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}

# User dataclass
@dataclass
class User:
	email: str
	username: str
	password: str
	following: list = None
	followers: list = None
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	privacy_setting: str = 'public'

# Post dataclass
@dataclass
class Post:
	content: str
	images: list
	author: str

# Message dataclass
@dataclass
class Message:
	content: str
	sender: str
	recipient: str

# Notification dataclass
@dataclass
class Notification:
	content: str
	recipient: str

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'], [], [])
	users_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == data['password']:
		token = jwt.encode({'username': user.username}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		if request.method == 'GET':
			return jsonify(user.__dict__), 200
		elif request.method == 'PUT':
			update_data = request.get_json()
			user.profile_picture = update_data.get('profile_picture', user.profile_picture)
			user.bio = update_data.get('bio', user.bio)
			user.website_link = update_data.get('website_link', user.website_link)
			user.location = update_data.get('location', user.location)
			user.privacy_setting = update_data.get('privacy_setting', user.privacy_setting)
			return jsonify({'message': 'Profile updated successfully'}), 200
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/post', methods=['POST', 'DELETE'])
def post():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		if request.method == 'POST':
			post_data = request.get_json()
			post = Post(post_data['content'], post_data.get('images', []), user.username)
			posts_db[post.content] = post
			return jsonify({'message': 'Post created successfully'}), 201
		elif request.method == 'DELETE':
			post_data = request.get_json()
			post = posts_db.get(post_data['content'])
			if post and post.author == user.username:
				del posts_db[post.content]
				return jsonify({'message': 'Post deleted successfully'}), 200
			return jsonify({'message': 'Post not found or unauthorized'}), 404
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/follow', methods=['POST'])
def follow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		follow_data = request.get_json()
		follow_user = users_db.get(follow_data['username'])
		if follow_user and follow_user.username not in user.following:
			user.following.append(follow_user.username)
			follow_user.followers.append(user.username)
			return jsonify({'message': 'User followed successfully'}), 200
		return jsonify({'message': 'User not found or already followed'}), 404
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/unfollow', methods=['POST'])
def unfollow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		unfollow_data = request.get_json()
		unfollow_user = users_db.get(unfollow_data['username'])
		if unfollow_user and unfollow_user.username in user.following:
			user.following.remove(unfollow_user.username)
			unfollow_user.followers.remove(user.username)
			return jsonify({'message': 'User unfollowed successfully'}), 200
		return jsonify({'message': 'User not found or not followed'}), 404
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/timeline', methods=['GET'])
def timeline():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		timeline_posts = [post.__dict__ for post in posts_db.values() if post.author in user.following]
		return jsonify({'posts': timeline_posts}), 200
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	matching_users = [user.__dict__ for user in users_db.values() if query in user.username]
	matching_posts = [post.__dict__ for post in posts_db.values() if query in post.content]
	return jsonify({'users': matching_users, 'posts': matching_posts}), 200

@app.route('/filter', methods=['GET'])
def filter():
	hashtags = request.args.getlist('hashtags')
	mentions = request.args.getlist('mentions')
	trending = request.args.get('trending')
	filtered_posts = [post.__dict__ for post in posts_db.values() if any(hashtag in post.content for hashtag in hashtags) or any(mention in post.content for mention in mentions) or (trending and trending in post.content)]
	return jsonify({'posts': filtered_posts}), 200

@app.route('/message', methods=['POST', 'GET'])
def message():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		if request.method == 'POST':
			message_data = request.get_json()
			message = Message(message_data['content'], user.username, message_data['recipient'])
			messages_db[message.content] = message
			return jsonify({'message': 'Message sent successfully'}), 201
		elif request.method == 'GET':
			received_messages = [message.__dict__ for message in messages_db.values() if message.recipient == user.username]
			return jsonify({'messages': received_messages}), 200
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/notifications', methods=['GET'])
def notifications():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		user_notifications = [notification.__dict__ for notification in notifications_db.values() if notification.recipient == user.username]
		return jsonify({'notifications': user_notifications}), 200
	except:
		return jsonify({'message': 'Token is invalid'}), 401

@app.route('/trending', methods=['GET'])
def trending():
	# Extract all hashtags from all posts
	hashtags = [re.findall(r'#\w+', post.content) for post in posts_db.values()]
	# Flatten the list of lists
	hashtags = [hashtag for sublist in hashtags for hashtag in sublist]
	# Count the occurrences of each hashtag
	hashtag_counts = Counter(hashtags)
	# Get the 10 most common hashtags
	trending_hashtags = hashtag_counts.most_common(10)
	return jsonify({'trending': trending_hashtags}), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
		# Get the users that the current user is not already following
		unfollowed_users = [u for u in users_db.values() if u.username not in user.following]
		# Sort the users by the number of mutual followers
		unfollowed_users.sort(key=lambda u: len(set(user.followers) & set(u.followers)), reverse=True)
		# Return the top 5 users as recommendations
		recommendations = [u.__dict__ for u in unfollowed_users[:5]]
		return jsonify({'recommendations': recommendations}), 200
	except:
		return jsonify({'message': 'Token is invalid'}), 401

if __name__ == '__main__':
	app.run(debug=True)
