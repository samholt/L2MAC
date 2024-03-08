import pytest
from group import Group, create_group, mock_db

def test_group_creation():
	response = create_group('Test Group', 'test.jpg', 'admin@test.com')
	assert response == 'Group created successfully'
	assert 'Test Group' in mock_db
	group = mock_db['Test Group']
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'
	assert group.admin == 'admin@test.com'
	assert group.participants == {'admin@test.com'}

def test_add_remove_participant():
	group = Group('Test Group', 'test.jpg', 'admin@test.com')
	group.add_participant('user@test.com')
	assert 'user@test.com' in group.participants
	group.remove_participant('user@test.com')
	assert 'user@test.com' not in group.participants

def test_set_admin():
	group = Group('Test Group', 'test.jpg', 'admin@test.com')
	group.add_participant('user@test.com')
	group.set_admin('user@test.com')
	assert group.admin == 'user@test.com'

