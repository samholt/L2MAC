import pytest
from message import Message

def test_message_encryption():
	message = Message('sender@test.com', 'recipient@test.com', 'Hello, World!')
	message.encrypt()
	assert message.content == 'Khoor/#Zruog$'
	assert message.encryption_status == True

	message.decrypt()
	assert message.content == 'Hello, World!'
	assert message.encryption_status == False

def test_message_read():
	message = Message('sender@test.com', 'recipient@test.com', 'Hello, World!')
	message.read()
	assert message.read_status == True
