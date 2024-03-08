from flask import Flask, request, jsonify
from dataclasses import dataclass, field
from typing import Dict, Optional, List
import jwt
from collections import Counter

app = Flask(__name__)

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: Optional[str] = None
	bio: Optional[str] = None
	website_link: Optional[str] = None
	location: Optional[str] = None
	following: List[str] = field(default_factory=list)
	followers: List[str] = field(default_factory=list)

@dataclass
class Post:
	user: User
	text: str
	images: List[str]
	likes: int = 0
	retweets: int = 0
	replies: int = 0

@dataclass
class Message:
	sender: str
	receiver: str
	text: str

@dataclass
class Notification:
	user: User
	type: str
	post: Optional[Post] = None

mock_db: Dict[str, User] = {}
post_db: Dict[int, Post] = {}
message_db: Dict[int, Message] = {}
notification_db: Dict[int, Notification] = {}
post_id: int = 0
message_id: int = 0
notification_id: int = 0

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	mock_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db.get(data['username'])
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
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if request.method == 'GET':
		return jsonify(user.__dict__), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		return jsonify(user.__dict__), 200

@app.route('/follow', methods=['POST', 'DELETE'])
def follow():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	data = request.get_json()
	to_follow = mock_db.get(data['to_follow'])
	if not to_follow:
		return jsonify({'message': 'User to follow not found'}), 404
	if request.method == 'POST':
		user.following.append(to_follow.username)
		to_follow.followers.append(user.username)
		global notification_id
		notification = Notification(user, 'follow')
		notification_db[notification_id] = notification
		notification_id += 1
		return jsonify({'message': 'Followed user'}), 200
	elif request.method == 'DELETE':
		if to_follow.username in user.following:
			user.following.remove(to_follow.username)
		if user.username in to_follow.followers:
			to_follow.followers.remove(user.username)
		return jsonify({'message': 'Unfollowed user'}), 200

@app.route('/posts', methods=['GET', 'POST'])
def posts():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if request.method == 'POST':
		data = request.get_json()
		if not user:
			return jsonify({'message': 'User not found'}), 404
		post = Post(user, data['text'], data['images'])
		global post_id
		post_db[post_id] = post
		post_id += 1
		global notification_id
		notification = Notification(user, 'post', post)
		notification_db[notification_id] = notification
		notification_id += 1
		return jsonify({'message': 'Post created', 'post_id': post_id-1}), 201
	elif request.method == 'GET':
		filter = request.args.get('filter')
		if filter:
			filtered_posts = {id: post for id, post in post_db.items() if filter in post.text}
			return jsonify(filtered_posts), 200
		return jsonify({id: post.__dict__ for id, post in post_db.items() if post.user.username in user.following}), 200

@app.route('/notifications', methods=['GET'])
def notifications():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify({id: notification.__dict__ for id, notification in notification_db.items() if notification.user.username == user.username}), 200

@app.route('/messages', methods=['GET', 'POST'])
def messages():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if request.method == 'POST':
		data = request.get_json()
		receiver = mock_db.get(data['receiver'])
		if not receiver:
			return jsonify({'message': 'Receiver not found'}), 404
		message = Message(user.username, receiver.username, data['text'])
		global message_id
		message_db[message_id] = message
		message_id += 1
		return jsonify({'message': 'Message sent', 'message_id': message_id-1}), 201
	elif request.method == 'GET':
		return jsonify({id: message.__dict__ for id, message in message_db.items() if message.receiver == user.username}), 200

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	if not query:
		return jsonify({'message': 'Query parameter is missing'}), 400
	matched_users = {username: user.__dict__ for username, user in mock_db.items() if query in user.username}
	matched_posts = {id: post.__dict__ for id, post in post_db.items() if query in post.text}
	return jsonify({'users': matched_users, 'posts': matched_posts}), 200

@app.route('/trending', methods=['GET'])
def trending():
	# Extract all hashtags from all posts
	hashtags = [word for post in post_db.values() for word in post.text.split() if word.startswith('#')]
	# Count the frequency of each hashtag
	counter = Counter(hashtags)
	# Get the top 10 trending hashtags
	trending = counter.most_common(10)
	return jsonify({'trending': trending}), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	token = request.headers.get('Authorization')
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, 'secret', algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user = mock_db.get(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	# Get the users that the current user is not already following
	not_following = [username for username in mock_db if username not in user.following and username != user.username]
	# Sort the users by the number of mutual followers
	not_following.sort(key=lambda username: len(set(user.followers) & set(mock_db[username].followers)), reverse=True)
	# Get the top 10 user recommendations
	recommendations = not_following[:10]
	return jsonify({'recommendations': recommendations}), 200

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
