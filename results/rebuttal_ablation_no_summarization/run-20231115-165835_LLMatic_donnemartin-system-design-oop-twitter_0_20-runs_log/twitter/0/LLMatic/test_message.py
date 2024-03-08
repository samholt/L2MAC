import pytest
from message import Message

def test_send_message():
	message = Message('user1', 'user2')
	assert message.send_message('Hello', '2022-01-01 00:00:00') == 'Message sent'
	assert message.database['2022-01-01 00:00:00'] == {'sender': 'user1', 'receiver': 'user2', 'text': 'Hello'}

	message.block_user('user2')
	assert message.send_message('Hello', '2022-01-01 00:01:00') == 'User is blocked'


def test_block_user():
	message = Message('user1', 'user2')
	message.block_user('user2')
	assert 'user2' in message.blocked_users
