class Trending:
	def __init__(self):
		self.trending_topics = {}
		self.user_recommendations = {}

	def add_topic(self, topic):
		if topic not in self.trending_topics:
			self.trending_topics[topic] = 0
		self.trending_topics[topic] += 1

	def get_trending_topics(self):
		return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)

	def add_user_recommendation(self, user):
		if user not in self.user_recommendations:
			self.user_recommendations[user] = 0
		self.user_recommendations[user] += 1

	def get_user_recommendations(self):
		return sorted(self.user_recommendations.items(), key=lambda x: x[1], reverse=True)
