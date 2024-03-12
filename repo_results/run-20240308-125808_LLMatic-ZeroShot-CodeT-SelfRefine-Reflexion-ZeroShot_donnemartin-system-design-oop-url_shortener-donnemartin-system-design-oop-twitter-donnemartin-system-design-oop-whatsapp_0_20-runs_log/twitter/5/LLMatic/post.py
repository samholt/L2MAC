import datetime
from notification import Notification
from collections import Counter


class Post:
	def __init__(self, text, images, user):
		self.text = text
		self.images = images
		self.user = user
		self.likes = []
		self.retweets = []
		self.replies = []
		self.timestamp = datetime.datetime.now()

	def like(self, user):
		self.likes.append(user)
		user.notifications.append(Notification(user, 'like'))

	def retweet(self, user):
		self.retweets.append(user)
		user.notifications.append(Notification(user, 'retweet'))

	def reply(self, text, images, user):
		reply = Post(text, images, user)
		self.replies.append(reply)
		user.notifications.append(Notification(user, 'reply'))
		return reply

	def search(self, keyword):
		if keyword in self.text:
			return self
		return None

	def filter(self, hashtag):
		if hashtag in self.text:
			return self
		return None

	@staticmethod
	def trending_topics(posts):
		hashtags = []
		for post in posts:
			hashtags.extend([word for word in post.text.split() if word.startswith('#')])
		return [hashtag for hashtag, count in Counter(hashtags).most_common(10)]
