import pytest
from message import Message


def test_send_message():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	assert message.send_message() == {'sender': 'sender@test.com', 'receiver': 'receiver@test.com', 'content': 'Hello!', 'timestamp': message.timestamp, 'read_receipt': False, 'encrypted': False, 'message_type': 'text'}


def test_receive_message():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	message_data = {'sender': 'new_sender@test.com', 'receiver': 'new_receiver@test.com', 'content': 'New message!', 'timestamp': message.timestamp, 'read_receipt': True, 'encrypted': True, 'message_type': 'image'}
	message.receive_message(message_data)
	assert message.send_message() == message_data


def test_set_read_receipt():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	message.set_read_receipt()
	assert message.get_read_receipt() == True


def test_encrypt_decrypt_message():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	message.encrypt_message()
	assert message.encrypted == True
	message.decrypt_message()
	assert message.encrypted == False


def test_handle_message_type():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	message.handle_message_type('image')
	assert message.message_type == 'image'
