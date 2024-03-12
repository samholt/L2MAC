class Trending:
	def __init__(self):
		self.topics = {}

	def add_topic(self, topic, location):
		if topic not in self.topics:
			self.topics[topic] = {'count': 1, 'locations': [location]}
		else:
			self.topics[topic]['count'] += 1
			self.topics[topic]['locations'].append(location)

	def get_trending_topics(self, location=None):
		if location:
			return sorted([topic for topic in self.topics.items() if location in topic[1]['locations']], key=lambda x: x[1]['count'], reverse=True)
		else:
			return sorted(self.topics.items(), key=lambda x: x[1]['count'], reverse=True)
