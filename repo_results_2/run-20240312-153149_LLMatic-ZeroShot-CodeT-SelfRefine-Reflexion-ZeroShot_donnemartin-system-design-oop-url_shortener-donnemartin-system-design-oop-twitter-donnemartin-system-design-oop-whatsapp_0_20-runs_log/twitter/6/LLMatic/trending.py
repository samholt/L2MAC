class Trending:
	def __init__(self):
		self.trending_topics_dict = {}

	def add_topic(self, topic):
		if topic in self.trending_topics_dict:
			self.trending_topics_dict[topic] += 1
		else:
			self.trending_topics_dict[topic] = 1

	def get_trending_topics(self):
		# Sort the topics based on the volume and return the top 10
		return sorted(self.trending_topics_dict.items(), key=lambda x: x[1], reverse=True)[:10]
