from flask import Blueprint, request, jsonify
import jwt
from models import User, Post, Message, Notification, users_db, posts_db, messages_db, notifications_db

views = Blueprint('views', __name__)

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(data['email'], data['username'], data['password'], data.get('profile_picture'), data.get('bio'), data.get('website_link'), data.get('location'), data.get('is_private', False))
	users_db[data['username']] = new_user
	return jsonify({'message': 'User registered successfully'}), 201

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == data['password']:
		token = jwt.encode({'username': user.username}, 'secret', algorithm='HS256')
		return jsonify({'token': token}), 200
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

@views.route('/profile/<username>', methods=['GET', 'PUT'])
def profile(username):
	user = users_db.get(username)
	if user:
		if request.method == 'GET':
			if not user.is_private:
				return jsonify({'username': user.username, 'email': user.email, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website_link': user.website_link, 'location': user.location, 'following': [users_db[username].username for username in user.following], 'followers': [users_db[username].username for username in user.followers]}), 200
			else:
				return jsonify({'message': 'Profile is private'}), 403
		elif request.method == 'PUT':
			data = request.get_json()
			if 'password' in data and user.password == data['password']:
				user.profile_picture = data.get('profile_picture', user.profile_picture)
				user.bio = data.get('bio', user.bio)
				user.website_link = data.get('website_link', user.website_link)
				user.location = data.get('location', user.location)
				user.is_private = data.get('is_private', user.is_private)
				return jsonify({'message': 'Profile updated successfully'}), 200
			else:
				return jsonify({'message': 'Invalid credentials'}), 401
	else:
		return jsonify({'message': 'User not found'}), 404

@views.route('/follow/<username>', methods=['POST'])
def follow(username):
	data = request.get_json()
	user = users_db.get(data['username'])
	to_follow = users_db.get(username)
	if user and 'password' in data and user.password == data['password'] and to_follow:
		user.following.append(username)
		to_follow.followers.append(user.username)
		new_notification = Notification(user.username, 'follow', to_follow.username)
		notifications_db[len(notifications_db)] = new_notification
		return jsonify({'message': 'User followed successfully'}), 200
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/unfollow/<username>', methods=['POST'])
def unfollow(username):
	data = request.get_json()
	user = users_db.get(data['username'])
	to_unfollow = users_db.get(username)
	if user and 'password' in data and user.password == data['password'] and to_unfollow and username in user.following:
		user.following.remove(username)
		to_unfollow.followers.remove(user.username)
		new_notification = Notification(user.username, 'unfollow', to_unfollow.username)
		notifications_db[len(notifications_db)] = new_notification
		return jsonify({'message': 'User unfollowed successfully'}), 200
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/feed', methods=['POST'])
def feed():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		feed = [post.to_dict() for post_id, post in posts_db.items() if post.user in user.following]
		return jsonify({'feed': feed}), 200
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		new_post = Post(data['text'], data.get('images'), user.username)
		posts_db[len(posts_db)] = new_post
		new_notification = Notification(user.username, 'post', len(posts_db)-1)
		notifications_db[len(notifications_db)] = new_notification
		return jsonify({'message': 'Post created successfully'}), 201
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def manage_post(post_id):
	post = posts_db.get(post_id)
	if request.method == 'GET':
		if post:
			return jsonify(post.to_dict()), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	elif request.method == 'DELETE':
		data = request.get_json()
		user = users_db.get(data['username'])
		if user and 'password' in data and user.password == data['password'] and post and post.user == user.username:
			del posts_db[post_id]
			new_notification = Notification(user.username, 'delete_post', post_id)
			notifications_db[len(notifications_db)] = new_notification
			return jsonify({'message': 'Post deleted successfully'}), 200
		else:
			return jsonify({'message': 'Invalid credentials or post not found'}), 401

@views.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		post = posts_db.get(post_id)
		if post:
			post.likes += 1
			new_notification = Notification(user.username, 'like', post_id)
			notifications_db[len(notifications_db)] = new_notification
			return jsonify({'message': 'Post liked successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

@views.route('/post/<int:post_id>/retweet', methods=['POST'])
def retweet_post(post_id):
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		post = posts_db.get(post_id)
		if post:
			post.retweets += 1
			new_notification = Notification(user.username, 'retweet', post_id)
			notifications_db[len(notifications_db)] = new_notification
			return jsonify({'message': 'Post retweeted successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

@views.route('/post/<int:post_id>/reply', methods=['POST'])
def reply_post(post_id):
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		post = posts_db.get(post_id)
		if post:
			post.replies.append(data['reply'])
			new_notification = Notification(user.username, 'reply', post_id)
			notifications_db[len(notifications_db)] = new_notification
			return jsonify({'message': 'Reply posted successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	else:
		return jsonify({'message': 'Invalid credentials'}), 401

@views.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	results = {'users': [], 'posts': []}
	for username, user in users_db.items():
		if query in username or query in user.bio:
			results['users'].append(username)
	for post_id, post in posts_db.items():
		if query in post.text:
			results['posts'].append(post_id)
	return jsonify(results), 200

@views.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = users_db.get(data['sender'])
	receiver = users_db.get(data['receiver'])
	if sender and 'password' in data and sender.password == data['password'] and receiver:
		new_message = Message(sender.username, receiver.username, data['text'])
		messages_db[len(messages_db)] = new_message
		new_notification = Notification(sender.username, 'message', receiver.username)
		notifications_db[len(notifications_db)] = new_notification
		return jsonify({'message': 'Message sent successfully'}), 201
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/messages', methods=['POST'])
def view_messages():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		messages = [message.to_dict() for message_id, message in messages_db.items() if message.receiver == user.username]
		return jsonify({'messages': messages}), 200
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/notifications', methods=['POST'])
def view_notifications():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and 'password' in data and user.password == data['password']:
		notifications = [notification.to_dict() for notification_id, notification in notifications_db.items() if notification.user == user.username]
		return jsonify({'notifications': notifications}), 200
	else:
		return jsonify({'message': 'Invalid credentials or user not found'}), 401

@views.route('/trending', methods=['GET'])
def trending():
	trending_posts = sorted(posts_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)[:10]
	return jsonify([post.to_dict() for post in trending_posts]), 200

@views.route('/recommendations/<username>', methods=['GET'])
def recommendations(username):
	user = users_db.get(username)
	if user:
		recommended_users = sorted(users_db.values(), key=lambda user: len(user.followers), reverse=True)
		recommended_users = [recommended_user for recommended_user in recommended_users if recommended_user.username not in user.following][:10]
		return jsonify([recommended_user.username for recommended_user in recommended_users]), 200
	else:
		return jsonify({'message': 'User not found'}), 404
