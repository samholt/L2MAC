import pytest
from group import Group


def test_group_management():
	group = Group('Test Group', 'admin@test.com', 'group_picture.jpg')

	group.manage_group('add', 'member1@test.com')
	assert 'member1@test.com' in group.members

	group.manage_group('remove', 'member1@test.com')
	assert 'member1@test.com' not in group.members

	group.edit_group('New Test Group', 'new_group_picture.jpg')
	assert group.name == 'New Test Group'
	assert group.picture == 'new_group_picture.jpg'

	group.manage_group('add', 'member2@test.com')
	group.manage_admin_roles('add', 'member2@test.com')
	assert 'member2@test.com' in group.admins

	group.manage_admin_roles('remove', 'member2@test.com')
	assert 'member2@test.com' not in group.admins
