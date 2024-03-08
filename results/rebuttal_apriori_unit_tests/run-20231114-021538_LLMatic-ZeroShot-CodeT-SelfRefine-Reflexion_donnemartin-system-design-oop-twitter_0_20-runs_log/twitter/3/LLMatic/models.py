import datetime

class User:
	def __init__(self, id, username, email, password, profile_picture=None, bio=None, website=None, location=None):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.following = []
		self.followers = []


class Post:
	def __init__(self, id, user_id, content):
		self.id = id
		self.user_id = user_id
		self.content = content
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

class Message:
	def __init__(self, id, sender_id, receiver_id, content):
		self.id = id
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.content = content
		self.timestamp = datetime.datetime.now()
