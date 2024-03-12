import pytest
from message import Message


def test_message_creation():
	message = Message('sender', 'receiver', 'content')
	assert message.sender == 'sender'
	assert message.receiver == 'receiver'
	assert message.content == 'content'
	assert message.read_status == False
	assert message.encryption_status == False
	assert message.image == None
	assert message.emojis_gifs_stickers == []


def test_mark_as_read():
	message = Message('sender', 'receiver', 'content')
	message.mark_as_read()
	assert message.read_status == True


def test_encrypt():
	message = Message('sender', 'receiver', 'content')
	message.encrypt()
	assert message.encryption_status == True


def test_add_image():
	message = Message('sender', 'receiver', 'content')
	message.add_image('image')
	assert message.image == 'image'


def test_add_emojis_gifs_stickers():
	message = Message('sender', 'receiver', 'content')
	message.add_emojis_gifs_stickers('emoji')
	assert 'emoji' in message.emojis_gifs_stickers
