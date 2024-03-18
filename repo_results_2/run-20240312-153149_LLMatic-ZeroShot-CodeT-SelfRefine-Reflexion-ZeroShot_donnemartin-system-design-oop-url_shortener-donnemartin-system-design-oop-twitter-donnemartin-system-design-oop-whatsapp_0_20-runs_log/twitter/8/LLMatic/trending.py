import operator
from collections import Counter

class Trending:
	def __init__(self):
		self.hashtags = {}
		self.locations = {}

	def add_hashtag(self, hashtag, location):
		if hashtag in self.hashtags:
			self.hashtags[hashtag] += 1
		else:
			self.hashtags[hashtag] = 1

		if location in self.locations:
			if hashtag in self.locations[location]:
				self.locations[location][hashtag] += 1
			else:
				self.locations[location][hashtag] = 1
		else:
			self.locations[location] = {hashtag: 1}

	def get_trending_hashtags(self, location=None):
		if location and location in self.locations:
			return sorted(self.locations[location].items(), key=operator.itemgetter(1), reverse=True)
		return sorted(self.hashtags.items(), key=operator.itemgetter(1), reverse=True)

