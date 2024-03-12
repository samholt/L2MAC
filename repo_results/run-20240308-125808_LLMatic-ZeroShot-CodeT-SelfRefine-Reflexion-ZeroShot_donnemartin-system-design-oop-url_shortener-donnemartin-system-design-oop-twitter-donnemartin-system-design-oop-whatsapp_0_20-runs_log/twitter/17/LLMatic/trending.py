class Trending:
	def __init__(self):
		self.trending_topics = {}

	def get_trending_topics(self):
		return sorted(self.trending_topics.items(), key=lambda x: x[1]['count'], reverse=True)

	def sort_trending_topics(self, location=None):
		if location:
			return sorted([topic for topic in self.trending_topics.items() if topic[1]['location'] == location], key=lambda x: x[1]['count'], reverse=True)
		else:
			return sorted(self.trending_topics.items(), key=lambda x: x[1]['count'], reverse=True)

	def add_topic(self, topic, location):
		if topic in self.trending_topics:
			self.trending_topics[topic]['count'] += 1
		else:
			self.trending_topics[topic] = {'count': 1, 'location': location}
