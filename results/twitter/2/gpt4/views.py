from models import User, Tweet, DirectMessage, Mention
from controllers import UserController, TweetController, DirectMessageController, MentionController


class UserView:
	def __init__(self):
		self.controller = UserController()

	def follow_user(self, user: User, other_user: User):
		self.controller.follow(user, other_user)


class TweetView:
	def __init__(self):
		self.controller = TweetController()

	def post_tweet(self, user: User, content: str, privacy: str):
		return self.controller.post_tweet(user, content, privacy)

	def reply_to_tweet(self, user: User, tweet: Tweet, content: str):
		return self.controller.reply_to_tweet(user, tweet, content)

	def get_trending_tweets(self):
		return self.controller.get_trending_tweets()


class DirectMessageView:
	def __init__(self):
		self.controller = DirectMessageController()

	def send_message(self, sender: User, receiver: User, content: str):
		return self.controller.send_message(sender, receiver, content)


class MentionView:
	def __init__(self):
		self.controller = MentionController()

	def mention_user(self, user: User, tweet: Tweet):
		return self.controller.mention_user(user, tweet)
