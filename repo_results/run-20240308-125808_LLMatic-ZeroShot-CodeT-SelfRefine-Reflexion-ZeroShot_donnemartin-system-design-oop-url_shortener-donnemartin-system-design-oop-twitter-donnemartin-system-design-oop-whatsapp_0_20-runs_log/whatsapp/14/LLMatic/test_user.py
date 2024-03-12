import pytest
from user import User, UserDatabase
from message import Message


def test_user_creation():
	user = User('test@test.com', 'password')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert user.online_status == False
	assert user.message_queue == []


def test_online_status():
	user = User('test@test.com', 'password')
	user.set_online_status(True)
	assert user.get_online_status() == True
	user.set_online_status(False)
	assert user.get_online_status() == False


def test_message_queue():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2, 'Hello')
	user1.queue_message(message)
	assert len(user1.message_queue) == 1
	user1.set_online_status(True)
	assert len(user1.message_queue) == 0
