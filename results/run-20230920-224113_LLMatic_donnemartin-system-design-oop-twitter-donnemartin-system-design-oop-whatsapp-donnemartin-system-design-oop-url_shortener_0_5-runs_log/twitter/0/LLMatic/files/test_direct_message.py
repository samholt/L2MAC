import pytest
from user import User
from direct_message import DirectMessage


def test_send_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	dm.send_message()
	assert dm in user2.direct_messages


def test_receive_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	dm.send_message()
	received_message = user2.receive_message()
	assert received_message == dm
