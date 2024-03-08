import pytest
from user import User
from message import Message


def test_message():
	user = User('test@example.com', 'password')
	message = Message(user, '')

	message.set_text('Hello, world!')
	assert message.content == 'Hello, world!'

	message.set_image('image.jpg')
	assert message.content == 'image.jpg'

	message.set_emoji('😀')
	assert message.content == '😀'
