import pytest
from models.user import User
from models.direct_message import DirectMessage


def test_direct_message():
	user1 = User('user1', 'password')
	user2 = User('user2', 'password')
	message = 'Hello, user2!'
	dm = DirectMessage(user1, user2, message)
	assert dm.sender == user1
	assert dm.recipient == user2
	assert dm.content == message

