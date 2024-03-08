import pytest
from user import User
from message import Message

def test_message_creation():
	user1 = User('test1@example.com', 'password1')
	user2 = User('test2@example.com', 'password2')
	message = Message(user1, user2, 'Hello, world!')
	assert message.get_content() == 'Hello, world!'


def test_set_content():
	user1 = User('test1@example.com', 'password1')
	user2 = User('test2@example.com', 'password2')
	message = Message(user1, user2, 'Hello, world!')
	message.set_content('Goodbye, world!')
	assert message.get_content() == 'Goodbye, world!'
