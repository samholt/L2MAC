class Conversation:
	def __init__(self):
		self.tweets = []

	def add_tweet(self, tweet):
		self.tweets.append(tweet)

	def get_tweets(self):
		return self.tweets
