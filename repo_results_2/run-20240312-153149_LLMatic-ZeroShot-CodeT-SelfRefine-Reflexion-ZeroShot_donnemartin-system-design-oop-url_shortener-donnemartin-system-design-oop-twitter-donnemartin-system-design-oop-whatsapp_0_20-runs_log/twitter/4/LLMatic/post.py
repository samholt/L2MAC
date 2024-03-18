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

	def create(self):
		return {'user': self.user, 'content': self.content, 'image': self.image, 'timestamp': str(self.timestamp)}

	def delete(self):
		self.user = None
		self.content = None
		self.image = None
		self.timestamp = None
		return {'status': 'Post deleted'}

	def like(self):
		self.likes += 1
		return {'status': 'Post liked', 'likes': self.likes}

	def retweet(self):
		self.retweets += 1
		return {'status': 'Post retweeted', 'retweets': self.retweets}

	def reply(self, user, content):
		reply = Post(user, content)
		self.replies.append(reply)
		return {'status': 'Reply posted', 'reply': reply.create()}
