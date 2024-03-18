class Trending:
	def __init__(self):
		self.trending_topics = {}

	def get_trending_topics(self):
		# Sort the trending topics based on volume and velocity of mentions
		trending = sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)
		return trending

	def sort_trending_topics(self, location=None):
		# If location is specified, sort the trending topics based on location
		if location:
			trending = {k: v for k, v in self.trending_topics.items() if k.startswith(location)}
			return sorted(trending.items(), key=lambda x: x[1], reverse=True)
		# If location is not specified, return the global trending topics
		return self.get_trending_topics()

