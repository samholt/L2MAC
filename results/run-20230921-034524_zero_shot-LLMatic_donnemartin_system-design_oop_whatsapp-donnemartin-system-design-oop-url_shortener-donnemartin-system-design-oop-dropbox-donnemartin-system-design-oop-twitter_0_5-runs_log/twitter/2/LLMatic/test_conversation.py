import pytest
from user import User
from tweet import Tweet
from conversation import Conversation


def test_conversation_creation():
	user = User('testuser', 'password')
	tweet1 = Tweet(user, 'Hello, world!', 'public')
	tweet2 = Tweet(user, 'Hello again, world!', 'public')
	conversation = Conversation([tweet1, tweet2])
	assert tweet1 in conversation.tweets
	assert tweet2 in conversation.tweets


def test_group_tweets():
	user = User('testuser', 'password')
	tweet1 = Tweet(user, 'Hello, world!', 'public')
	tweet2 = Tweet(user, 'Hello again, world!', 'public')
	conversation = Conversation([tweet1, tweet2])
	grouped_tweets = conversation.group_tweets()
	assert tweet1 in grouped_tweets[tweet1.conversation_id]
	assert tweet2 in grouped_tweets[tweet2.conversation_id]
