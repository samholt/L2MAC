import pytest
from user import User
from tweet import Tweet
from conversation import Conversation


def test_set_privacy():
	user = User('user1', 'password1')
	tweet = Tweet(user, 'Hello, world!', 'public')
	tweet.set_privacy('private')
	assert tweet.privacy == 'private'


def test_group_by_conversation():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet1 = Tweet(user1, 'Hello, world!', 'public')
	tweet2 = Tweet(user2, 'Hello, user1!', 'public')
	conversation = Conversation([tweet1, tweet2])
	tweet1.group_by_conversation(conversation)
	tweet2.group_by_conversation(conversation)
	assert tweet1 in conversation.tweets
	assert tweet2 in conversation.tweets
