import pytest
from services.message import send_message, receive_message, send_emoji, send_gif, send_sticker


def test_send_message():
	message = send_message(1, 2, 'Hello, world!', 'encryption_key')
	assert message.sender_id == 1
	assert message.receiver_id == 2
	assert message.text == 'Hello, world!'
	assert message.read_status == False
	assert message.encryption_key == 'encryption_key'

def test_receive_message():
	message = receive_message(1, 2)
	assert message.sender_id == 1
	assert message.receiver_id == 2
	assert message.text == 'Hello, world!'
	assert message.read_status == False
	assert message.encryption_key == 'encryption_key'

def test_send_emoji():
	message = send_emoji(1, 2, '😀')
	assert message.text == '😀'

def test_send_gif():
	message = send_gif(1, 2, 'gif')
	assert message.text == 'gif'

def test_send_sticker():
	message = send_sticker(1, 2, 'sticker')
	assert message.text == 'sticker'
