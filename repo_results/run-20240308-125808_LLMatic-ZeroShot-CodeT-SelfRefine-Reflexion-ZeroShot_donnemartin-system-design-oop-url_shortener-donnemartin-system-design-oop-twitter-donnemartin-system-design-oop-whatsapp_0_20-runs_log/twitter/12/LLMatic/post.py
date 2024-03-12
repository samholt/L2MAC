import datetime
from collections import Counter


class Post:
	def __init__(self, id, user_id, text, image=None):
		self.id = id
		self.user_id = user_id
		self.text = text
		self.image = image
		self.timestamp = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, post):
		self.replies.append(post)

	def delete(self):
		self.text = 'This post has been deleted.'
		self.image = None

	@staticmethod
	def search(posts, keyword):
		return [post for post in posts if keyword in post.text]

	@staticmethod
	def filter_by_hashtag(posts, hashtag):
		return [post for post in posts if '#' + hashtag in post.text]

	@staticmethod
	def filter_by_mention(posts, user_id):
		return [post for post in posts if '@' + str(user_id) in post.text]

	@staticmethod
	def filter_by_trending(posts, trending_topics):
		return [post for post in posts if any(topic in post.text for topic in trending_topics)]

	@staticmethod
	def get_trending_hashtags(posts):
		hashtags = []
		for post in posts:
			words = post.text.split()
			hashtags.extend([word for word in words if word.startswith('#')])
		return [hashtag for hashtag, count in Counter(hashtags).most_common(5)]
