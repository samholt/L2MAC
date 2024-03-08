import pytest
from chat import Chat
from user import User
from message import Message

def test_send_message():
	chat = Chat()
	sender = User()
	recipient = User()
	message = Message(sender, recipient, 'Hello', 'text')
	chat.send_message(sender, recipient, message)
	assert (sender, recipient, message) in chat.messages

def test_receive_message():
	chat = Chat()
	sender = User()
	recipient = User()
	message = Message(sender, recipient, 'Hello', 'text')
	chat.send_message(sender, recipient, message)
	received_message = chat.receive_message(sender, recipient, message)
	assert received_message == message

def test_encrypt_message():
	chat = Chat()
	message = 'Hello'
	encrypted_message = chat.encrypt_message(message)
	assert encrypted_message == message

def test_share_image():
	chat = Chat()
	sender = User()
	recipient = User()
	image = Message(sender, recipient, 'image_content', 'image')
	chat.share_image(sender, recipient, image)
	assert (sender, recipient, image) in chat.messages

def test_restore_connectivity():
	chat = Chat()
	sender = User()
	recipient = User()
	recipient.is_online = False
	message = Message(sender, recipient, 'Hello', 'text')
	chat.send_message(sender, recipient, message)
	assert (sender, recipient, message) in chat.offline_messages
	recipient.is_online = True
	chat.restore_connectivity(recipient)
	assert (sender, recipient, message) in chat.messages
	assert (sender, recipient, message) not in chat.offline_messages
