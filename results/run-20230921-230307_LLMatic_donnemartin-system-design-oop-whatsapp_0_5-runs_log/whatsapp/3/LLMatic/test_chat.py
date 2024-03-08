import pytest
from user import User
from chat import Chat
from message import Message


def test_send_message():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	chat = Chat(user1, user2)
	chat.send_message(user1, user2, 'Hello!')
	assert len(chat.messages) == 1
	assert chat.messages[0].content == 'Hello!'


def test_receive_message():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	chat = Chat(user1, user2)
	message = Message('Hello!', user1, user2)
	chat.receive_message(message)
	assert message.content == 'Hello!'


def test_encrypt_decrypt_message():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	chat = Chat(user1, user2)
	message = Message('Hello!', user1, user2)
	chat.encrypt_message(message)
	assert message.content != 'Hello!'
	chat.decrypt_message(message)
	assert message.content == 'Hello!'


def test_handle_read_receipt():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	chat = Chat(user1, user2)
	message = Message('Hello!', user1, user2)
	chat.handle_read_receipt(message)
	assert message.read
