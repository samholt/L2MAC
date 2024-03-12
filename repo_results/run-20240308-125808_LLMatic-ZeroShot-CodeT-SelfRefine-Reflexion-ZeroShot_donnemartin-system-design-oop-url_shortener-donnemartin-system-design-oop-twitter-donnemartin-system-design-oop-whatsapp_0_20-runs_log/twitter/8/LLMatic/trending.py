class Trending:
	def __init__(self):
		self.topics = {}

	def add_topic(self, topic):
		if topic not in self.topics:
			self.topics[topic] = 1
		else:
			self.topics[topic] += 1

	def get_trending_topics(self):
		trending_topics = sorted(self.topics.items(), key=lambda x: x[1], reverse=True)
		return trending_topics

	def sort_trending_topics(self, location=None):
		if location is None:
			return self.get_trending_topics()
		else:
			# Assuming location based trending topics are stored in a dictionary with location as key
			# and trending topics as values
			return self.topics.get(location, [])
