import collections


class Trending:
	def __init__(self):
		self.global_trends = collections.defaultdict(int)
		self.location_trends = collections.defaultdict(lambda: collections.defaultdict(int))

	def add_mention(self, topic, location=None):
		self.global_trends[topic] += 1
		if location:
			self.location_trends[location][topic] += 1

	def get_trending(self, location=None):
		if location and location in self.location_trends:
			return sorted(self.location_trends[location].items(), key=lambda x: x[1], reverse=True)
		return sorted(self.global_trends.items(), key=lambda x: x[1], reverse=True)
