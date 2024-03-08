import pytest
from user import User
from direct_message import DirectMessage


def test_send_direct_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	message = DirectMessage(user1, user2, 'Hello, user2!')
	user1.send_direct_message(user2, message)
	assert message in user2.direct_messages
