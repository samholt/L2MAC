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
		return [topic[0] for topic in trending_topics[:10]]
