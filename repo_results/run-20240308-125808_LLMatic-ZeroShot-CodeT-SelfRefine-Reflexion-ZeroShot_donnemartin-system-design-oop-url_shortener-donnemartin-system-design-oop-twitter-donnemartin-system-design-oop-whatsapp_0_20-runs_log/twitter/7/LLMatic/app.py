from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

mock_db = {}
mock_posts_db = {}
mock_messages_db = {}
mock_notifications_db = {}


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website=None, location=None, visibility='public', following=None, followers=None):
		self.email = email
		self.username = username
		self.password = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.visibility = visibility
		self.following = following if following else []
		self.followers = followers if followers else []


class Post:
	def __init__(self, content, images, author):
		self.content = content
		self.images = images
		self.author = author


class Message:
	def __init__(self, sender, recipient, content):
		self.sender = sender
		self.recipient = recipient
		self.content = content


class Notification:
	def __init__(self, recipient, content):
		self.recipient = recipient
		self.content = content


@app.route('/')
def home():
	return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['email'], data['username'], data['password'])
	mock_db[new_user.username] = new_user
	return jsonify({'message': 'Registered successfully'}), 200


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = mock_db.get(data['username'])
	if user and check_password_hash(user.password, data['password']):
		token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if request.method == 'GET':
		return jsonify({'username': user.username, 'email': user.email, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website': user.website, 'location': user.location, 'visibility': user.visibility, 'following': user.following, 'followers': user.followers}), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		user.visibility = data.get('visibility', user.visibility)
		return jsonify({'message': 'Profile updated successfully'}), 200


@app.route('/post', methods=['POST'])
def post():
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	data = request.get_json()
	new_post = Post(data['content'], data['images'], user.username)
	mock_posts_db[len(mock_posts_db)] = new_post
	return jsonify({'message': 'Post created successfully'}), 200


@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	results = {'users': [], 'posts': []}
	for username, user in mock_db.items():
		if query in username or query in user.email:
			results['users'].append(username)
	for post_id, post in mock_posts_db.items():
		if query in post.content:
			results['posts'].append(post_id)
	return jsonify(results), 200


@app.route('/follow/<username>', methods=['POST'])
def follow(username):
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
		to_follow = mock_db.get(username)
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if not to_follow:
		return jsonify({'message': 'User to follow not found'}), 404
	user.following.append(username)
	to_follow.followers.append(user.username)
	new_notification = Notification(to_follow.username, f'{user.username} started following you.')
	mock_notifications_db[len(mock_notifications_db)] = new_notification
	return jsonify({'message': 'Followed successfully'}), 200


@app.route('/unfollow/<username>', methods=['POST'])
def unfollow(username):
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
		to_unfollow = mock_db.get(username)
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if not to_unfollow:
		return jsonify({'message': 'User to unfollow not found'}), 404
	user.following.remove(username)
	to_unfollow.followers.remove(user.username)
	return jsonify({'message': 'Unfollowed successfully'}), 200


@app.route('/timeline', methods=['GET'])
def timeline():
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	timeline_posts = [post for post_id, post in mock_posts_db.items() if post.author in user.following]
	return jsonify({'timeline': [post.content for post in timeline_posts]}), 200


@app.route('/message/<username>', methods=['POST'])
def message(username):
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
		recipient = mock_db.get(username)
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if not recipient:
		return jsonify({'message': 'Recipient not found'}), 404
	data = request.get_json()
	new_message = Message(user.username, username, data['content'])
	mock_messages_db[len(mock_messages_db)] = new_message
	new_notification = Notification(recipient.username, f'You have a new message from {user.username}.')
	mock_notifications_db[len(mock_notifications_db)] = new_notification
	return jsonify({'message': 'Message sent successfully'}), 200


@app.route('/messages', methods=['GET'])
def messages():
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user_messages = [message for message_id, message in mock_messages_db.items() if message.recipient == user.username]
	return jsonify({'messages': [message.content for message in user_messages]}), 200


@app.route('/block/<username>', methods=['POST'])
def block(username):
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
		to_block = mock_db.get(username)
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	if not to_block:
		return jsonify({'message': 'User to block not found'}), 404
	user.following.remove(username)
	to_block.followers.remove(user.username)
	return jsonify({'message': 'Blocked successfully'}), 200


@app.route('/notifications', methods=['GET'])
def notifications():
	token = request.headers.get('Authorization').split(' ')[1]
	if not token:
		return jsonify({'message': 'Token is missing'}), 401
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		user = mock_db.get(data['username'])
	except:
		return jsonify({'message': 'Token is invalid'}), 401
	user_notifications = [notification for notification_id, notification in mock_notifications_db.items() if notification.recipient == user.username]
	return jsonify({'notifications': [notification.content for notification in user_notifications]}), 200


if __name__ == '__main__':
	app.run(debug=True)
