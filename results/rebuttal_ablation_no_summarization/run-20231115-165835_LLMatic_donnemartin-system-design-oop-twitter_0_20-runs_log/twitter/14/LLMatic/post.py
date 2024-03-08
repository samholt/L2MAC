import datetime

class Post:
	def __init__(self, user, text, images=None):
		self.user = user
		self.text = text
		self.images = images if images else []
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.timestamp = datetime.datetime.now()

	def edit_post(self, text=None, images=None):
		if text is not None:
			self.text = text
		if images is not None:
			self.images = images

	def delete_post(self):
		self.text = None
		self.images = []
		self.user = None

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, user, text):
		reply = Post(user, text)
		self.replies.append(reply)

	@staticmethod
	def search_posts(posts, keyword):
		return [post for post in posts if keyword in post.text]

	@staticmethod
	def filter_posts(posts, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in posts if '#' + filter_value in post.text]
		elif filter_type == 'user mention':
			return [post for post in posts if '@' + filter_value in post.text]
		elif filter_type == 'trending topic':
			# For simplicity, assume that a trending topic is a keyword that appears in the text of a post
			return [post for post in posts if filter_value in post.text]
		else:
			return []

	@staticmethod
	def get_trending_topics(posts, min_mentions=3):
		keywords = {}
		for post in posts:
			for word in post.text.split():
				if word.startswith('#'):
					keywords[word] = keywords.get(word, 0) + 1
		return [keyword for keyword, count in keywords.items() if count >= min_mentions]
