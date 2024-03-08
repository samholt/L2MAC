from controllers.tweet_controller import TweetController


class TweetView:
	def __init__(self):
		self.controller = TweetController()

	def create_tweet_form(self, poster):
		content = input('Enter tweet content: ')
		privacy = input('Enter privacy setting (public/private): ')
		self.controller.create_tweet(content, poster, privacy)

	def list_tweets(self):
		for tweet in self.controller.tweets:
			print(f'Content: {tweet.content}')
			print(f'Poster: {tweet.poster.username}')
			print(f'Privacy: {tweet.privacy}')

	def detail_tweet(self, id):
		tweet = self.controller.get_tweet(id)
		if tweet:
			print(f'Content: {tweet.content}')
			print(f'Poster: {tweet.poster.username}')
			print(f'Privacy: {tweet.privacy}')
		else:
			print('Tweet not found.')
