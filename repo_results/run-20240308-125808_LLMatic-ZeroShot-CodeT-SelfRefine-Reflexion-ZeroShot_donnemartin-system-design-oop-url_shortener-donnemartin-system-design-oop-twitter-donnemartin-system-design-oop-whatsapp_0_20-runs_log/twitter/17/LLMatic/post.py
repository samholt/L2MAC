import datetime


class Post:
	def __init__(self, user, content, image=None):
		self.user = user
		self.content = content
		self.image = image
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create(self):
		return {'user': self.user, 'content': self.content, 'image': self.image, 'timestamp': self.timestamp, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies}

	def delete(self):
		self.user = None
		self.content = None
		self.image = None
		self.timestamp = None
		self.likes = None
		self.retweets = None
		self.replies = None
		return True

	def like(self):
		self.likes += 1
		return self.likes

	def retweet(self):
		self.retweets += 1
		return self.retweets

	def reply(self, reply_content):
		reply = Post(self.user, reply_content)
		self.replies.append(reply.create())
		return self.replies

