import pytest
from models.user import User
from models.tweet import Tweet
from models.trending_tweet import TrendingTweet
from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController
from controllers.trending_tweet_controller import TrendingTweetController


def test_trending_tweet_creation():
	user_controller = UserController()
	tweet_controller = TweetController()
	trending_tweet_controller = TrendingTweetController()
	user = user_controller.create_user('testuser', 'testpassword')
	tweet = tweet_controller.create_tweet('Hello, world!', user, 'public')
	trending_tweet = trending_tweet_controller.add_trending_tweet(tweet, 100)
	assert trending_tweet.tweet == tweet
	assert trending_tweet.popularity == 100
