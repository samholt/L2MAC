import pytest
from user import User, Auth


def test_block_unblock_contact():
	auth = Auth()
	auth.sign_up('test1@test.com', 'password1')
	auth.sign_up('test2@test.com', 'password2')
	user1 = auth.users['test1@test.com']
	user2 = auth.users['test2@test.com']

	user1.block_contact(user2.email)
	assert user2.email in user1.blocked_contacts

	user1.unblock_contact(user2.email)
	assert user2.email not in user1.blocked_contacts

def test_queue_message():
	auth = Auth()
	auth.sign_up('test1@test.com', 'password1')
	user1 = auth.users['test1@test.com']

	user1.queue_message('Hello')
	assert 'Hello' in user1.queued_messages

	user1.set_online_status(True)
	assert user1.online_status

	user1.set_online_status(False)
	assert not user1.online_status

	user1.receive_message('Hello')
	assert 'Hello' not in user1.queued_messages
