import pytest
from message import Message
from user import User

def test_send_text():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2)
	assert message.send_text('Hello') == 'Text message sent successfully'


def test_send_image():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2)
	assert message.send_image('image.jpg') == 'Image sent successfully'


def test_send_emoji():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2)
	assert message.send_emoji('😀') == 'Emoji sent successfully'


def test_send_gif():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2)
	assert message.send_gif('funny.gif') == 'GIF sent successfully'


def test_send_sticker():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2)
	assert message.send_sticker('cool.sticker') == 'Sticker sent successfully'


def test_send_queued_messages():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	user2.set_connectivity(False)
	message = Message(user1, user2)
	assert message.send_text('Hello') == 'Message queued'
	user2.set_connectivity(True)
	assert message.send_queued_messages() == 'Queued messages sent successfully'
