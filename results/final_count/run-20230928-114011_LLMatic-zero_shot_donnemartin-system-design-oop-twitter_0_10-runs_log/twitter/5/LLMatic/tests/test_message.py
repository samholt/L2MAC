import pytest
from message import Message


def test_send_message():
	message = Message('Hello', 'User1', 'User2')
	assert message.send_message() == 'Message sent'


def test_delete_message():
	message = Message('Hello', 'User1', 'User2')
	assert message.delete_message() == 'Message deleted'


def test_block_user():
	message = Message('Hello', 'User1', 'User2')
	message.block_user('User2')
	assert 'User2' in message.blocked_users
	assert message.send_message() == 'User is blocked'


def test_unblock_user():
	message = Message('Hello', 'User1', 'User2')
	message.block_user('User2')
	message.unblock_user('User2')
	assert 'User2' not in message.blocked_users
	assert message.send_message() == 'Message sent'
