import pytest
from models import User, Post, Notification, users_db, notifications_db
from notifications import get_notifications


def setup_module(module):
	users_db.clear()
	notifications_db.clear()
	user1 = User(1, 'user1', 'user1@example.com', 'password')
	user2 = User(2, 'user2', 'user2@example.com', 'password')
	users_db[1] = user1
	users_db[2] = user2
	post = Post(1, 2, 'Hello, world!')
	user1.mention_user(user2)
	user1.reply_to_post(post, 'Nice post!')
	user1.retweet_post(post)
	user1.like_post(post)


def test_get_notifications():
	notifications = get_notifications(2)
	assert len(notifications) == 4
	assert isinstance(notifications[0], Notification)
	assert notifications[0].message == 'user1 liked your post.'
	assert notifications[1].message == 'user1 retweeted your post.'
	assert notifications[2].message == 'user1 replied to your post.'
	assert notifications[3].message == 'user1 mentioned you in a post.'
