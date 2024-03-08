from models.user import User
from views.user_view import UserView


class UserController:
	@staticmethod
	def create_user(username, password):
		user = User(username, password)
		return user

	@staticmethod
	def follow_user(user, user_to_follow):
		user.follow(user_to_follow)
		UserView.display_following(user)

	@staticmethod
	def post_tweet(user, tweet_content, privacy):
		tweet = user.post_tweet(tweet_content, privacy)
		UserView.display_user_tweets(user)
		return tweet

	@staticmethod
	def reply_to_tweet(user, tweet, reply_content):
		if tweet is not None:
			reply = user.reply_to_tweet(tweet, reply_content)
			UserView.display_user_tweets(user)
			return reply

	@staticmethod
	def send_direct_message(user, receiver, message_content):
		dm = user.send_direct_message(receiver, message_content)
		UserView.display_direct_messages(user)
		return dm
