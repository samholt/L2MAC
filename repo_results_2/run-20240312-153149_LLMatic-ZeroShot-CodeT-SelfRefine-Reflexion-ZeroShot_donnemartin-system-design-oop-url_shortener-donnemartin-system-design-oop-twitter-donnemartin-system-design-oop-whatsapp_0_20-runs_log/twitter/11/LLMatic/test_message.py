import pytest
from message import Message

def test_send_message():
	m = Message()
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
	assert m.send('user2', 'user1', 'Hi') == 'Message sent'
	assert ('user1', 'Hello') in m.messages['user2']
	assert ('user2', 'Hi') in m.messages['user1']

def test_block_user():
	m = Message()
	assert m.block_user('user1', 'user2') == 'User blocked'
	assert 'user2' in m.blocked_users['user1']
	assert m.send('user1', 'user2', 'Hello') == 'User is blocked'

def test_unblock_user():
	m = Message()
	m.block_user('user1', 'user2')
	assert m.unblock_user('user1', 'user2') == 'User unblocked'
	assert 'user2' not in m.blocked_users['user1']
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
