import datetime
class Post:
	def __init__(self, text, images, user):
		self.text = text
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.comments = []
		self.timestamp = datetime.datetime.utcnow()

	def create_post(self):
		return {'text': self.text, 'images': self.images, 'user': self.user.username, 'likes': self.likes, 'retweets': self.retweets, 'comments': [comment.create_comment() for comment in self.comments], 'timestamp': self.timestamp}

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, comment):
		self.comments.append(comment.create_comment())

