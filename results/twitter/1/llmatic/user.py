from direct_message import DirectMessage

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.tweets = []
		self.following = []
		self.direct_messages = []

	def post_tweet(self, tweet):
		self.tweets.append(tweet)

	def reply_to_tweet(self, tweet, reply):
		tweet.replies.append(reply)

	def view_trending_tweets(self):
		# This method will be implemented in the Trending class
		pass

	def send_direct_message(self, user, direct_message):
		user.direct_messages.append(direct_message)

	def mention_user(self, user, tweet):
		tweet.mentions.append(user)
		user.mentions.append(tweet)

	def follow_user(self, user):
		self.following.append(user)
