from direct_message import DirectMessage

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.tweets = []
		self.following = []
		self.followers = []
		self.direct_messages = []
		self.mentions = []

	def post_tweet(self, tweet):
		self.tweets.append(tweet)

	def reply_to_tweet(self, tweet, reply):
		tweet.replies.append(reply)

	def view_trending_tweets(self):
		# This method will be implemented in the Trending class
		pass

	def send_direct_message(self, user, message):
		dm = DirectMessage(self, user, message)
		self.direct_messages.append(dm)
		user.direct_messages.append(dm)

	def mention_user(self, tweet, user):
		tweet.mentions.append(user)

	def follow_user(self, user):
		self.following.append(user)
		user.followers.append(self)

	def receive_message(self):
		return self.direct_messages[-1]
