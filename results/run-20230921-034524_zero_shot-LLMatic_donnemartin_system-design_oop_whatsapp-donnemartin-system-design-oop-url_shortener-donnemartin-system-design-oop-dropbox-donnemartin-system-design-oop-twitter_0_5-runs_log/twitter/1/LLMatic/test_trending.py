import pytest
from user import User
from tweet import Tweet
from trending import Trending


def test_trending():
	assert Trending.trending_tweets == []

	user = User('testuser')
	tweet = Tweet(user, 'Hello, world!')
	Trending.add_trending_tweet(tweet)
	assert tweet in Trending.get_trending_tweets()
