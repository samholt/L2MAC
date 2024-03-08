from models.tweet import Tweet
from views.tweet_view import TweetView


class TweetController:
	@staticmethod
	def set_privacy(tweet, privacy):
		tweet.set_privacy(privacy)
		TweetView.display_tweet(tweet)

	@staticmethod
	def get_replies(tweet):
		replies = tweet.get_replies()
		TweetView.display_replies(tweet)
		return replies
