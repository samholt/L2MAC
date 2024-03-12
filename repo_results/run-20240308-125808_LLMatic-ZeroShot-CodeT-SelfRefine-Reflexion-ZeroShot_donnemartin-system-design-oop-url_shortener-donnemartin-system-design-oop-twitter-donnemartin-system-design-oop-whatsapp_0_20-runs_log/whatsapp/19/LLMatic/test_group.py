import pytest
from group import Group

def test_group_creation():
	group = Group('Test Group', 'test.jpg')
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'


def test_add_remove_participant():
	group = Group('Test Group', 'test.jpg')
	group.add_participant('User1')
	assert 'User1' in group.participants
	group.remove_participant('User1')
	assert 'User1' not in group.participants


def test_manage_admin_roles_and_permissions():
	group = Group('Test Group', 'test.jpg')
	group.admins.append('Admin1')
	group.manage_admin_roles_and_permissions('Admin1', 'all')
	for admin in group.admins:
		if admin[0] == 'Admin1':
			assert admin[1] == 'all'
