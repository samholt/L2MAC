import jwt
import datetime
from post import Post

SECRET_KEY = 'secret'


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = is_private
		self.authenticated = False
		self.following = []
		self.followers = []
		self.notifications = []
		self.posts = []

	def register(self):
		# In a real application, you would save these details in a database
		print(f'User {self.username} registered with email {self.email}')

	def authenticate(self, password):
		# In a real application, you would check the password hash in your database
		if self.password == password:
			self.authenticated = True
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return 'Invalid password'

	def reset_password(self, new_password):
		# In a real application, you would save the new password hash in your database
		self.password = new_password
		print(f'Password for user {self.username} has been reset')

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

	def view_notifications(self):
		return self.notifications
