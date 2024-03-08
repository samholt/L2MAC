import hashlib
import jwt
from post import Post


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = self._hash_password(password)
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.followers = []
		self.posts = []
		self.notifications = []

	def _hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self, db):
		if self.email in db:
			return False
		db[self.email] = self
		return True

	def authenticate(self, db, password):
		if self.email not in db:
			return False
		user = db[self.email]
		return user.password == self._hash_password(password)

	def reset_password(self, db, new_password):
		if self.email not in db:
			return False
		user = db[self.email]
		user.password = self._hash_password(new_password)
		return True

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			user.receive_notification(f'{self.username} started following you.')

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post['timestamp'], reverse=True)

	def receive_notification(self, notification):
		self.notifications.append(notification)

