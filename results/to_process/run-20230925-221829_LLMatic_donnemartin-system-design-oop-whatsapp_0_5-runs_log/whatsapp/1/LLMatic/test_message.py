import pytest
from message import Message


def test_send_message():
	messages = []
	message = Message('Alice', 'Bob', 'Hello, Bob!')
	messages = message.send_message(messages)
	assert len(messages) == 1
	assert messages[0].content == 'Hello, Bob!'


def test_receive_message():
	messages = [Message('Alice', 'Bob', 'Hello, Bob!')]
	message = Message('Alice', 'Bob', '')
	messages = message.receive_message(messages)
	assert messages[0].read_receipt == True


def test_set_read_receipt():
	message = Message('Alice', 'Bob', 'Hello, Bob!')
	message.set_read_receipt()
	assert message.read_receipt == True


def test_encrypt_decrypt_message():
	message = Message('Alice', 'Bob', 'Hello, Bob!')
	message.encrypt_message()
	assert message.content != 'Hello, Bob!'
	decrypted_message = message.decrypt_message()
	assert decrypted_message == 'Hello, Bob!'


def test_share_image():
	message = Message('Alice', 'Bob', 'Hello, Bob!')
	message.share_image('image.png')
	assert message.image == 'image.png'

