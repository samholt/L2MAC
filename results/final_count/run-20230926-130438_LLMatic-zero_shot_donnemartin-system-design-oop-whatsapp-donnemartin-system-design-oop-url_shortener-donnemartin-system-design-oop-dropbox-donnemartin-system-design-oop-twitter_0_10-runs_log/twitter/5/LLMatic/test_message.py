import pytest
from message import Message

def test_send():
	message = Message()
	assert message.send('user1', 'user2', 'Hello') == 'Message sent'
	assert message.send('user2', 'user1', 'Hello') == 'Message sent'
	message.block('user1', 'user2')
	assert message.send('user2', 'user1', 'Hello') == 'User is blocked'


def test_block():
	message = Message()
	assert message.block('user1', 'user2') == 'User blocked'
	assert 'user2' in message.blocked_users['user1']


def test_unblock():
	message = Message()
	message.block('user1', 'user2')
	assert message.unblock('user1', 'user2') == 'User unblocked'
	assert 'user2' not in message.blocked_users['user1']
