import pytest
from user import User
from tweet import Tweet


def test_post_tweet():
	user = User('user1', 'password1')
	tweet = Tweet(user, 'Hello, world!')
	user.post_tweet(tweet)
	assert tweet in user.tweets


def test_reply_to_tweet():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet = Tweet(user1, 'Hello, world!')
	reply = Tweet(user2, 'Hello, user1!')
	user2.reply_to_tweet(tweet, reply)
	assert reply in tweet.replies


def test_follow_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user1.follow_user(user2)
	assert user2 in user1.following
