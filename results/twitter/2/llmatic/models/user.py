from .tweet import Tweet
from .direct_message import DirectMessage

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.following = []
		self.tweets = []
		self.direct_messages = []

	def follow(self, user):
		self.following.append(user)

	def post_tweet(self, tweet_content, privacy):
		tweet = Tweet(self, tweet_content, privacy)
		self.tweets.append(tweet)
		return tweet

	def reply_to_tweet(self, tweet, reply_content):
		reply = Tweet(self, reply_content, 'public')
		if tweet.replies is None:
			tweet.replies = []
		tweet.replies.append(reply)
		return reply

	def send_direct_message(self, user, message):
		self.direct_messages.append(DirectMessage(self, user, message))
