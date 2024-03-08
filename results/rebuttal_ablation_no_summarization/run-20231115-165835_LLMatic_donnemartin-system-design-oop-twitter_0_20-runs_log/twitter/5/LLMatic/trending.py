import re
from collections import Counter


class Trending:
	def __init__(self, posts):
		self.posts = posts

	def get_trending_topics(self):
		hashtags = []
		for post in self.posts:
			hashtags.extend(re.findall(r'#\w+', post.text))
		return Counter(hashtags).most_common(5)
