from models.trending_tweet import TrendingTweet


class TrendingTweetController:
	def __init__(self):
		self.trending_tweets = []

	def add_trending_tweet(self, tweet, popularity: int):
		trending_tweet = TrendingTweet(tweet, popularity)
		self.trending_tweets.append(trending_tweet)
		self.trending_tweets.sort(key=lambda x: x.popularity, reverse=True)
		return trending_tweet

	def get_trending_tweets(self):
		return self.trending_tweets
