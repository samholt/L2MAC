import pytest
from message import Message
from user import User

def test_send_message():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1')
	user2 = User('test2@test.com', 'testuser2', 'testpassword2')
	message = Message(user1, user2, 'Hello!')
	assert message.send_message() == 'Message not sent. You are blocked by the recipient.'
