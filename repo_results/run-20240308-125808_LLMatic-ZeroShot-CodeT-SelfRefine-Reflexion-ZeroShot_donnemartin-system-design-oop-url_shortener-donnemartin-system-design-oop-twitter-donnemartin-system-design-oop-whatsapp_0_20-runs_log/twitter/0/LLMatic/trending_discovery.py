class TrendingTopic:
	def __init__(self, topic, count):
		self.topic = topic
		self.count = count


class TrendingDiscovery:
	def __init__(self):
		self.trending_topics = []

	def identify_trending_topics(self, posts):
		topics = {}
		for post in posts:
			for hashtag in post.hashtags:
				if hashtag not in topics:
					topics[hashtag] = 0
				topics[hashtag] += 1
		for topic, count in topics.items():
			self.trending_topics.append(TrendingTopic(topic, count))

	def display_trending_topics(self):
		return sorted(self.trending_topics, key=lambda x: x.count, reverse=True)

	def sort_trending_topics(self, location):
		# Mock implementation as location data is not available
		return self.trending_topics
