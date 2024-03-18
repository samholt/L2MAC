class Post:
	def __init__(self, text, images=None, hashtags=None, topics=None):
		self.text = text
		self.images = images if images else []
		self.hashtags = hashtags if hashtags else []
		self.topics = topics if topics else []
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)

	def delete(self):
		self.text = ''
		self.images = []
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.hashtags = []
		self.topics = []

	@staticmethod
	def search(posts, keyword):
		return [post for post in posts if keyword in post.text]
