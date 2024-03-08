import pytest
from models.user import User
from models.tweet import Tweet
from models.trending import Trending


def test_calculate_trending():
	user = User('test_user', 'password')
	tweet1 = Tweet('Hello, world!', user)
	tweet1.likes = 10
	tweet1.retweets = 5
	tweet2 = Tweet('Goodbye, world!', user)
	tweet2.likes = 5
	tweet2.retweets = 10
	trending = Trending()
	trending.tweets = [tweet1, tweet2]
	trending.calculate_trending()
	assert trending.tweets == [tweet1, tweet2]

