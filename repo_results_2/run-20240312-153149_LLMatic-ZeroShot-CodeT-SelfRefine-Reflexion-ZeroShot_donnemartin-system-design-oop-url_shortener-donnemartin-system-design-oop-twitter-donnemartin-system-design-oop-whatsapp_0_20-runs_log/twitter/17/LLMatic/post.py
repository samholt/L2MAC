from datetime import datetime


class Post:
	def __init__(self, user, content, image=None):
		self.user = user
		self.content = content
		self.image = image
		self.timestamp = datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@classmethod
	def create_post(cls, user, content, image=None):
		return cls(user, content, image)

	def delete_post(self):
		self.user = None
		self.content = None
		self.image = None
		self.timestamp = None

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)

	def get_replies(self):
		return self.replies
