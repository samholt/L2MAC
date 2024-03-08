import pytest
from user import User
from tweet import Tweet
from conversation import Conversation


def test_conversation():
	conversation = Conversation()
	assert conversation.tweets == []

	user = User('testuser')
	tweet = Tweet(user, 'Hello, world!')
	conversation.add_tweet(tweet)
	assert tweet in conversation.tweets
