import pytest
from group import Group
from user import User
from message import Message

def test_group():
	admin = User('admin@example.com', 'password')
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	group = Group('Test Group', admin)

	# Test adding participants
	group.add_participant(user1)
	group.add_participant(user2)
	assert len(group.participants) == 3

	# Test removing participants
	group.remove_participant(user1)
	assert len(group.participants) == 2

	# Test assigning admin
	group.assign_admin(user2)
	assert group.participants[user2] == 'admin'

	# Test adding messages
	message = Message(admin, group, 'Hello, world!')
	group.add_message(message)
	assert len(group.group_chat) == 1
