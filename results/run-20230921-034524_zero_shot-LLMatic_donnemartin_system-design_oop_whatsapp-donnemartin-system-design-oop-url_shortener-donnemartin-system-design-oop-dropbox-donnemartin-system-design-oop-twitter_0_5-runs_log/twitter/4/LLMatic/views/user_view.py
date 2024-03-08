from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController


class UserView:
	def __init__(self):
		self.user_controller = UserController()
		self.tweet_controller = TweetController()

	def create_user_form(self):
		username = input('Enter username: ')
		password = input('Enter password: ')
		self.user_controller.create_user(username, password)

	def mention_user_form(self):
		tweet_id = int(input('Enter tweet id: '))
		username = input('Enter username of the user to mention: ')
		user = self.user_controller.get_user(username)
		if user:
			self.tweet_controller.mention_user(tweet_id, user)
		else:
			print('User not found.')

	def list_users(self):
		for user in self.user_controller.users:
			print(f'Username: {user.username}')

	def detail_user(self, username):
		user = self.user_controller.get_user(username)
		if user:
			print(f'Username: {user.username}')
			print(f'Followers: {len(user.followers)}')
			print(f'Following: {len(user.following)}')
		else:
			print('User not found.')

	def follow_user_form(self):
		follower_username = input('Enter your username: ')
		followee_username = input('Enter the username of the user you want to follow: ')
		if self.user_controller.follow_user(follower_username, followee_username):
			print('You are now following ' + followee_username)
		else:
			print('Could not follow user.')
