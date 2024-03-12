import pytest
from social_interaction import Message, Timeline, Notification
from user_management import User
from posting_content_management import Post

def test_message_creation():
	user1 = User('email1', 'username1', 'password1')
	user2 = User('email2', 'username2', 'password2')
	message = Message(user1, user2, 'Hello!')
	assert message.sender == user1
	assert message.receiver == user2
	assert message.content == 'Hello!'

def test_timeline_update():
	user1 = User('email1', 'username1', 'password1')
	user2 = User('email2', 'username2', 'password2')
	user1.follow(user2)
	timeline = Timeline(user1)
	post = Post(user2, 'Hello!', [])
	timeline.update([post])
	assert len(timeline.posts) == 1

def test_notification_creation():
	user1 = User('email1', 'username1', 'password1')
	user2 = User('email2', 'username2', 'password2')
	post = Post(user1, 'Hello!', [])
	user2.like(post)
	assert len(user1.notifications) == 1
	assert user1.notifications[0].notification_type == 'like'

