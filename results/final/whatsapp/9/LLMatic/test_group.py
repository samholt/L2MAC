import pytest
from group import Group
from user import User
from message import Message

def test_group():
	group = Group('Test Group', 'test.jpg', [], [], [])
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, 'Hello, World!')

	group.add_participant(user1)
	assert user1 in group.participants

	group.remove_participant(user1)
	assert user1 not in group.participants

	group.assign_admin(user2)
	assert user2 in group.admins

	group.remove_admin(user2)
	assert user2 not in group.admins

	group.send_message(message)
	assert message in group.messages
