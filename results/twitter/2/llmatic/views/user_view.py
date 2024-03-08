from models.user import User


class UserView:
	@staticmethod
	def display_user_tweets(user: User):
		for tweet in user.tweets:
			print(f'{user.username}: {tweet.content}')

	@staticmethod
	def display_following(user: User):
		for following in user.following:
			print(f'Following: {following.username}')

	@staticmethod
	def display_direct_messages(user: User):
		for dm in user.direct_messages:
			print(f'Direct Message from {dm.sender.username} to {dm.receiver.username}: {dm.content}')
