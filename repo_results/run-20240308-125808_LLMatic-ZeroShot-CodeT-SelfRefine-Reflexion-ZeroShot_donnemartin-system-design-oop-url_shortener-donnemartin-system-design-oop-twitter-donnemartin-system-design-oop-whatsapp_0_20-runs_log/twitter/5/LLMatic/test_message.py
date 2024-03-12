import pytest
from message import Message
from user import User
from notification import Notification

def test_send_message():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello')
	assert message.send_message() == 'Message sent.'
	assert message in user2.inbox
	assert isinstance(user2.notifications[0], Notification)
	assert user2.notifications[0].event == 'message'

def test_block_user():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello')
	user2.blocked_users.append(user1)
	assert user1 in user2.blocked_users
	assert message.send_message() == 'You are blocked from sending messages to this user.'
