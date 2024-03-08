from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt
from datetime import datetime

app = Flask(__name__)

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = field(default='')
	bio: str = field(default='')
	website_link: str = field(default='')
	location: str = field(default='')
	privacy_setting: str = field(default='public')

@dataclass
class Post:
	author: str
	content: str
	timestamp: datetime = field(default_factory=datetime.now)
	image: str = field(default='')

@dataclass
class Follow:
	follower: str
	followee: str

@dataclass
class Message:
	sender: str
	recipient: str
	content: str

@dataclass
class Notification:
	recipient: str
	type: str
	related_user: str = field(default='')
	related_post: str = field(default='')

mock_db = {'users': {}, 'posts': {}, 'follows': {}, 'messages': {}, 'notifications': {}}

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	mock_db['users'][user.username] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db['users'].get(data['username'])
	if user and user.password == data['password']:
		token = jwt.encode({'username': user.username}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	if request.method == 'POST':
		data = request.get_json()
		user = mock_db['users'].get(data['username'])
		if user:
			user.profile_picture = data.get('profile_picture', '')
			user.bio = data.get('bio', '')
			user.website_link = data.get('website_link', '')
			user.location = data.get('location', '')
			user.privacy_setting = data.get('privacy_setting', 'public')
			return jsonify({'message': 'Profile updated successfully'}), 200
		return jsonify({'message': 'User not found'}), 404
	else:
		username = request.args.get('username')
		user = mock_db['users'].get(username)
		if user:
			return jsonify({'username': user.username, 'email': user.email, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website_link': user.website_link, 'location': user.location, 'privacy_setting': user.privacy_setting}), 200
		return jsonify({'message': 'User not found'}), 404

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	post = Post(data['author'], data['content'], image=data.get('image', ''))
	mock_db['posts'][post.timestamp] = post
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	follow = Follow(data['follower'], data['followee'])
	mock_db['follows'][follow.follower] = follow
	return jsonify({'message': 'Followed successfully'}), 200

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	message = Message(data['sender'], data['recipient'], data['content'])
	mock_db['messages'][message.sender] = message
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
	if request.method == 'POST':
		data = request.get_json()
		notification = Notification(data['recipient'], data['type'], related_user=data.get('related_user', ''), related_post=data.get('related_post', ''))
		mock_db['notifications'][notification.recipient] = notification
		return jsonify({'message': 'Notification created successfully'}), 200
	else:
		recipient = request.args.get('recipient')
		notification = mock_db['notifications'].get(recipient)
		if notification:
			return jsonify({'recipient': notification.recipient, 'type': notification.type, 'related_user': notification.related_user, 'related_post': notification.related_post}), 200
		return jsonify({'message': 'No notifications found'}), 404

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	results = {'users': [], 'posts': []}
	for username, user in mock_db['users'].items():
		if query in username or query in user.bio:
			results['users'].append(username)
	for timestamp, post in mock_db['posts'].items():
		if query in post.content:
			results['posts'].append(post.content)
	return jsonify(results), 200

@app.route('/trending', methods=['GET'])
def trending():
	location = request.args.get('location')
	trending_topics = []  # This should be replaced with actual logic to get trending topics
	return jsonify({'trending_topics': trending_topics}), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	username = request.args.get('username')
	user_recommendations = []  # This should be replaced with actual logic to get user recommendations
	return jsonify({'user_recommendations': user_recommendations}), 200

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = [u for u in mock_db['users'].values() if u.email == data['email']]
	if user:
		token = jwt.encode({'email': user[0].email}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Email not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
