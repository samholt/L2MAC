import pytest
from message import Message

def test_send_message():
	m = Message()
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
	assert m.send('user1', 'user2', 'Hello again') == 'Message sent'
	assert m.send('user2', 'user1', 'Hi') == 'Message sent'

	# Test blocking
	assert m.block_user('user2', 'user1') == 'User blocked'
	assert m.send('user1', 'user2', 'Blocked message') == 'User is blocked'

	# Test unblocking
	assert m.unblock_user('user2', 'user1') == 'User unblocked'
	assert m.send('user1', 'user2', 'Unblocked message') == 'Message sent'
