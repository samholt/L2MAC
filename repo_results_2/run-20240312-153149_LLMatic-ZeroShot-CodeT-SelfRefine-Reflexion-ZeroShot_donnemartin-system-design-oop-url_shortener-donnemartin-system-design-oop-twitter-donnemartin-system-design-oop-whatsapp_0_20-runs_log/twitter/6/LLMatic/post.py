import time

class Post:
	def __init__(self, user, content, image=None):
		self.user = user
		self.content = content
		self.image = image
		self.timestamp = None
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create(self, db):
		self.timestamp = time.time()
		if self.user.email not in db:
			db[self.user.email] = self.user
		if self not in self.user.posts:
			self.user.posts.append(self)

	def delete(self, db):
		if self.user.email in db and self in db[self.user.email].posts:
			db[self.user.email].posts.remove(self)

	def like(self):
		self.likes += 1
		self.user.receive_notification(f'Your post has been liked.')

	def retweet(self):
		self.retweets += 1
		self.user.receive_notification(f'Your post has been retweeted.')

	def reply(self, reply):
		self.replies.append(reply)
		self.user.receive_notification(f'Your post has been replied to.')
