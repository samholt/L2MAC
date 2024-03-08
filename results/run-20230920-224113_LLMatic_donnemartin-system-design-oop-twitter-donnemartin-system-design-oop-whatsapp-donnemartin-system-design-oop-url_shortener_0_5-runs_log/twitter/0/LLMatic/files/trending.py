class Trending:
	def __init__(self, tweets):
		self.tweets = tweets
		self.trending_tweets = []

	def calculate_trending(self):
		# For simplicity, let's say the trending tweets are the ones with the most replies
		self.trending_tweets = sorted(self.tweets, key=lambda tweet: len(tweet.replies), reverse=True)[:10]

	def display_trending(self):
		return self.trending_tweets
