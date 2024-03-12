import pytest
from message import Message, ImageMessage, EmojiMessage


def test_message_send_receive():
	message = Message('Alice', 'Bob', 'Hello')
	message.send_message()
	message.receive_message()
	assert message.is_read() == True


def test_message_encryption():
	message = Message('Alice', 'Bob', 'Hello')
	message.encrypt_message()
	assert message.is_encrypted() == True
	message.decrypt_message()
	assert message.is_encrypted() == False


def test_image_message():
	message = ImageMessage('Alice', 'Bob', 'Hello', 'image.jpg')
	message.send_message()


def test_emoji_message():
	message = EmojiMessage('Alice', 'Bob', 'Hello', 'emoji.png')
	message.send_message()
