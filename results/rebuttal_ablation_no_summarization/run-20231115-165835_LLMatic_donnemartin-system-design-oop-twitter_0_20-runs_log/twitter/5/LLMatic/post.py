from datetime import datetime


class Post:
	def __init__(self, user, text, image=None):
		self.user = user
		self.text = text
		self.image = image
		self.timestamp = datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@classmethod
	def create_post(cls, user, text, image=None):
		return cls(user, text, image)

	def delete_post(self):
		self.user = None
		self.text = None
		self.image = None
		self.timestamp = None

	def like_post(self):
		self.likes += 1

	def unlike_post(self):
		if self.likes > 0:
			self.likes -= 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)

	def view_replies(self):
		return self.replies
