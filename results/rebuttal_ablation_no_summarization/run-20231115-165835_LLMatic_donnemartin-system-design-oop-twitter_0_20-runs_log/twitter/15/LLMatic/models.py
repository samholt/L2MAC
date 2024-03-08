from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User:
	def __init__(self, id, email, username, password, profile_picture, bio, website_link, location):
		self.id = id
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password) if password else None
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = False
		self.posts = []
		self.likes = []
		self.following = []
		self.followers = []

	def check_password(self, password):
		return check_password_hash(self.password_hash, password) if self.password_hash else False

	def search(self, keyword):
		# TODO: Implement search functionality
		pass

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)


class Post:
	def __init__(self, id, user_id, text, image):
		self.id = id
		self.user_id = user_id
		self.text = text
		self.image = image
		self.timestamp = datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.hashtags = [word for word in text.split() if word.startswith('#')]

	def delete(self):
		# Mock delete operation
		self.id = None
		self.user_id = None
		self.text = None
		self.image = None
		self.timestamp = None

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)
