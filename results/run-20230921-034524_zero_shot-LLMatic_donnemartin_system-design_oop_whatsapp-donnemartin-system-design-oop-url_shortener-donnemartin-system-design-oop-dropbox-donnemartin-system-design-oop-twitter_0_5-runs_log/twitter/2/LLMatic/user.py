class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.tweets = []
		self.following = []
		self.followers = []
		self.direct_messages = []
		self.mentions = []
		self.inbox = []

	def post_tweet(self, tweet):
		self.tweets.append(tweet)

	def reply_to_tweet(self, tweet, reply):
		tweet.replies.append(reply)

	def view_trending_tweets(self):
		pass

	def send_direct_message(self, user, message):
		self.direct_messages.append(message)
		user.inbox.append(message)
		user.direct_messages.append(message)

	def mention_user(self, user, tweet):
		if '@' + user.username in tweet.content:
			user.mentions.append(tweet)

	def follow_user(self, user):
		self.following.append(user)
		user.followers.append(self)

	def receive_message(self):
		return self.inbox
