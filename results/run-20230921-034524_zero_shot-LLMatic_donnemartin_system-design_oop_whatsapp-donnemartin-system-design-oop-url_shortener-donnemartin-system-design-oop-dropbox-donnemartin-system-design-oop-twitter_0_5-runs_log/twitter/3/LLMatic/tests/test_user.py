import pytest
from models.user import User
from models.tweet import Tweet
from models.direct_message import DirectMessage


def test_post_tweet():
	user = User('test_user', 'password')
	tweet = Tweet('Hello, world!', user)
	user.post_tweet(tweet)
	assert tweet in user.tweets


def test_reply_to_tweet():
	user1 = User('user1', 'password')
	user2 = User('user2', 'password')
	tweet = Tweet('Hello, world!', user1)
	reply = Tweet('Hello, user1!', user2)
	user2.reply_to_tweet(tweet, reply)
	assert reply in tweet.replies


def test_send_direct_message():
	user1 = User('user1', 'password')
	user2 = User('user2', 'password')
	message = 'Hello, user2!'
	user1.send_direct_message(user2, message)
	assert any(dm.content == message for dm in user1.direct_messages)


def test_follow_user():
	user1 = User('user1', 'password')
	user2 = User('user2', 'password')
	user1.follow_user(user2)
	assert user2 in user1.following

