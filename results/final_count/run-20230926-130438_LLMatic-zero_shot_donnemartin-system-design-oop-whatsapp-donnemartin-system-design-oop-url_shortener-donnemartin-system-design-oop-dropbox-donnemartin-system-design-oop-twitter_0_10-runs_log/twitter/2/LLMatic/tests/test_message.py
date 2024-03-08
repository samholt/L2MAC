import pytest
from user import register_user
from message import send_message, block_user, unblock_user


def setup_module():
	# Populate the mock database before the tests are run
	register_user('test@test.com', 'testuser', 'testpassword')
	register_user('test2@test.com', 'testuser2', 'testpassword2')


def test_send_message():
	assert send_message('testuser', 'testuser2', 'Hello!') == 'Message sent successfully'
	assert send_message('testuser', 'wronguser', 'Hello!') == 'User not found'


def test_block_user():
	assert block_user('testuser', 'testuser2') == 'User blocked successfully'
	assert block_user('testuser', 'wronguser') == 'User not found'


def test_unblock_user():
	assert unblock_user('testuser', 'testuser2') == 'User unblocked successfully'
	assert unblock_user('testuser', 'testuser2') == 'User not blocked'
	assert unblock_user('testuser', 'wronguser') == 'User not found'
