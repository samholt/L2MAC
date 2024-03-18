import pytest
from message import Message, mock_message_db
from user import User

def test_message_creation():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello')
	assert message.sender == 'sender@test.com'
	assert message.receiver == 'receiver@test.com'
	assert message.content == 'Hello'
	assert message.read_receipt == False
	assert message.encrypted == False

	message.encrypt_content()
	assert message.content == 'Khoor'
	assert message.encrypted == True
