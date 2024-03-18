import pytest
from message import Message
from user import User

def test_message_sending():
	user1 = User(1, 'user1@example.com', 'user1', 'password1')
	user2 = User(2, 'user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	message.send_message()
	assert message in user2.messages

def test_message_receiving():
	user1 = User(1, 'user1@example.com', 'user1', 'password1')
	user2 = User(2, 'user2@example.com', 'user2', 'password2')
	message = Message(user1, user2, 'Hello, user2!')
	message.receive_message()
	assert message in user1.messages
