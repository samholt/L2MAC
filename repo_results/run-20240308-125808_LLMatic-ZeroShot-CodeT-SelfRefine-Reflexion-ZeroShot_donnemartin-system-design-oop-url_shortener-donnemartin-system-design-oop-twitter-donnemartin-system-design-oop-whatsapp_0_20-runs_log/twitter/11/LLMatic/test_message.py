import pytest
from message import Message
from user import User


def test_send_message():
	user1 = User('1', 'user1', 'email1', 'password1', False)
	user2 = User('2', 'user2', 'email2', 'password2', False)
	message = Message(user1, user2, 'Hello')
	db = {}
	assert message.send(db) == 'Message sent'
	assert db[message.id] == message


def test_block_user():
	user1 = User('1', 'user1', 'email1', 'password1', False)
	user2 = User('2', 'user2', 'email2', 'password2', False)
	message = Message(user1, user2, 'Hello')
	assert message.block_user(user2) == 'User blocked'
	assert user2 in message.receiver.blocked_users


def test_unblock_user():
	user1 = User('1', 'user1', 'email1', 'password1', False)
	user2 = User('2', 'user2', 'email2', 'password2', False)
	message = Message(user1, user2, 'Hello')
	message.block_user(user2)
	assert message.unblock_user(user2) == 'User unblocked'
	assert user2 not in message.receiver.blocked_users

