import pytest
from models.user import User
from models.tweet import Tweet
from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController


def test_tweet_creation():
	user_controller = UserController()
	tweet_controller = TweetController()
	user = user_controller.create_user('testuser', 'testpassword')
	tweet = tweet_controller.create_tweet('Hello, world!', user, 'public')
	assert tweet.content == 'Hello, world!'
	assert tweet.poster == user
	assert tweet.privacy == 'public'


def test_tweet_reply():
	user_controller = UserController()
	tweet_controller = TweetController()
	user = user_controller.create_user('testuser', 'testpassword')
	tweet = tweet_controller.create_tweet('Hello, world!', user, 'public')
	reply = tweet_controller.create_reply('Hello, reply!', user, 'public', tweet)
	assert reply.content == 'Hello, reply!'
	assert reply.poster == user
	assert reply.privacy == 'public'
	assert reply.original_tweet == tweet
