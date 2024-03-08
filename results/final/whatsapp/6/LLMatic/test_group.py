import pytest
from user import User
from group import Group


def test_group():
	# Mock database
	db = {}

	# Create users
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')

	# Create group
	group = Group('Test Group', 'picture.jpg', user1)

	# Test add participant
	assert group.add_participant(user2) == 'User added successfully'
	assert group.add_participant(user2) == 'User already in the group'

	# Test remove participant
	assert group.remove_participant(user2) == 'User removed successfully'
	assert group.remove_participant(user2) == 'User not in the group'

	# Test set admin
	assert group.set_admin(user2) == 'User not in the group'
	group.add_participant(user2)
	assert group.set_admin(user2) == 'Admin set successfully'

	# Test send message
	message_id = group.send_message('Hello, world!', db)
	assert db[message_id].content == 'Hello, world!'
