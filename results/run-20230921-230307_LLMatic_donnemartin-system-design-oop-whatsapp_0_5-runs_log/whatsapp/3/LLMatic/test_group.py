import pytest
from group import Group
from user import User

def test_add_participant():
	group = Group('Test Group', 'picture.png', User('admin@example.com', 'password'))
	user = User('user@example.com', 'password')
	group.add_participant(user)
	assert user in group.participants

def test_remove_participant():
	group = Group('Test Group', 'picture.png', User('admin@example.com', 'password'))
	user = User('user@example.com', 'password')
	group.add_participant(user)
	group.remove_participant(user)
	assert user not in group.participants

def test_manage_admin_roles():
	group = Group('Test Group', 'picture.png', User('admin@example.com', 'password'))
	user = User('user@example.com', 'password')
	group.add_participant(user)
	group.manage_admin_roles(user, True)
	assert user.admin == True
	group.manage_admin_roles(user, False)
	assert user.admin == False
