import pytest
from message import Message

def test_message_creation():
	message = Message('user1', 'user2', 'Hello, world!', 'text')
	assert message.sender == 'user1'
	assert message.recipient == 'user2'
	assert message.content == 'Hello, world!'
	assert message.content_type == 'text'

def test_get_content():
	message = Message('user1', 'user2', 'Hello, world!', 'text')
	assert message.get_content() == 'Hello, world!'

def test_get_content_type():
	message = Message('user1', 'user2', 'Hello, world!', 'text')
	assert message.get_content_type() == 'text'
