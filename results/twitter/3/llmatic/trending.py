class Trending:
	trending_tweets = []

	@staticmethod
	def add_trending_tweet(tweet):
		Trending.trending_tweets.append(tweet)

	@staticmethod
	def get_trending_tweets():
		return Trending.trending_tweets
