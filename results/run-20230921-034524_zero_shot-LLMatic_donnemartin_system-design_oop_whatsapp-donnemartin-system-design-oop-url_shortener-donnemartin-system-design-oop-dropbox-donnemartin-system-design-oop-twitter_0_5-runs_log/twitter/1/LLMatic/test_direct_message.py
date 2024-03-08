import pytest
from user import User
from direct_message import DirectMessage


def test_direct_message():
	sender = User('sender')
	receiver = User('receiver')
	message = DirectMessage(sender, receiver, 'Hello!')

	assert message.sender == sender
	assert message.receiver == receiver
	assert message.content == 'Hello!'
