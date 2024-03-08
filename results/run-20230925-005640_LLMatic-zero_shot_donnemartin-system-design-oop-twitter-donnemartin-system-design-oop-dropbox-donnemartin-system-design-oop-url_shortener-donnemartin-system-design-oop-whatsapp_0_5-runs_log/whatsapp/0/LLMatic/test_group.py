import pytest
from group import Group
from user import User

def test_group():
	group = Group('Test Group', 'test.jpg')
	user1 = User('test1@test.com', 'password1')
	user2 = User('test2@test.com', 'password2')

	group.add_participant(user1)
	assert user1 in group.participants

	group.add_participant(user2)
	assert user2 in group.participants

	group.remove_participant(user1)
	assert user1 not in group.participants

	group.promote_to_admin(user2)
	assert user2 in group.admins

	group.demote_from_admin(user2)
	assert user2 not in group.admins
