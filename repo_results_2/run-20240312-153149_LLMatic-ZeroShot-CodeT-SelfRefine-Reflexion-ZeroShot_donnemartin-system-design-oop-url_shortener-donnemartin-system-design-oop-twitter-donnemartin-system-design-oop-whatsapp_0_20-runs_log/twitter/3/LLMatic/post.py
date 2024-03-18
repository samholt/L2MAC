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

	@staticmethod
	def create_post(user, content, image=None):
		return Post(user, content, image)

	@staticmethod
	def delete_post(post_dict, post_id):
		if post_id in post_dict:
			del post_dict[post_id]
			return True
		return False

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, user, content, image=None):
		reply = Post(user, content, image)
		self.replies.append(reply)
		return reply
