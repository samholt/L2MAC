import pytest
from user import User
from message import Message

def test_message_sending():
	user1 = User('test1@test.com', 'test1', 'password1')
	user2 = User('test2@test.com', 'test2', 'password2')
	message = Message(user1, user2, 'Hello, World!')
	assert message.send() == True
	assert len(user2.inbox) == 1
	assert user2.inbox[0].text == 'Hello, World!'

	message.block()
	assert message.send() == False
	assert len(user2.inbox) == 1

	message.unblock()
	assert message.send() == True
	assert len(user2.inbox) == 2
