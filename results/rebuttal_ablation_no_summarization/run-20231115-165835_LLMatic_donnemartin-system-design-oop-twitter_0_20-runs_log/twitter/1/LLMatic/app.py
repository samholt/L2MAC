from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from dataclasses import dataclass, field
from collections import Counter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

users = {}
posts = {}
messages = {}

@app.route('/')
def home():
	return 'Hello, World!'

@dataclass
class Notification:
	user: str
	text: str

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	private: bool = False
	followers: list = field(default_factory=list)
	following: list = field(default_factory=list)
	notifications: list = field(default_factory=list)
	blocked_users: list = field(default_factory=list)

	def hash_password(self):
		self.password = generate_password_hash(self.password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture:
			self.profile_picture = profile_picture
		if bio:
			self.bio = bio
		if website_link:
			self.website_link = website_link
		if location:
			self.location = location

	def toggle_privacy(self):
		self.private = not self.private

	def follow(self, user):
		if user in users and user not in self.following:
			self.following.append(user)
			users[user].followers.append(self.username)
			users[user].notifications.append(Notification(self.username, f'{self.username} started following you.'))

	def unfollow(self, user):
		if user in users and user in self.following:
			self.following.remove(user)
			users[user].followers.remove(self.username)

	def block_user(self, user):
		if user in users and user not in self.blocked_users:
			self.blocked_users.append(user)

	def unblock_user(self, user):
		if user in users and user in self.blocked_users:
			self.blocked_users.remove(user)

	def timeline(self):
		timeline_posts = [post for user in self.following for post in posts.values() if post.user == user]
		return timeline_posts

	@staticmethod
	def search_user(keyword):
		return [user for user in users.values() if keyword in user.username]

	@staticmethod
	def recommend_users_to_follow(user):
		# Recommend users who are followed by the users that the given user is following
		recommended_users = [followed_user for following_user in users[user].following for followed_user in users[following_user].following if followed_user != user and followed_user not in users[user].following]
		return recommended_users

@dataclass
class Post:
	user: str
	text: str
	images: list = None
	likes: int = 0
	retweets: int = 0
	replies: list = field(default_factory=list)
	id: int = field(init=False)

	def __post_init__(self):
		self.id = len(posts)

	def create_post(self):
		if self.user in users:
			posts[self.id] = self
			return self
		else:
			return 'User does not exist'

	def delete_post(self, post_id):
		if post_id in posts and posts[post_id].user == self.user:
			del posts[post_id]
			return 'Post deleted successfully'
		else:
			return 'Post does not exist or user is not the owner'

	def like_post(self):
		self.likes += 1
		users[self.user].notifications.append(Notification(self.user, f'Your post has been liked.'))

	def retweet_post(self):
		self.retweets += 1
		users[self.user].notifications.append(Notification(self.user, f'Your post has been retweeted.'))

	def reply_to_post(self, reply):
		self.replies.append(reply)
		users[self.user].notifications.append(Notification(self.user, f'Your post has been replied to.'))

	@staticmethod
	def search_post(keyword):
		return [post for post in posts.values() if keyword in post.text]

	@staticmethod
	def filter_post(hashtag):
		return [post for post in posts.values() if hashtag in post.text]

	@staticmethod
	def trending_topics():
		# Identify and display trending hashtags based on volume and velocity of mentions
		hashtags = [word for post in posts.values() for word in post.text.split() if word.startswith('#')]
		trending_hashtags = Counter(hashtags).most_common(5)
		return trending_hashtags

@dataclass
class Message:
	text: str
	sender: str
	recipient: str
	id: int = field(init=False)

	def __post_init__(self):
		self.id = len(messages)

	def send_message(self):
		if self.sender in users and self.recipient in users and self.recipient not in users[self.sender].blocked_users:
			messages[self.id] = self
			users[self.recipient].notifications.append(Notification(self.recipient, f'You have a new message from {self.sender}.'))
			return self
		else:
			return 'User does not exist or recipient has blocked the sender'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(email=data['email'], username=data['username'], password=data['password'])
	new_user.hash_password()
	users[new_user.username] = new_user
	return jsonify({'message': 'registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users.get(data['username'])
	if not user or not user.check_password(data['password']):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'user': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

if __name__ == '__main__':
	app.run(debug=True)
