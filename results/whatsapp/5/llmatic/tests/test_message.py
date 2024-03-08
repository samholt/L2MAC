import pytest
from models.user import User
from models.message import Message
from controllers.message_controller import MessageController


def test_message():
	user1 = User(id='user1', email='user1@example.com', password='password', profile_picture='profile_picture', status_message='status_message', privacy_settings={}, blocked_contacts=[])
	user2 = User(id='user2', email='user2@example.com', password='password', profile_picture='profile_picture', status_message='status_message', privacy_settings={}, blocked_contacts=[])
	message_controller = MessageController()
	message_controller.send_message(user1, user2, 'Hello, world!')
	message = message_controller.messages[0]
	assert message.sender == user1
	assert message.receiver == user2
	assert message.content == 'Hello, world!'
	assert message.read_receipt == False
	message_controller.receive_message(message)
	assert message.read_receipt == True

