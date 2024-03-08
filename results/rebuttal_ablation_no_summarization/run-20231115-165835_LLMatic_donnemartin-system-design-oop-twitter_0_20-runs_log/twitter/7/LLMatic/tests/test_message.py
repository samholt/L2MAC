import pytest
import message


def test_send_message():
	message_1 = message.send_message('Hello', 'user1', 'user2')
	assert message_1 is not None
	assert message_1.text == 'Hello'
	assert message_1.sender == 'user1'
	assert message_1.receiver == 'user2'

	# Test sending a message to a blocked user
	message.block_user('user2', 'user1')
	message_2 = message.send_message('Hello', 'user1', 'user2')
	assert message_2 is None


def test_block_user():
	result = message.block_user('user1', 'user2')
	assert result is True
	assert 'user2' in message.blocked_users['user1']


def test_unblock_user():
	result = message.unblock_user('user1', 'user2')
	assert result is True
	assert 'user2' not in message.blocked_users['user1']
