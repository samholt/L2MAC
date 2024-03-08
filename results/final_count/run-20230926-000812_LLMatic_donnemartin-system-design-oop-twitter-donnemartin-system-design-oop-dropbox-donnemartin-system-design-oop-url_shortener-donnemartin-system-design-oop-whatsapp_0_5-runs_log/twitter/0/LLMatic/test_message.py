import pytest
from user import User
from message import Message


def test_send_message():
	user1 = User('user1', 'user1', 'password1', False)
	user2 = User('user2', 'user2', 'password2', False)
	message = Message(user1, user2, 'Hello, user2!')
	assert message.send_message() == 'Message sent successfully.'
	assert len(user2.inbox) == 1
	assert user2.inbox[0].text == 'Hello, user2!'


def test_block_user():
	user1 = User('user1', 'user1', 'password1', False)
	user2 = User('user2', 'user2', 'password2', False)
	assert user1.block_user(user2) == 'user2 has been blocked.'
	assert user2 in user1.blocked_users


def test_unblock_user():
	user1 = User('user1', 'user1', 'password1', False)
	user2 = User('user2', 'user2', 'password2', False)
	user1.block_user(user2)
	assert user1.unblock_user(user2) == 'user2 has been unblocked.'
	assert user2 not in user1.blocked_users
