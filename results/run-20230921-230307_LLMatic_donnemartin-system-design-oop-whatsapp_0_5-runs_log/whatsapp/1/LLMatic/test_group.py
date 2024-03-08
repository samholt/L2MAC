import pytest
from user import User
from group import Group


def test_group():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	group = Group('Test Group')

	group.add_participant(user1)
	assert user1 in group.participants

	group.remove_participant(user1)
	assert user1 not in group.participants

	group.add_participant(user1)
	group.promote_to_admin(user1)
	assert user1 in group.admins

	group.demote_from_admin(user1)
	assert user1 not in group.admins

	group.edit_group_name('New Test Group')
	assert group.name == 'New Test Group'

	group.edit_group_picture('new_picture.jpg')
	assert group.picture == 'new_picture.jpg'
