from models import User, Tweet, DirectMessage, Mention


class Controller:
	def __init__(self):
		self.users = []
		self.tweets = []
		self.direct_messages = []
		self.mentions = []

	def create_user(self, id, username):
		user = User(id=id, username=username, followers=[], following=[], tweets=[], direct_messages=[])
		self.users.append(user)
		return user

	def create_tweet(self, user, content, privacy):
		tweet = Tweet(id=len(self.tweets)+1, user=user, content=content, privacy=privacy, replies=[], mentions=[])
		user.post_tweet(tweet)
		self.tweets.append(tweet)
		return tweet

	def create_direct_message(self, sender, receiver, message):
		dm = DirectMessage(id=len(self.direct_messages)+1, sender=sender, receiver=receiver, message=message)
		sender.send_direct_message(receiver, message)
		self.direct_messages.append(dm)
		return dm

	def create_mention(self, user, tweet):
		mention = Mention(id=len(self.mentions)+1, user=user, tweet=tweet)
		tweet.add_mention(user)
		self.mentions.append(mention)
		return mention
