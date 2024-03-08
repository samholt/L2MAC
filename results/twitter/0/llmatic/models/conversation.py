class Conversation:
	def __init__(self):
		self.tweets = []

	def add_tweet(self, tweet):
		self.tweets.append(tweet)
		tweet.group_in_conversation(self)
