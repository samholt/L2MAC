from models.direct_message import DirectMessage

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.following = []
		self.tweets = []
		self.direct_messages = []

	def post_tweet(self, tweet):
		self.tweets.append(tweet)

	def reply_to_tweet(self, tweet, reply):
		tweet.replies.append(reply)

	def view_trending_tweets(self):
		# This method will be implemented in the Trending class
		pass

	def send_direct_message(self, recipient, message):
		self.direct_messages.append(DirectMessage(self, recipient, message))

	def mention_user(self, user):
		# This method will be implemented in the Tweet class
		pass

	def follow_user(self, user):
		self.following.append(user)
