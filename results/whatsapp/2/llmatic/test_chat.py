import pytest
from chat import Chat
from user import User

def test_chat():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	chat = Chat(user1, user2)

	# Test message sending and receiving
	chat.send_message(user1, user2, 'Hello, world!')
	assert len(chat.messages) == 1
	assert chat.messages[0] == (user1, user2, 'Hello, world!')
	assert not chat.read_receipts[(user1, user2, 'Hello, world!')]

	chat.receive_message(user1, user2, 'Hello, world!')
	assert chat.read_receipts[(user1, user2, 'Hello, world!')]
