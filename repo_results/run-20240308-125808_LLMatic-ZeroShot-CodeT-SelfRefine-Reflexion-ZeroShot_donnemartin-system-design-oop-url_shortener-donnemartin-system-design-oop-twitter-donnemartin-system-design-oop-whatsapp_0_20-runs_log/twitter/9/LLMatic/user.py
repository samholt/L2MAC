import hashlib
import binascii
import os
from post import Post
from notification import Notification


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website=None, location=None):
		self.email = email
		self.username = username
		self.password = self.hash_password(password)
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.following = set()
		self.posts = []
		self.notifications = []

	@staticmethod
	def hash_password(password):
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

	def follow_user(self, user):
		if user.is_private:
			return False
		self.following.add(user)
		return True

	def unfollow_user(self, user):
		if user in self.following:
			self.following.remove(user)
			return True
		return False

	def view_timeline(self):
		timeline = [post for user in self.following for post in user.posts]
		timeline.sort(key=lambda post: post.timestamp, reverse=True)
		return timeline

	def receive_notification(self, type):
		self.notifications.append(Notification(self.email, type))

	def recommend_users(self):
		# Mock implementation of user recommendation based on interests, activity, and mutual followers
		# In a real-world scenario, this would involve complex algorithms and machine learning
		# For this task, we will return a list of users who are not currently being followed by the user
		return [user for user in USERS.values() if user not in self.following]


USERS = {}


def register(email, username, password, is_private, profile_picture=None, bio=None, website=None, location=None):
	if email in USERS:
		return False
	user = User(email, username, password, is_private, profile_picture, bio, website, location)
	USERS[email] = user
	return True


def authenticate(email, password):
	if email not in USERS:
		return False
	user = USERS[email]
	return user if user.verify_password(password) else False
