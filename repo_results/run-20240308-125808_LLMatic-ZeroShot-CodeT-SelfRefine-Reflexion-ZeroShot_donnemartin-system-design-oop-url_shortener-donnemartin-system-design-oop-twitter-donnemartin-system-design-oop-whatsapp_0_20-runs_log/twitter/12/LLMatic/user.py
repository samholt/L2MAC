import hashlib
import jwt
import datetime


class User:
	def __init__(self, id, email, username, password, profile_picture, bio, website_link, location):
		self.id = id
		self.email = email
		self.username = username
		self.password = self.hash_password(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.followers = []
		self.blocked_users = []
		self.messages = []
		self.notifications = []

	def hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == self.hash_password(password)

	def generate_auth_token(self, secret_key):
		payload = {
			'user_id': self.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
		}
		return jwt.encode(payload, secret_key, algorithm='HS256')

	def update_profile(self, profile_picture, bio, website_link, location):
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		return self

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			user.notifications.append(f'{self.username} started following you.')

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def send_message(self, user, message):
		if user not in self.blocked_users and self not in user.blocked_users:
			self.messages.append((user, message))
			user.messages.append((self, message))

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user != self and len(set(self.following) & set(user.followers)) > 0:
				recommendations.append(user)
		return recommendations[:5]
