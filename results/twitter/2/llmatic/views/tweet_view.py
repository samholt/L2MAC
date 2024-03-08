from models.tweet import Tweet


class TweetView:
	@staticmethod
	def display_tweet(tweet: Tweet):
		print(f'{tweet.user.username}: {tweet.content}')

	@staticmethod
	def display_replies(tweet: Tweet):
		for reply in tweet.replies:
			print(f'Reply from {reply.user.username}: {reply.content}')
