import pytest
from message import Message


def test_send():
	message = Message('user1', 'user2', 'Hello')
	assert message.send() == {'sender': 'user1', 'receiver': 'user2', 'content': 'Hello', 'timestamp': message.timestamp, 'read_receipt': False, 'type': 'text'}


def test_receive():
	message = Message('user1', 'user2', 'Hello')
	message.send()
	assert message.receive() == 'Hello'


def test_read():
	message = Message('user1', 'user2', 'Hello')
	message.send()
	message.receive()
	assert message.read() == 'Hello'


def test_encrypt():
	message = Message('user1', 'user2', 'Hello')
	message.encryption = True
	assert message.encrypt() == 'SGVsbG8='


def test_decrypt():
	message = Message('user1', 'user2', 'SGVsbG8=')
	message.encryption = True
	assert message.decrypt() == 'Hello'


def test_send_emoji():
	message = Message('user1', 'user2', '')
	assert message.send_emoji('😀') == '😀'
