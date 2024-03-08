class Trending:
	def __init__(self, tweets):
		self.tweets = tweets
		self.trending_tweets = []

	def calculate_trending(self):
		# For simplicity, let's say a tweet is trending if it has more than 10 replies
		for tweet in self.tweets:
			if len(tweet.replies) > 10:
				self.trending_tweets.append(tweet)

	def display_trending(self):
		return self.trending_tweets
