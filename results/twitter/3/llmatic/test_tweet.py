import pytest
from user import User
from tweet import Tweet


def test_tweet():
	user = User('testuser')
	tweet = Tweet(user, 'Hello, world!')

	assert tweet.user == user
	assert tweet.content == 'Hello, world!'
	assert tweet.replies == []
	assert tweet.mentions == []
	assert tweet.privacy == 'public'

	reply = tweet.reply(user, 'Hello, testuser!')
	assert isinstance(reply, Tweet)
	assert reply in tweet.replies

	tweet.set_privacy('private')
	assert tweet.get_privacy() == 'private'
