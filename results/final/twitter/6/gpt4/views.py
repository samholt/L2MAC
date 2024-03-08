from models import User, Tweet, DirectMessage, Mention


class UserView:
	def display_user(self, user: User):
		print(f'User: {user.username}')


class TweetView:
	def display_tweet(self, tweet: Tweet):
		print(f'Tweet: {tweet.content}')


class DirectMessageView:
	def display_direct_message(self, message: DirectMessage):
		print(f'Message: {message.content}')


class MentionView:
	def display_mention(self, mention: Mention):
		print(f'Mention: {mention.id}')
