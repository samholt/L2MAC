from flask import Flask, request, jsonify
from models import User, Post, Like, Notification, users_db, posts_db, likes_db, notifications_db

app = Flask(__name__)

@app.route('/view_notifications/<username>', methods=['GET'])
def view_notifications(username):
	user = users_db.get(username)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	notifications = [notification.view_notification() for notification in notifications_db.values() if notification.user == user]
	return jsonify({'notifications': notifications}), 200

@app.route('/like_post', methods=['POST'])
def like_post():
	data = request.get_json()
	username = data.get('username')
	post_id = data.get('post_id')
	like_id = data.get('like_id')
	user = users_db.get(username)
	post = posts_db.get(post_id)
	if not user or not post or not like_id:
		return jsonify({'message': 'Invalid input'}), 400
	if like_id in likes_db:
		return jsonify({'message': 'Like already exists'}), 400
	new_like = Like(like_id, user, post)
	likes_db[like_id] = new_like
	notification_id = f'notif_{like_id}'
	new_notification = Notification(notification_id, post.user, 'like', post)
	notifications_db[notification_id] = new_notification
	return jsonify({'message': 'Post liked successfully'}), 201

@app.route('/trending', methods=['GET'])
def trending():
	# Mock trending topics
	trending_topics = ['topic1', 'topic2', 'topic3']
	return jsonify({'trending': trending_topics}), 200

@app.route('/recommendations/<username>', methods=['GET'])
def recommendations(username):
	# Mock user recommendations
	recommendations = ['user1', 'user2', 'user3']
	return jsonify({'recommendations': recommendations}), 200
