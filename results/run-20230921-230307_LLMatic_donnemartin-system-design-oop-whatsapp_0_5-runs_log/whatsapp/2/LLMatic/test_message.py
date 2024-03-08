import pytest
from message import Message
from cryptography.fernet import Fernet


def test_message_creation():
	message = Message('sender@example.com', 'receiver@example.com', 'Hello, world!')
	assert message.sender == 'sender@example.com'
	assert message.receiver == 'receiver@example.com'
	assert message.content == 'Hello, world!'
	assert message.read_status is False


def test_send_message():
	message = Message('sender@example.com', 'receiver@example.com', 'Hello, world!')
	message = message.send_message()
	assert message.sender == 'sender@example.com'
	assert message.receiver == 'receiver@example.com'
	assert message.content == 'Hello, world!'


def test_receive_message():
	message1 = Message('sender@example.com', 'receiver@example.com', 'Hello, world!')
	message2 = Message(None, None, None)
	message2.receive_message(message1)
	assert message2.sender == 'sender@example.com'
	assert message2.receiver == 'receiver@example.com'
	assert message2.content == 'Hello, world!'
	assert message2.read_status is False


def test_read_receipt():
	message = Message('sender@example.com', 'receiver@example.com', 'Hello, world!')
	message.read_receipt()
	assert message.read_status is True


def test_encrypt_decrypt_message():
	message = Message('sender@example.com', 'receiver@example.com', 'Hello, world!')
	key = Fernet.generate_key()
	message.encrypt_message(key)
	encrypted_content = message.content
	message.decrypt_message(key)
	decrypted_content = message.content
	assert encrypted_content != decrypted_content
	assert decrypted_content == 'Hello, world!'

