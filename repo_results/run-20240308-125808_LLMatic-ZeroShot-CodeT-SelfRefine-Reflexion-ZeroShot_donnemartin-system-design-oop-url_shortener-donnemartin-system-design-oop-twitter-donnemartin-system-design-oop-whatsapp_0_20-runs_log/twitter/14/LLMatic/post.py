import datetime
from user import User


class Post:
	def __init__(self, text, images, author):
		self.text = text
		self.images = images
		self.author = author
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like(self, liker):
		self.likes += 1
		self.author.notifications.append(f'{liker.username} liked your post.')

	def retweet(self, retweeter):
		self.retweets += 1
		self.author.notifications.append(f'{retweeter.username} retweeted your post.')

	def reply(self, replier, reply):
		self.replies.append(reply)
		self.author.notifications.append(f'{replier.username} replied to your post.')

	@staticmethod
	def create(db, text, images, author):
		if not isinstance(author, User):
			return 'Invalid author'
		id = len(db) + 1
		db[id] = Post(text, images, author)
		return id

	@staticmethod
	def delete(db, id):
		if id in db:
			del db[id]
			return 'Post deleted'
		return 'Post not found'

mock_db = {}

