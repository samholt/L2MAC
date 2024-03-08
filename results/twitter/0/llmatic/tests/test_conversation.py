import pytest
from models.user import User
from models.tweet import Tweet
from models.conversation import Conversation


def test_add_tweet():
	user = User('test_user', 'password')
	tweet = Tweet('Hello, world!', user)
	conversation = Conversation()
	conversation.add_tweet(tweet)
	assert tweet in conversation.tweets
	assert tweet.conversation == conversation

