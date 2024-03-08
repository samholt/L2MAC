from message import Message
from user import User, users_db

def test_send_message():
	User.register('user1', 'user1@email.com', 'password1')
	User.register('user2', 'user2@email.com', 'password2')
	assert Message.send_message('user1', 'user2', 'Hello!')

def test_block_user():
	User.register('user1', 'user1@email.com', 'password1')
	User.register('user2', 'user2@email.com', 'password2')
	assert Message.block_user('user1', 'user2')
	assert 'user2' in users_db['user1'].blocked_users

def test_unblock_user():
	User.register('user1', 'user1@email.com', 'password1')
	User.register('user2', 'user2@email.com', 'password2')
	Message.block_user('user1', 'user2')
	assert Message.unblock_user('user1', 'user2')
	assert 'user2' not in users_db['user1'].blocked_users
