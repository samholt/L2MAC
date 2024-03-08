import pytest
from user import User
from message import Message


def test_set_status():
	user = User()
	user.set_status('online')
	assert user.get_status() == 'online'
	user.set_status('offline')
	assert user.get_status() == 'offline'


def test_add_to_queue():
	user1 = User()
	user2 = User()
	message = Message(user1, user2, 'Hello, world!')
	user1.add_to_queue(message)
	assert user1.queue == [message]


def test_send_queued_messages():
	user1 = User()
	user2 = User()
	message1 = Message(user1, user2, 'Hello, world!')
	message2 = Message(user1, user2, 'Goodbye, world!')
	user1.add_to_queue(message1)
	user1.add_to_queue(message2)
	user1.set_status('online')
	user1.send_queued_messages()
	assert user1.queue == []
