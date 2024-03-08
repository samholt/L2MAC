import pytest
from group import Group


def test_group_management():
	group = Group()
	assert group.create_group('test_group', 'admin@test.com', 'group_picture.jpg') == 'Group created successfully'
	assert 'group_picture.jpg' == group.get_group('test_group')['picture']
	assert group.add_member('test_group', 'member@test.com') == 'Member added successfully'
	assert 'member@test.com' in group.get_group('test_group')['members']
	assert group.remove_member('test_group', 'member@test.com') == 'Member removed successfully'
	assert 'member@test.com' not in group.get_group('test_group')['members']
	assert group.block_member('test_group', 'blocked@test.com') == 'Member blocked successfully'
	assert 'blocked@test.com' in group.get_group('test_group')['blocked_members']
	assert group.unblock_member('test_group', 'blocked@test.com') == 'Member unblocked successfully'
	assert 'blocked@test.com' not in group.get_group('test_group')['blocked_members']
