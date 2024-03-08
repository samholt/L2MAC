import pytest
from user import User
from tweet import Tweet
from trending import Trending


def test_trending_creation():
	user = User('testuser', 'password')
	tweet1 = Tweet(user, 'Hello, world!', 'public')
	tweet2 = Tweet(user, 'Hello again, world!', 'public')
	trending = Trending([tweet1, tweet2])
	assert tweet1 in trending.tweets
	assert tweet2 in trending.tweets


def test_calculate_trending():
	user = User('testuser', 'password')
	tweet1 = Tweet(user, 'Hello, world!', 'public')
	tweet2 = Tweet(user, 'Hello again, world!', 'public')
	trending = Trending([tweet1, tweet2])
	trending.calculate_trending()
	# Assuming the calculate_trending method updates a 'trending_tweets' attribute
	assert trending.trending_tweets is not None


def test_display_trending():
	user = User('testuser', 'password')
	tweet1 = Tweet(user, 'Hello, world!', 'public')
	tweet2 = Tweet(user, 'Hello again, world!', 'public')
	trending = Trending([tweet1, tweet2])
	trending.calculate_trending()
	trending_tweets = trending.display_trending()
	# Assuming the display_trending method returns the 'trending_tweets' attribute
	assert trending_tweets == trending.trending_tweets
