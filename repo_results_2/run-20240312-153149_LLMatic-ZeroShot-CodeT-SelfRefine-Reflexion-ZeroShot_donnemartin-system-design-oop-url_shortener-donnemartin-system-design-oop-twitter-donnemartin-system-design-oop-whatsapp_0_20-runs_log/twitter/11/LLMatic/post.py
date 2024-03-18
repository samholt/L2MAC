import datetime

class Post:
	def __init__(self, user, text, image=None, mentions=None):
		self.user = user
		self.text = text
		self.image = image
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.mentions = mentions if mentions else []

	def create(self):
		return {'user': self.user, 'text': self.text, 'image': self.image, 'timestamp': self.timestamp, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies, 'mentions': self.mentions}

	def delete(self):
		self.user = None
		self.text = None
		self.image = None
		self.timestamp = None
		self.likes = None
		self.retweets = None
		self.replies = None
		self.mentions = None
		return True

	def like(self):
		self.likes += 1
		return self.likes

	def retweet(self):
		self.retweets += 1
		return self.retweets

	def reply(self, user, text):
		reply = Post(user, text)
		self.replies.append(reply.create())
		return self.replies
