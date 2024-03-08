import pytest
from message import Message
from user import User


def test_send_message():
	user1 = User()
	user2 = User()
	message = Message(user1, user2, 'Hello, world!')
	user1.set_status('online')
	user2.set_status('online')
	assert message.send_message() == {'sender': user1, 'receiver': user2, 'message': 'SGVsbG8sIHdvcmxkIQ==', 'timestamp': message.timestamp}
	user2.set_status('offline')
	message.send_message()
	assert user2.queue == [message]
