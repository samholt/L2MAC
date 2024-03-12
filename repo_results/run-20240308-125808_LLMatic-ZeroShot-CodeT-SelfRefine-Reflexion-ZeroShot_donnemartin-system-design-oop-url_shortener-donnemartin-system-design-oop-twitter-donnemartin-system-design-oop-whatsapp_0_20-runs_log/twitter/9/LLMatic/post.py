import datetime


class Post:
	def __init__(self, user_id, text, image=None):
		self.user_id = user_id
		self.text = text[:280]
		self.image = image
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@classmethod
	def create_post(cls, user_id, text, image=None):
		return cls(user_id, text, image)

	def delete_post(self):
		self.user_id = None
		self.text = None
		self.image = None
		self.timestamp = None
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, user_id, text, image=None):
		reply = Post(user_id, text, image)
		self.replies.append(reply)
