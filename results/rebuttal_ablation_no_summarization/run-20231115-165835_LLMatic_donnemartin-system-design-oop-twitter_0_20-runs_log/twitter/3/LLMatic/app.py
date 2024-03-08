from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt

app = Flask(__name__)

mock_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}
trending_db = {}

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = field(default='')
	bio: str = field(default='')
	website_link: str = field(default='')
	location: str = field(default='')
	is_private: bool = field(default=False)
	following: list = field(default_factory=list)
	followers: list = field(default_factory=list)
	blocked: list = field(default_factory=list)

@dataclass
class Post:
	text: str
	images: list
	user: User

@dataclass
class Message:
	sender: str
	receiver: str
	text: str

@dataclass
class Notification:
	user: User
	text: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	mock_db[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		token = jwt.encode({'username': user.username}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website_link = data.get('website_link', user.website_link)
		user.location = data.get('location', user.location)
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/toggle_privacy', methods=['POST'])
def toggle_privacy():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		user.is_private = not user.is_private
		return jsonify({'message': 'Profile privacy toggled successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = mock_db.get(data['username'])
	to_follow = mock_db.get(data['to_follow'])
	if user and user.password == data['password'] and to_follow:
		user.following.append(to_follow.username)
		to_follow.followers.append(user.username)
		return jsonify({'message': 'Followed successfully'}), 200
	return jsonify({'message': 'Invalid username or password or user to follow not found'}), 401

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = mock_db.get(data['username'])
	to_unfollow = mock_db.get(data['to_unfollow'])
	if user and user.password == data['password'] and to_unfollow:
		user.following.remove(to_unfollow.username)
		to_unfollow.followers.remove(user.username)
		return jsonify({'message': 'Unfollowed successfully'}), 200
	return jsonify({'message': 'Invalid username or password or user to unfollow not found'}), 401

@app.route('/block', methods=['POST'])
def block():
	data = request.get_json()
	user = mock_db.get(data['username'])
	to_block = mock_db.get(data['to_block'])
	if user and user.password == data['password'] and to_block:
		user.blocked.append(to_block.username)
		return jsonify({'message': 'Blocked successfully'}), 200
	return jsonify({'message': 'Invalid username or password or user to block not found'}), 401

@app.route('/unblock', methods=['POST'])
def unblock():
	data = request.get_json()
	user = mock_db.get(data['username'])
	to_unblock = mock_db.get(data['to_unblock'])
	if user and user.password == data['password'] and to_unblock:
		user.blocked.remove(to_unblock.username)
		return jsonify({'message': 'Unblocked successfully'}), 200
	return jsonify({'message': 'Invalid username or password or user to unblock not found'}), 401

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = mock_db.get(data['sender'])
	receiver = mock_db.get(data['receiver'])
	if sender and sender.password == data['password'] and receiver and receiver.username not in sender.blocked:
		message = Message(sender.username, receiver.username, data['text'])
		messages_db[len(messages_db)] = message
		return jsonify({'message': 'Message sent successfully'}), 200
	return jsonify({'message': 'Invalid sender or password or receiver not found or blocked'}), 401

@app.route('/timeline', methods=['POST'])
def timeline():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		timeline_posts = [post for post in posts_db.values() if post.user.username in user.following]
		return jsonify({'timeline': [post.text for post in timeline_posts]}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		post = Post(data['text'], data['images'], user)
		posts_db[len(posts_db)] = post
		# Update trending topics
		for word in post.text.split():
			if word.startswith('#'):
				trending_db[word] = trending_db.get(word, 0) + 1
		return jsonify({'message': 'Post created successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/trending', methods=['GET'])
def trending():
	# Get top 5 trending topics
	trending_topics = sorted(trending_db.items(), key=lambda x: x[1], reverse=True)[:5]
	return jsonify({'trending': trending_topics}), 200

@app.route('/search', methods=['POST'])
def search():
	data = request.get_json()
	keyword = data.get('keyword')
	results = [post for post in posts_db.values() if keyword in post.text]
	return jsonify({'results': [post.text for post in results]}), 200

@app.route('/recommendations', methods=['POST'])
def recommendations():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		# Recommend users who are followed by the users that the current user is following
		recommended_users = set()
		for following in user.following:
			for follower in mock_db[following].following:
				if follower not in user.following and follower not in user.blocked:
					recommended_users.add(follower)
		return jsonify({'recommendations': list(recommended_users)}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and user.password == data['password']:
		notification = Notification(user, data['text'])
		notifications_db[len(notifications_db)] = notification
		return jsonify({'message': 'Notification created successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/')
def home():
	return 'Hello, World!', 200

if __name__ == '__main__':
	app.run(debug=True)
