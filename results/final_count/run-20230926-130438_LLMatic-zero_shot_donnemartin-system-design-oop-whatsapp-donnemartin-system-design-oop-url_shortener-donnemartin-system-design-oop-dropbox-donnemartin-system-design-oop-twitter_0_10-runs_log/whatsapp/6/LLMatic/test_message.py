import pytest
from message import Message

def test_queue_offline_message():
	message = Message()
	message.queue_offline_message('user1', 'user2', 'Hello')
	assert message.get_offline_messages('user2') == [('user1', 'Hello')]

	message.queue_offline_message('user1', 'user2', 'Hi')
	assert message.get_offline_messages('user2') == [('user1', 'Hello'), ('user1', 'Hi')]

	assert message.get_offline_messages('user1') == []

