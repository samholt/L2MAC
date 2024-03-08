import pytest
from user import User
from contact import Contact
from message import Message


def test_message_send():
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	message = Message(user1, user2, 'Hello')
	message.send()
	assert message.is_read == False


def test_message_read():
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	message = Message(user1, user2, 'Hello')
	message.read()
	assert message.is_read == True


def test_message_encrypt():
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	message = Message(user1, user2, 'Hello')
	message.encrypt()
	assert message.is_encrypted == True


def test_message_add_attachment():
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	message = Message(user1, user2, 'Hello')
	message.add_attachment('path/to/file')
	assert 'path/to/file' in message.attachments
