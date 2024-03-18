import pytest
from group import Group
from user import User

def test_group():
	admin = User('admin@example.com', 'password', 'admin_pic.jpg', 'Hello', 'public')
	group = Group('Test Group', 'picture.jpg', admin)
	assert group.name == 'Test Group'
	assert group.picture == 'picture.jpg'
	assert group.admins == [admin]
	assert group.participants == [admin]

	user = User('user@example.com', 'password', 'user_pic.jpg', 'Hi', 'public')
	group.add_participant(user)
	assert user in group.participants

	group.remove_participant(user)
	assert user not in group.participants

	group.add_admin(user)
	assert user not in group.admins

	group.add_participant(user)
	group.add_admin(user)
	assert user in group.admins

	group.remove_admin(user)
	assert user not in group.admins
