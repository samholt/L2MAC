class Conversation:
	def __init__(self, tweets):
		self.tweets = tweets

	def group_tweets(self):
		# Group tweets by conversation
		conversations = {}
		for tweet in self.tweets:
			if tweet.conversation_id not in conversations:
				conversations[tweet.conversation_id] = []
			conversations[tweet.conversation_id].append(tweet)
		return conversations
