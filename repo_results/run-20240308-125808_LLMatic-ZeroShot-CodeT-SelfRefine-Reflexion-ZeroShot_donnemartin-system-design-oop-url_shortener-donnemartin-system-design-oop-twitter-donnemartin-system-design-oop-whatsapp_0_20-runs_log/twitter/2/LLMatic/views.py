from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify
from models import User, Post, Message, Notification
from collections import Counter

views = Blueprint('views', __name__)

users = {}
posts = {}
messages = {}
notifications = {}
hashtags = Counter()

@views.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'error': 'Email already registered'}), 400
	user = User(data['email'], data['username'], data['password'])
	users[data['email']] = user
	return jsonify({'message': 'User registered successfully'}), 200

@views.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['email'])
	if not user or not user.check_password(data['password']):
		return jsonify({'error': 'Invalid credentials'}), 400
	token = create_access_token(identity=user.email)
	return jsonify({'token': token}), 200

@views.route('/request-reset', methods=['POST'])
def request_reset():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	reset_token = user.get_reset_token()
	print(f'Password reset link: /reset-password?token={reset_token}')
	return jsonify({'message': 'Password reset link sent'}), 200

@views.route('/reset-password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = User.verify_reset_token(data['token'])
	if not user:
		return jsonify({'error': 'Invalid or expired token'}), 400
	user.password = data['new_password']
	return jsonify({'message': 'Password reset successful'}), 200

@views.route('/profile', methods=['GET', 'POST'])
def profile():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	if request.method == 'POST':
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		user.private = data.get('private', user.private)
		return jsonify({'message': 'Profile updated successfully'}), 200
	else:
		if user.private:
			return jsonify({'error': 'This profile is private'}), 403
		else:
			return jsonify({'email': user.email, 'username': user.username, 'profile_picture': user.profile_picture, 'bio': user.bio, 'website': user.website, 'location': user.location, 'followers': len(user.followers), 'following': len(user.following)}), 200

@views.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = users.get(data['email'])
	to_follow = users.get(data['to_follow'])
	if not user or not to_follow:
		return jsonify({'error': 'User not found'}), 400
	if to_follow.email in user.following:
		return jsonify({'error': 'Already following'}), 400
	user.following.append(to_follow.email)
	to_follow.followers.append(user.email)
	return jsonify({'message': 'Followed successfully'}), 200

@views.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	user = users.get(data['email'])
	to_unfollow = users.get(data['to_unfollow'])
	if not user or not to_unfollow:
		return jsonify({'error': 'User not found'}), 400
	if to_unfollow.email not in user.following:
		return jsonify({'error': 'Not following'}), 400
	user.following.remove(to_unfollow.email)
	to_unfollow.followers.remove(user.email)
	return jsonify({'message': 'Unfollowed successfully'}), 200

@views.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	post = Post(data['content'], data['images'], user, data.get('hashtags', []), data.get('mentions', []))
	for hashtag in post.hashtags:
		hashtags[hashtag] += 1
	posts[len(posts)] = post
	return jsonify({'message': 'Post created successfully'}), 200

@views.route('/post/<int:post_id>', methods=['GET', 'DELETE'])
def manage_post(post_id):
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	post = posts.get(post_id)
	if not post:
		return jsonify({'error': 'Post not found'}), 400
	if request.method == 'DELETE':
		if post.user != user:
			return jsonify({'error': 'You do not have permission to delete this post'}), 403
		del posts[post_id]
		return jsonify({'message': 'Post deleted successfully'}), 200
	else:
		return jsonify({'content': post.content, 'images': post.images, 'user': post.user.email, 'likes': post.likes, 'retweets': post.retweets, 'replies': post.replies, 'hashtags': post.hashtags, 'mentions': post.mentions}), 200

@views.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	post = posts.get(post_id)
	if not post:
		return jsonify({'error': 'Post not found'}), 400
	post.likes += 1
	for mentioned_user in post.mentions:
		if mentioned_user in users:
			notification = Notification(users[mentioned_user], f'{user.username} liked your post')
			users[mentioned_user].notifications.append(notification)
			notifications[len(notifications)] = notification
	return jsonify({'message': 'Post liked successfully', 'likes': post.likes}), 200

@views.route('/post/<int:post_id>/retweet', methods=['POST'])
def retweet_post(post_id):
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	post = posts.get(post_id)
	if not post:
		return jsonify({'error': 'Post not found'}), 400
	post.retweets += 1
	for mentioned_user in post.mentions:
		if mentioned_user in users:
			notification = Notification(users[mentioned_user], f'{user.username} retweeted your post')
			users[mentioned_user].notifications.append(notification)
			notifications[len(notifications)] = notification
	return jsonify({'message': 'Post retweeted successfully', 'retweets': post.retweets}), 200

@views.route('/post/<int:post_id>/reply', methods=['POST'])
def reply_post(post_id):
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	post = posts.get(post_id)
	if not post:
		return jsonify({'error': 'Post not found'}), 400
	post.replies.append(data['reply'])
	for mentioned_user in post.mentions:
		if mentioned_user in users:
			notification = Notification(users[mentioned_user], f'{user.username} replied to your post')
			users[mentioned_user].notifications.append(notification)
			notifications[len(notifications)] = notification
	return jsonify({'message': 'Reply posted successfully', 'replies': post.replies}), 200

@views.route('/search', methods=['GET'])
def search():
	data = request.get_json()
	keyword = data['keyword']
	results = {'users': [], 'posts': []}
	for email, user in users.items():
		if keyword in user.username or keyword in user.email:
			results['users'].append({'email': user.email, 'username': user.username})
	for post_id, post in posts.items():
		if keyword in post.content or keyword in post.hashtags or keyword in post.mentions:
			results['posts'].append({'post_id': post_id, 'content': post.content, 'hashtags': post.hashtags, 'mentions': post.mentions})
	return jsonify(results), 200

@views.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender = users.get(data['sender'])
	receiver = users.get(data['receiver'])
	if not sender or not receiver:
		return jsonify({'error': 'User not found'}), 400
	message = Message(sender, receiver, data['content'])
	messages[len(messages)] = message
	return jsonify({'message': 'Message sent successfully'}), 200

@views.route('/message/<int:message_id>', methods=['GET'])
def get_message(message_id):
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	message = messages.get(message_id)
	if not message:
		return jsonify({'error': 'Message not found'}), 400
	if message.sender != user and message.receiver != user:
		return jsonify({'error': 'You do not have permission to view this message'}), 403
	return jsonify({'sender': message.sender.email, 'receiver': message.receiver.email, 'content': message.content}), 200

@views.route('/notifications', methods=['GET'])
def get_notifications():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	return jsonify({'notifications': [notification.message for notification in user.notifications]}), 200

@views.route('/trending', methods=['GET'])
def trending():
	return jsonify(hashtags.most_common(10)), 200

@views.route('/recommend', methods=['GET'])
def recommend():
	data = request.get_json()
	user = users.get(data['email'])
	if not user:
		return jsonify({'error': 'User not found'}), 400
	recommendations = []
	for email, potential_follow in users.items():
		if potential_follow.email in user.following or potential_follow.email == user.email:
			continue
		mutual_followers = len(set(user.followers) & set(potential_follow.followers))
		if mutual_followers > 2:
			recommendations.append({'email': potential_follow.email, 'username': potential_follow.username, 'mutual_followers': mutual_followers})
	recommendations.sort(key=lambda x: x['mutual_followers'], reverse=True)
	return jsonify(recommendations[:10]), 200
