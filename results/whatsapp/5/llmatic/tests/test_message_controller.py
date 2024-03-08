import pytest
from models.user import User
from models.message import Message
from controllers.message_controller import MessageController


def test_message_queue():
	message_controller = MessageController()
	sender = User(id='sender_id', email='sender@example.com', password='password', profile_picture='profile_picture.jpg', status_message='Hello, world!', privacy_settings={}, blocked_contacts=[])
	receiver = User(id='receiver_id', email='receiver@example.com', password='password', profile_picture='profile_picture.jpg', status_message='Hello, world!', privacy_settings={}, blocked_contacts=[])
	message_controller.send_message(sender, receiver, 'Hello, world!')
	assert len(message_controller.message_queue) == 1
	receiver.online_status = True
	message_controller.process_message_queue()
	assert len(message_controller.message_queue) == 0
