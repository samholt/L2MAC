import hashlib
import binascii
import os
from post import Post


class User:
	def __init__(self, id, email, username, password, is_private):
		self.id = id
		self.email = email
		self.username = username
		self.password = self.hash_password(password)
		self.is_private = is_private
		self.profile_picture = None
		self.bio = None
		self.website_link = None
		self.location = None
		self.following = set()
		self.followers = set()
		self.notifications = []
		self.posts = []
		self.blocked_users = set()

	def hash_password(self, password):
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		pwdhash = binascii.hexlify(pwdhash)
		return (salt + pwdhash).decode('ascii')

	def verify_password(self, provided_password):
		salt = self.password[:64]
		stored_password = self.password[64:]
		pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')
		return pwdhash == stored_password

	def reset_password(self, new_password):
		self.password = self.hash_password(new_password)

	def update_profile_picture(self, new_picture):
		self.profile_picture = new_picture

	def update_bio(self, new_bio):
		self.bio = new_bio

	def update_website_link(self, new_website_link):
		self.website_link = new_website_link

	def update_location(self, new_location):
		self.location = new_location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user.username not in self.following:
			self.following.add(user.username)
			user.followers.add(self.username)
			user.notifications.append(f'{self.username} started following you.')

	def unfollow(self, user):
		if user.username in self.following:
			self.following.remove(user.username)
			user.followers.remove(self.username)

	def view_timeline(self, user_db):
		timeline = []
		for username in self.following:
			user = user_db.users[username]
			timeline.extend(user.posts)
		timeline.sort(key=lambda post: post.timestamp, reverse=True)
		return timeline

	def notify(self, notification):
		self.notifications.append(notification)

	def recommend_users(self, user_db):
		recommended_users = []
		for user in user_db.users.values():
			if user.username not in self.following and user.username != self.username:
				mutual_followers = self.followers.intersection(user.followers)
				if len(mutual_followers) > 0:
					recommended_users.append(user.username)
		return recommended_users


class UserDatabase:
	def __init__(self):
		self.users = {}

	def register(self, id, email, username, password, is_private):
		if username in self.users:
			return False
		self.users[username] = User(id, email, username, password, is_private)
		return True

	def authenticate(self, username, password):
		if username in self.users:
			user = self.users[username]
			return user.verify_password(password)
		return False

