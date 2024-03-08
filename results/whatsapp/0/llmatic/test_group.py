import pytest
from group import Group

def test_create_group():
	group = Group('Test Group', 'test.jpg', 'creator')
	group.create_group('New Group', 'new.jpg', 'new_creator')
	assert group.name == 'New Group'
	assert group.picture == 'new.jpg'
	assert 'new_creator' in group.participants
	assert 'new_creator' in group.admins

def test_manage_group():
	group = Group('Test Group', 'test.jpg', 'creator')
	group.manage_group('creator', 'add', 'participant')
	assert 'participant' in group.participants
	group.manage_group('creator', 'remove', 'participant')
	assert 'participant' not in group.participants

def test_administer_group():
	group = Group('Test Group', 'test.jpg', 'creator')
	group.administer_group('creator', 'add', 'admin')
	assert 'admin' in group.admins
	group.administer_group('creator', 'remove', 'admin')
	assert 'admin' not in group.admins
