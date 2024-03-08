import datetime
from collections import Counter
from operator import itemgetter


class Trending:
	def __init__(self):
		self.hashtags = []
		self.mentions = []
		self.locations = []

	def add_hashtag(self, hashtag):
		self.hashtags.append((hashtag, datetime.datetime.now()))

	def add_mention(self, mention):
		self.mentions.append((mention, datetime.datetime.now()))

	def add_location(self, location):
		self.locations.append((location, datetime.datetime.now()))

	def get_trending_hashtags(self):
		counter = Counter(hashtag for hashtag, _ in self.hashtags)
		return sorted(counter.items(), key=itemgetter(1), reverse=True)

	def get_trending_mentions(self):
		counter = Counter(mention for mention, _ in self.mentions)
		return sorted(counter.items(), key=itemgetter(1), reverse=True)

	def get_trending_locations(self):
		counter = Counter(location for location, _ in self.locations)
		return sorted(counter.items(), key=itemgetter(1), reverse=True)
