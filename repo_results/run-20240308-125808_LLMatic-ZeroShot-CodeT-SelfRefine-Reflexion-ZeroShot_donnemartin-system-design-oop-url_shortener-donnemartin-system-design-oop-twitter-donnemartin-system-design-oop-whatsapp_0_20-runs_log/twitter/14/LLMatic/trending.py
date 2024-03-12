import collections


class Trending:
	def __init__(self):
		self.topics = collections.defaultdict(int)
		self.location_based_topics = collections.defaultdict(lambda: collections.defaultdict(int))

	def add_topic(self, topic, location=None):
		self.topics[topic] += 1
		if location:
			self.location_based_topics[location][topic] += 1

	def get_trending_topics(self):
		return sorted(self.topics.items(), key=lambda x: x[1], reverse=True)

	def sort_trending_topics(self, location=None):
		if location is None:
			return self.get_trending_topics()
		else:
			return sorted(self.location_based_topics[location].items(), key=lambda x: x[1], reverse=True)
