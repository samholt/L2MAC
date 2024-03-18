import hashlib
import jwt


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = self._encrypt_password(password)
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.posts = []
		self.notifications = []

	def _encrypt_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self):
		print(f'User {self.username} registered with email {self.email}')

	def authenticate(self, password):
		return self.password == self._encrypt_password(password)

	def reset_password(self, new_password):
		self.password = self._encrypt_password(new_password)
		print(f'Password for user {self.username} has been reset.')

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location
		print(f'Profile for user {self.username} has been updated.')

	def toggle_privacy(self):
		self.is_private = not self.is_private
		print(f'Privacy for user {self.username} has been toggled.')

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.notify_new_follower(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)

	def get_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def notify_new_follower(self, follower):
		print(f'User {follower.username} started following you.')
		self.notifications.append(f'User {follower.username} started following you.')

	def notify(self, notification):
		self.notifications.append(notification)
		print(notification)

