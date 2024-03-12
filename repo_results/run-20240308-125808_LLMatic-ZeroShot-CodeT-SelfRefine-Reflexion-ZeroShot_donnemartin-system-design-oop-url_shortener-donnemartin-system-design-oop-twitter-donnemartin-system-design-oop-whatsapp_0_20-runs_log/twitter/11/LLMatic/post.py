class Post:
	def __init__(self, post_id, text, images, author_id, timestamp):
		self.post_id = post_id
		self.text = text
		self.images = images
		self.author_id = author_id
		self.timestamp = timestamp
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@classmethod
	def create(cls, post_id, text, images, author_id, timestamp):
		return cls(post_id, text, images, author_id, timestamp)

	@staticmethod
	def delete(posts_db, post_id):
		if post_id in posts_db:
			del posts_db[post_id]
			return True
		return False

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)
