import pytest
from user import User
from tweet import Tweet
from direct_message import DirectMessage


def test_post_tweet():
	user = User('username', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	user.post_tweet(tweet)
	assert tweet in user.tweets


def test_reply_to_tweet():
	user = User('username', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	reply = Tweet(user, 'Hello, user!', 'public')
	user.reply_to_tweet(tweet, reply)
	assert reply in tweet.replies


def test_send_direct_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	user1.send_direct_message(user2, message)
	assert any(dm.content == message for dm in user2.direct_messages)


def test_mention_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet = Tweet(user1, 'Hello, @user2', 'public')
	user1.mention_user(tweet, user2)
	assert user2 in tweet.mentions


def test_follow_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user1.follow_user(user2)
	assert user2 in user1.following
	assert user1 in user2.followers


def test_receive_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	user1.send_direct_message(user2, message)
	received_message = user2.receive_message()
	assert received_message.content == message
