from message import Message
from user import User
import pytest

def test_message_send_receive():
	sender = User('Alice', 'password', 'alice.jpg', 'Hello, I am Alice', 'public')
	receiver = User('Bob', 'password', 'bob.jpg', 'Hello, I am Bob', 'public')
	message = Message(sender, receiver, 'Hello, Bob!')
	assert message.send_message() == 'Message queued'

	receiver.set_online_status(True)
	assert message.send_message() == {'sender': sender, 'receiver': receiver, 'content': 'Hello, Bob!'}

	message.receive_message({'sender': receiver, 'receiver': sender, 'content': 'Hello, Alice!'})
	assert message.content == 'Hello, Alice!'
	assert message.read_status == True

def test_message_encryption():
	sender = User('Alice', 'password', 'alice.jpg', 'Hello, I am Alice', 'public')
	receiver = User('Bob', 'password', 'bob.jpg', 'Hello, I am Bob', 'public')
	message = Message(sender, receiver, 'Hello, Bob!')
	message.encrypt_message()
	assert message.content == 'Khoor, Ere!'
	assert message.encryption_status == True

	message.decrypt_message()
	assert message.content == 'Hello, Bob!'
	assert message.encryption_status == False

def test_message_queue():
	sender = User('Alice', 'password', 'alice.jpg', 'Hello, I am Alice', 'public')
	receiver = User('Bob', 'password', 'bob.jpg', 'Hello, I am Bob', 'public')
	message = Message(sender, receiver, 'Hello, Bob!')
	assert message.send_message() == 'Message queued'
	assert message.get_queued_messages() == ['Hello, Bob!']
