import pytest
from user import User
from tweet import Tweet


def test_tweet_creation():
	user = User('testuser', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	assert tweet.user == user
	assert tweet.content == 'Hello, world!'
	assert tweet.privacy == 'public'


def test_set_privacy():
	user = User('testuser', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	tweet.set_privacy('private')
	assert tweet.privacy == 'private'


def test_group_by_conversation():
	user = User('testuser', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	conversation_id = 1
	tweet.group_by_conversation(conversation_id)
	assert tweet.conversation_id == conversation_id
