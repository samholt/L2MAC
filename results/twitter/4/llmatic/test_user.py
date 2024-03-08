import pytest
from user import User
from tweet import Tweet


def test_user_creation():
	user = User('testuser', 'password')
	assert user.username == 'testuser'
	assert user.password == 'password'


def test_post_tweet():
	user = User('testuser', 'password')
	tweet = Tweet(user, 'Hello, world!', 'public')
	user.post_tweet(tweet)
	assert tweet in user.tweets


def test_reply_to_tweet():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet1 = Tweet(user1, 'Hello, world!', 'public')
	reply1 = Tweet(user2, 'Hello, user1!', 'public')
	user2.reply_to_tweet(tweet1, reply1)
	assert reply1 in tweet1.replies


def test_send_direct_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	user1.send_direct_message(user2, message)
	assert message in user2.direct_messages


def test_mention_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	tweet = Tweet(user1, 'Hello, @user2!', 'public')
	user1.mention_user(user2, tweet)
	assert tweet in user2.mentions


def test_follow_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user1.follow_user(user2)
	assert user2 in user1.following
	assert user1 in user2.followers
