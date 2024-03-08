import pytest
from user import User
from direct_message import DirectMessage


def test_direct_message_creation():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	assert dm.sender == user1
	assert dm.receiver == user2
	assert dm.message == message


def test_send_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	dm.send_message()
	assert dm in user2.inbox


def test_receive_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	dm.send_message()
	inbox = user2.receive_message()
	assert dm in inbox
