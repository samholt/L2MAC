import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from post import Post
from message import Message
from notification import Notification

SECRET_KEY = 'secret'


class User:
	def __init__(self, username, email, password, profile_picture=None, bio=None, website=None, location=None, is_private=False):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.is_private = is_private
		self.authenticated = False
		self.posts = []
		self.following = []
		self.followers = []
		self.inbox = []
		self.blocked_users = []
		self.notifications = []

	def authenticate(self, password):
		if check_password_hash(self.password, password):
			self.authenticated = True
			return self.generate_auth_token()
		return None

	def generate_auth_token(self):
		payload = {
			'user': self.username,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
		}
		return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

	def is_authenticated(self):
		return self.authenticated

	def edit_profile(self, profile_picture=None, bio=None, website=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website is not None:
			self.website = website
		if location is not None:
			self.location = location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def create_post(self, text, images):
		post = Post(text, images, self)
		self.posts.append(post.create_post())

	def delete_post(self, post_index):
		if post_index < len(self.posts):
			del self.posts[post_index]

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def get_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post['timestamp'], reverse=True)

	def notify_followers(self):
		for follower in self.followers:
			print(f'{follower.username} has a new post!')

	def send_message(self, recipient, text):
		message = Message(self, recipient, text)
		self.inbox.append(message.send())
		return True

	def receive_message(self, sender, text):
		message = Message(sender, self, text)
		self.inbox.append(message.receive())
		return True

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)

	def receive_notification(self, notification_type, triggered_by):
		notification = Notification(notification_type, triggered_by, self)
		self.notifications.append(notification.get_notification())

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user not in self.following and user not in self.blocked_users:
				common_followers = len(set(self.followers) & set(user.followers))
				if common_followers > 0 or len(user.posts) > 0:
					recommendations.append((user, common_followers))
		return sorted(recommendations, key=lambda x: x[1], reverse=True)
