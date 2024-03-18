import pytest
from message import Message

def test_send_and_receive_message():
	m = Message()
	m.send_message('user1', 'user2', 'Hello')
	messages = m.get_messages('user2')
	assert len(messages) == 1
	assert messages[0] == ('user1', 'Hello')

	m.send_message('user2', 'user1', 'Hi')
	messages = m.get_messages('user1')
	assert len(messages) == 1
	assert messages[0] == ('user2', 'Hi')
