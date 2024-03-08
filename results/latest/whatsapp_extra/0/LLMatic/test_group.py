import pytest
from user import User
from group import Group


def test_group_functions():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	group = Group('Test Group', 'group_picture.jpg', [user1])

	# Test add participant
	group.add_participant(user2)
	assert user2 in group.participants

	# Test remove participant
	group.remove_participant(user2)
	assert user2 not in group.participants

	# Test promote to admin
	group.promote_to_admin(user1)
	assert user1 in group.admins

	# Test demote from admin
	group.demote_from_admin(user1)
	assert user1 not in group.admins
