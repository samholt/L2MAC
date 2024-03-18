class Trending:
	def __init__(self):
		self.trending_hashtags = {}
		self.trending_topics = {}
		self.recommended_users = {}

	def identify_trending_hashtags(self, posts):
		for post in posts:
			for hashtag in post.hashtags:
				if hashtag not in self.trending_hashtags:
					self.trending_hashtags[hashtag] = 0
				self.trending_hashtags[hashtag] += 1

	def display_trending_hashtags(self):
		return sorted(self.trending_hashtags.items(), key=lambda x: x[1], reverse=True)

	def identify_trending_topics(self, posts):
		for post in posts:
			for topic in post.topics:
				if topic not in self.trending_topics:
					self.trending_topics[topic] = 0
				self.trending_topics[topic] += 1

	def display_trending_topics(self):
		return sorted(self.trending_topics.items(), key=lambda x: x[1], reverse=True)

	def recommend_users(self, user, users):
		for u in users:
			if u != user and u not in user.following:
				self.recommended_users[u] = len(u.followers)
		return sorted(self.recommended_users.items(), key=lambda x: x[1], reverse=True)

	@staticmethod
	def filter(posts, keyword):
		return [post for post in posts if keyword in post.hashtags or keyword in post.topics]
