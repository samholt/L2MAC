import pytest
from user import User
from tweet import Tweet


def test_set_privacy():
	user = User('user1', 'password1')
	tweet = Tweet(user, 'Hello, world!')
	tweet.set_privacy('private')
	assert tweet.privacy == 'private'


def test_group_tweets_by_conversation():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet = Tweet(user1, 'Hello, world!')
	reply = Tweet(user2, 'Hello, user1!')
	user2.reply_to_tweet(tweet, reply)
	conversation = tweet.group_tweets_by_conversation()
	assert conversation == [tweet, reply]
