from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt
from collections import Counter
import time

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
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	privacy_setting: str = 'public'
	following: list = field(default_factory=list)
	followers: list = field(default_factory=list)

# Post dataclass
@dataclass
class Post:
	user: str
	content: str
	timestamp: float
	images: list = field(default_factory=list)

# Message dataclass
@dataclass
class Message:
	sender: str
	recipient: str
	content: str

# Notification dataclass
@dataclass
class Notification:
	user: str
	type: str
	post_or_message: str

@app.route('/')
def home():
	return 'Hello, World!'

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
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if request.method == 'GET':
		return jsonify(user.__dict__), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		user.privacy_setting = data.get('privacy_setting', user.privacy_setting)
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST'])
def post():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	data = request.get_json()
	post = Post(user.username, data['content'], time.time(), data.get('images'))
	posts_db[len(posts_db)] = post
	return jsonify({'message': 'Post created successfully'}), 201

@app.route('/follow', methods=['POST'])
def follow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	data = request.get_json()
	user_to_follow = users_db.get(data['username_to_follow'])
	if user_to_follow:
		user.following.append(user_to_follow.username)
		user_to_follow.followers.append(user.username)
		return jsonify({'message': 'User followed successfully'}), 200
	return jsonify({'message': 'User to follow not found'}), 404

@app.route('/unfollow', methods=['POST'])
def unfollow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	data = request.get_json()
	user_to_unfollow = users_db.get(data['username_to_unfollow'])
	if user_to_unfollow:
		user.following.remove(user_to_unfollow.username)
		user_to_unfollow.followers.remove(user.username)
		return jsonify({'message': 'User unfollowed successfully'}), 200
	return jsonify({'message': 'User to unfollow not found'}), 404

@app.route('/message', methods=['POST'])
def message():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		sender = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	data = request.get_json()
	recipient = users_db.get(data['recipient'])
	if not recipient:
		return jsonify({'message': 'Recipient not found'}), 404
	message = Message(sender.username, recipient.username, data['content'])
	messages_db[len(messages_db)] = message
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/notifications', methods=['GET'])
def notifications():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	notifications = [notification.__dict__ for notification in notifications_db.values() if notification.user == user.username]
	return jsonify({'notifications': notifications}), 200

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	matching_users = [user.__dict__ for user in users_db.values() if keyword in user.username]
	matching_posts = [post.__dict__ for post in posts_db.values() if keyword in post.content]
	return jsonify({'users': matching_users, 'posts': matching_posts}), 200

@app.route('/filter', methods=['GET'])
def filter():
	criteria = request.args.get('criteria')
	filtered_posts = [post.__dict__ for post in posts_db.values() if criteria in post.content]
	return jsonify({'posts': filtered_posts}), 200

@app.route('/trending', methods=['GET'])
def trending():
	# Extract hashtags from posts
	hashtags = [word for post in posts_db.values() for word in post.content.split() if word.startswith('#')]
	# Count occurrences of each hashtag
	hashtag_counts = Counter(hashtags)
	# Get the top 10 trending hashtags
	trending = hashtag_counts.most_common(10)
	return jsonify({'trending': trending}), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
		user = users_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	# Get the users that the current user is not following
	not_following = [u for u in users_db.values() if u.username not in user.following]
	# Sort the users by the number of mutual followers
	not_following.sort(key=lambda u: len(set(user.followers) & set(u.followers)), reverse=True)
	# Return the top 5 users as recommendations
	recommendations = [u.__dict__ for u in not_following[:5]]
	return jsonify({'recommendations': recommendations}), 200

if __name__ == '__main__':
	app.run(debug=True)
