from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt
import collections

app = Flask(__name__)

users_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}

@dataclass
class User:
	email: str
	username: str
	password: str
	following: list = field(default_factory=list)
	blocked: list = field(default_factory=list)
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	is_private: bool = False

	def follow(self, user):
		if user not in self.following and user not in self.blocked:
			self.following.append(user)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)

	def block(self, user):
		if user not in self.blocked:
			self.blocked.append(user)
		if user in self.following:
			self.following.remove(user)

	def unblock(self, user):
		if user in self.blocked:
			self.blocked.remove(user)

@dataclass
class Message:
	sender: User
	receiver: User
	content: str

@dataclass
class Comment:
	user: User
	content: str

@dataclass
class Post:
	user: User
	content: str
	hashtags: list = field(default_factory=list)
	images: list = None
	likes: int = 0
	retweets: int = 0
	comments: list = field(default_factory=list)

@dataclass
class Notification:
	user: User
	content: str

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	follower_email = data.get('follower_email')
	followee_email = data.get('followee_email')

	follower = users_db.get(follower_email)
	followee = users_db.get(followee_email)

	if not follower or not followee:
		return jsonify({'message': 'User not found'}), 404

	follower.follow(followee)

	return jsonify({'message': 'User followed successfully'}), 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	follower_email = data.get('follower_email')
	followee_email = data.get('followee_email')

	follower = users_db.get(follower_email)
	followee = users_db.get(followee_email)

	if not follower or not followee:
		return jsonify({'message': 'User not found'}), 404

	follower.unfollow(followee)

	return jsonify({'message': 'User unfollowed successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	sender_email = data.get('sender_email')
	receiver_email = data.get('receiver_email')
	content = data.get('content')

	sender = users_db.get(sender_email)
	receiver = users_db.get(receiver_email)

	if not sender or not receiver:
		return jsonify({'message': 'User not found'}), 404

	if receiver in sender.blocked:
		return jsonify({'message': 'Cannot send message, user is blocked'}), 403

	message = Message(sender, receiver, content)
	messages_db[id(message)] = message

	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/block', methods=['POST'])
def block():
	data = request.get_json()
	blocker_email = data.get('blocker_email')
	blockee_email = data.get('blockee_email')

	blocker = users_db.get(blocker_email)
	blockee = users_db.get(blockee_email)

	if not blocker or not blockee:
		return jsonify({'message': 'User not found'}), 404

	blocker.block(blockee)

	return jsonify({'message': 'User blocked successfully'}), 200

@app.route('/unblock', methods=['POST'])
def unblock():
	data = request.get_json()
	blocker_email = data.get('blocker_email')
	blockee_email = data.get('blockee_email')

	blocker = users_db.get(blocker_email)
	blockee = users_db.get(blockee_email)

	if not blocker or not blockee:
		return jsonify({'message': 'User not found'}), 404

	blocker.unblock(blockee)

	return jsonify({'message': 'User unblocked successfully'}), 200

@app.route('/timeline', methods=['GET'])
def timeline():
	email = request.args.get('email')

	user = users_db.get(email)

	if not user:
		return jsonify({'message': 'User not found'}), 404

	timeline_posts = [post for post in posts_db.values() if post.user in user.following]

	return jsonify({'posts': [post.__dict__ for post in timeline_posts]}), 200

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	user_email = data.get('user_email')
	content = data.get('content')

	user = users_db.get(user_email)

	if not user:
		return jsonify({'message': 'User not found'}), 404

	notification = Notification(user, content)
	notifications_db[id(notification)] = notification

	return jsonify({'message': 'Notification created successfully'}), 200

@app.route('/get_notifications', methods=['GET'])
def get_notifications():
	user_email = request.args.get('user_email')

	user = users_db.get(user_email)

	if not user:
		return jsonify({'message': 'User not found'}), 404

	user_notifications = [notification for notification in notifications_db.values() if notification.user == user]

	return jsonify({'notifications': [notification.__dict__ for notification in user_notifications]}), 200

@app.route('/get_trending_topics', methods=['GET'])
def get_trending_topics():
	# Extract hashtags from posts
	hashtags = [hashtag for post in posts_db.values() for hashtag in post.hashtags]

	# Count frequency of each hashtag
	hashtag_counts = collections.Counter(hashtags)

	# Get the 10 most common hashtags
	trending_topics = hashtag_counts.most_common(10)

	return jsonify({'trending_topics': trending_topics}), 200

@app.route('/recommend_users', methods=['GET'])
def recommend_users():
	user_email = request.args.get('user_email')

	user = users_db.get(user_email)

	if not user:
		return jsonify({'message': 'User not found'}), 404

	# Get users that the current user is not following
	not_following = [u for u in users_db.values() if u not in user.following and u != user]

	# Recommend users based on mutual followers
	recommended_users = sorted(not_following, key=lambda u: len(set(user.following) & set(u.following)), reverse=True)

	# If there are less than 10 users, return all users
	if len(recommended_users) < 10:
		return jsonify({'recommended_users': [u.__dict__ for u in recommended_users]}), 200

	# Otherwise, return the top 10 users
	return jsonify({'recommended_users': [u.__dict__ for u in recommended_users[:10]]}), 200
