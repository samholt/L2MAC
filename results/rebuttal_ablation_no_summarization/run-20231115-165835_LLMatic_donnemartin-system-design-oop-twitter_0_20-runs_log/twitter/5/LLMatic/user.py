import hashlib
from post import Post


class User:
	def __init__(self, email, username, password, is_private=False, profile_picture=None, bio=None, website=None, location=None):
		self.email = email
		self.username = username
		self.password = self._hash_password(password)
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.following = []
		self.followers = []
		self.posts = []
		self.notifications = []

	def _hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def authenticate(self, username, password):
		if self.username == username and self.password == self._hash_password(password):
			return self
		return None

	def reset_password(self, new_password):
		self.password = self._hash_password(new_password)
		return self

	def update_profile(self, profile_picture=None, bio=None, website=None, location=None):
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

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def add_notification(self, notification):
		self.notifications.append(notification)

	def view_notifications(self):
		return self.notifications

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user != self and len(set(self.following) & set(user.followers)) > 0:
				recommendations.append(user)
		return sorted(recommendations, key=lambda user: len(set(self.following) & set(user.followers)), reverse=True)

