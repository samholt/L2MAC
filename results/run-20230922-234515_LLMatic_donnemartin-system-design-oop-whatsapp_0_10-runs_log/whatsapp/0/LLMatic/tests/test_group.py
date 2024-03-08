import pytest
from services.group import create_group, add_participant, remove_participant, set_admin


def test_create_group():
	group = create_group('Test Group', 'test.jpg', 1)
	assert group.id is not None
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'
	assert group.admin_id == 1

def test_add_remove_participant():
	group = create_group('Test Group', 'test.jpg', 1)
	add_participant(group.id, 2)
	remove_participant(group.id, 2)

def test_set_admin():
	group = create_group('Test Group', 'test.jpg', 1)
	set_admin(group.id, 2)
	group = create_group('Test Group', 'test.jpg', 2)
	assert group.admin_id == 2
