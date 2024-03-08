import pytest
from user import User
from chat import Chat

def test_send_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	chat = Chat(user1, user2)
	message = chat.send_message(user1, 'Hello, user2!')
	assert message.content == 'Hello, user2!'

def test_receive_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	chat = Chat(user1, user2)
	chat.send_message(user1, 'Hello, user2!')
	message = chat.receive_message()
	assert message.content == 'Hello, user2!'

def test_encrypt_message():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	chat = Chat(user1, user2)
	message = chat.send_message(user1, 'Hello, user2!')
	encrypted_message = chat.encrypt_message(message)
	assert encrypted_message.content == '!2resu ,olleH'
