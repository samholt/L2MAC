from models import User, Tweet, DirectMessage, Mention
from controllers import UserController, TweetController, DirectMessageController, MentionController


class UserView:
	def __init__(self, user_controller):
		self.user_controller = user_controller

	def display_user(self, user_id):
		user = self.user_controller.users[user_id - 1]
		print(f'User: {user.username}')
		print(f'Followers: {len(user.followers)}')


class TweetView:
	def __init__(self, tweet_controller):
		self.tweet_controller = tweet_controller

	def display_tweet(self, tweet_id):
		tweet = self.tweet_controller.tweets[tweet_id - 1]
		print(f'Tweet: {tweet.content}')
		print(f'Replies: {len(tweet.replies)}')
		print(f'Mentions: {len(tweet.mentions)}')

	def display_trending_tweets(self):
		trending_tweets = self.tweet_controller.get_trending_tweets()
		for tweet in trending_tweets:
			self.display_tweet(tweet.id)


class DirectMessageView:
	def __init__(self, direct_message_controller):
		self.direct_message_controller = direct_message_controller

	def display_direct_message(self, message_id):
		message = self.direct_message_controller.direct_messages[message_id - 1]
		print(f'Message: {message.content}')


class MentionView:
	def __init__(self, mention_controller):
		self.mention_controller = mention_controller

	def display_mention(self, mention_id):
		mention = self.mention_controller.mentions[mention_id - 1]
		print(f'Mention: {mention.id} in Tweet: {mention.tweet_id}')
