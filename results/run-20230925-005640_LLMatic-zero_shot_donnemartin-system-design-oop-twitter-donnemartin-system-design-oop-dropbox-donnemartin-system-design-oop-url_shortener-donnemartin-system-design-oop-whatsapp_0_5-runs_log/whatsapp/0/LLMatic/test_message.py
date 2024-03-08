import pytest
from message import Message
from user import User
from database import Database


def test_message_creation():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2, 'Hello, World!')
	assert message.sender == user1
	assert message.receiver == user2
	assert message.content == 'Hello, World!'
	assert message.queued == False


def test_send_message():
	db = Database()
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2, 'Hello, World!')
	message.send(db)
	assert message.queued == True
	user2.set_online_status(True)
	db.add_message(message)
	assert message.queued == False
