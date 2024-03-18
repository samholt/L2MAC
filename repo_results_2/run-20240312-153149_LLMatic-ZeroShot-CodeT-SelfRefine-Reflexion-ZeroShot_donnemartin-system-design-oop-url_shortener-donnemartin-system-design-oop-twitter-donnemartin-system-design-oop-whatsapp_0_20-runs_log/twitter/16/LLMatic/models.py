class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.followers = []
		self.notifications = []


class Post:
	def __init__(self, text, images, user):
		self.text = text
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.replies = []


class Message:
	def __init__(self, sender, recipient, text):
		self.sender = sender
		self.recipient = recipient
		self.text = text

# In-memory database
users_db = {}
posts_db = {}
messages_db = {}
