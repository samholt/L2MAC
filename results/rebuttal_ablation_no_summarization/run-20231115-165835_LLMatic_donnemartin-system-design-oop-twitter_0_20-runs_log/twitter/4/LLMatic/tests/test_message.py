import pytest
from message import Message
from user import User


def test_send_message():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello')
	assert message.send_message(user2, 'Hello').content == 'Hello'


def test_block_user():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello')
	message.block_user(user2)
	assert user2 in message.blocked_users


def test_unblock_user():
	user1 = User('user1@example.com', 'user1', 'password1')
	user2 = User('user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello')
	message.block_user(user2)
	message.unblock_user(user2)
	assert user2 not in message.blocked_users
