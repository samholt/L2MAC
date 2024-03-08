from tweet import Tweet
from direct_message import DirectMessage


class User:
	def __init__(self, username):
		self.username = username
		self.tweets = []
		self.following = []
		self.followers = []
		self.direct_messages = []

	def post_tweet(self, content):
		tweet = Tweet(self, content)
		self.tweets.append(tweet)
		return tweet

	def reply_to_tweet(self, tweet, content):
		reply = tweet.reply(self, content)
		self.tweets.append(reply)
		return reply

	def send_direct_message(self, user, content):
		message = DirectMessage(self, user, content)
		self.direct_messages.append(message)
		return message

	def follow(self, user):
		self.following.append(user)
		user.followers.append(self)

	def mention(self, user, content):
		tweet = Tweet(self, content)
		tweet.mentions.append(user)
		self.tweets.append(tweet)
		return tweet

	def view_trending_tweets(self):
		# This method will be implemented in the Trending class
		pass
