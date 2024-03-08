from controller import Controller
from view import View


class Application:
	def __init__(self):
		self.controller = Controller()
		self.view = View(self.controller)

	def run(self):
		# Create users
		alice = self.controller.create_user(1, 'Alice')
		bob = self.controller.create_user(2, 'Bob')

		# Alice posts a tweet
		tweet = self.controller.create_tweet(alice, 'Hello, world!', 'public')

		# Bob replies to the tweet
		reply = self.controller.create_tweet(bob, 'Hello, Alice!', 'public')
		alice.reply_to_tweet(tweet, reply)

		# Alice sends a direct message to Bob
		dm = self.controller.create_direct_message(alice, bob, 'Hi Bob!')

		# Alice mentions Bob in a tweet
		mention = self.controller.create_mention(bob, tweet)

		# Display the users, tweets, direct messages, and mentions
		self.view.display_user(alice)
		self.view.display_user(bob)
		self.view.display_tweet(tweet)
		self.view.display_tweet(reply)
		self.view.display_direct_message(dm)
		self.view.display_mention(mention)


if __name__ == '__main__':
	app = Application()
	app.run()
