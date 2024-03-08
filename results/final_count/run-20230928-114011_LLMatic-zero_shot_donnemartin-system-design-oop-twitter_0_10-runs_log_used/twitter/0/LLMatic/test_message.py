import pytest
from message import Message

def test_message():
	message = Message()

	# Test sending and receiving messages
	assert message.send_message('user1', 'user2', 'Hello') == 'Message sent'
	assert message.receive_message('user2') == [('user1', 'Hello')]

	# Test blocking and unblocking users
	assert message.block_user('user2', 'user1') == 'User blocked'
	assert message.send_message('user1', 'user2', 'Hello again') == 'User is blocked'
	assert message.unblock_user('user2', 'user1') == 'User unblocked'
	assert message.send_message('user1', 'user2', 'Hello again') == 'Message sent'
