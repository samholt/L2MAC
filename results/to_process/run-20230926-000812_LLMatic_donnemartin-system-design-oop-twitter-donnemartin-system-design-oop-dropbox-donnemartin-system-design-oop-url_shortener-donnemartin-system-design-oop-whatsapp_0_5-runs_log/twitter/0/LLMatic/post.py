from datetime import datetime
from user import User

class Post:
	def __init__(self, text, images, author):
		self.text = text
		self.images = images
		self.author = author
		self.timestamp = datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def delete_post(self):
		self.text = None
		self.images = None
		self.author = None
		self.timestamp = None

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, reply):
		self.replies.append(reply)

