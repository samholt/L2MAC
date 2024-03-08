import pytest
from message import Message
from user import User


def test_send_message():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	assert message.send_message() == 'Message sent successfully'
	assert message in user2.messages


def test_block_user():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	assert message.block_user(user1) == 'User blocked successfully'
	assert user1 in message.blocked_users


def test_unblock_user():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	message.block_user(user1)
	assert message.unblock_user(user1) == 'User unblocked successfully'
	assert user1 not in message.blocked_users
