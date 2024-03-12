import pytest
from message import Message
from user import User


def test_send_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	db = {}
	assert message.send_message(db) == 'Message sent.'
	assert db[message.timestamp] == message


def test_block_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	assert user1.block_user(user2) == 'User blocked.'
	assert user2 in user1.blocked_users
