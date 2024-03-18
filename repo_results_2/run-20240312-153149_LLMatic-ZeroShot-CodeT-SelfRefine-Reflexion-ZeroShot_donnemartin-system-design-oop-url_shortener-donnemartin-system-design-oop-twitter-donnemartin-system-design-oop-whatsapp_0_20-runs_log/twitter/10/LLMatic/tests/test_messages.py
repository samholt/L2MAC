import pytest
from models import User, Message
from database import users


def test_send_message():
	users.clear()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	assert user1.send_message(user2, 'Hello') == {'message': 'Message sent successfully'}
	assert len(user1.messages) == 1
	assert len(user2.messages) == 1
	assert user1.messages[0].content == 'Hello'
	assert user2.messages[0].content == 'Hello'


def test_get_messages():
	users.clear()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	user1.send_message(user2, 'Hello')
	messages = user1.get_messages()
	assert len(messages) == 1
	assert messages[0]['content'] == 'Hello'


def test_block_user():
	users.clear()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	user1.block(user2)
	assert user2 in user1.blocked
	assert user1.send_message(user2, 'Hello') == {'message': 'This user has blocked you'}
	assert len(user1.messages) == 0
	assert len(user2.messages) == 0


def test_unblock_user():
	users.clear()
	user1 = User('user1@example.com', 'user1', 'password')
	user2 = User('user2@example.com', 'user2', 'password')
	users[user1.email] = user1
	users[user2.email] = user2
	user1.block(user2)
	user1.unblock(user2)
	assert user2 not in user1.blocked
	assert user1.send_message(user2, 'Hello') == {'message': 'Message sent successfully'}
	assert len(user1.messages) == 1
	assert len(user2.messages) == 1
	assert user1.messages[0].content == 'Hello'
	assert user2.messages[0].content == 'Hello'
