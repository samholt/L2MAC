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
		self.following = []
		self.followers = []
		self.messages = []
		self.notifications = []


class Post:
	def __init__(self, text, images=None, user=None):
		self.text = text
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def to_dict(self):
		return {
			'text': self.text,
			'images': self.images,
			'user': self.user,
			'likes': self.likes,
			'retweets': self.retweets,
			'replies': self.replies
		}

class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text

	def to_dict(self):
		return {
			'sender': self.sender,
			'receiver': self.receiver,
			'text': self.text
		}

class Notification:
	def __init__(self, user, notification_type, related_user_or_post):
		self.user = user
		self.notification_type = notification_type
		self.related_user_or_post = related_user_or_post

	def to_dict(self):
		return {
			'user': self.user,
			'notification_type': self.notification_type,
			'related_user_or_post': self.related_user_or_post
		}


users_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}
