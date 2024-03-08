class Post:
	def __init__(self, user, text, images=None):
		self.user = user
		self.text = text
		self.images = images if images else []
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create_post(self):
		return {'user': self.user, 'text': self.text, 'images': self.images, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies}

	def delete_post(self):
		self.text = None
		self.images = None
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, reply):
		self.replies.append(reply)
