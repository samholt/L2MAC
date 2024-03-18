import pytest
from user import User
from message import Message

def test_send_receive_message():
	user1 = User('user1', 'user1@test.com', 'testpassword')
	user2 = User('user2', 'user2@test.com', 'testpassword')
	message = Message(user1, user2, 'Hello, user2!')
	assert message.send() == True
	assert message in user2.inbox

	message2 = Message(user2, user1, 'Hello, user1!')
	assert message2.receive() == True
	assert message2 in user1.inbox

def test_block_unblock_user():
	user1 = User('user1', 'user1@test.com', 'testpassword')
	user2 = User('user2', 'user2@test.com', 'testpassword')
	user1.block_user(user2)
	assert user2 in user1.blocked_users

	message = Message(user2, user1, 'Hello, user1!')
	assert message.send() == False
	assert message not in user1.inbox

	user1.unblock_user(user2)
	assert user2 not in user1.blocked_users

	message2 = Message(user2, user1, 'Hello again, user1!')
	assert message2.send() == True
	assert message2 in user1.inbox
