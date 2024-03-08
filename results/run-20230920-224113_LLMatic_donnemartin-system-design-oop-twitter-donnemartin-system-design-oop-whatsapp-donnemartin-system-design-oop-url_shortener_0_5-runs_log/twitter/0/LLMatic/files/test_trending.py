import pytest
from user import User
from tweet import Tweet
from trending import Trending


def test_calculate_trending():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet1 = Tweet(user1, 'Hello, world!', 'public')
	tweet2 = Tweet(user2, 'Hello, user1!', 'public')
	trending = Trending([tweet1, tweet2])
	trending.calculate_trending()
	assert trending.trending_tweets != []


def test_display_trending():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet1 = Tweet(user1, 'Hello, world!', 'public')
	tweet2 = Tweet(user2, 'Hello, user1!', 'public')
	trending = Trending([tweet1, tweet2])
	trending.calculate_trending()
	trending_tweets = trending.display_trending()
	assert trending_tweets == trending.trending_tweets
