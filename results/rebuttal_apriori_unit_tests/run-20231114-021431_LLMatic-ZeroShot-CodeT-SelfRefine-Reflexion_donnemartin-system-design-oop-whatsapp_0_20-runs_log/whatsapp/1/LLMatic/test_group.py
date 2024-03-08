import pytest
from group import GroupService

def test_group_service():
	group_service = GroupService()

	# Test creating a group
	group_id = group_service.create_group(1, 'Test Group')
	assert group_id is not None
	assert group_service.groups[group_id] == 'Test Group'
	assert group_service.group_admins[group_id] == [1]
	assert group_service.group_members[group_id] == [1]

	# Test editing a group
	assert group_service.edit_group(1, group_id, 'New Group Name') == True
	assert group_service.groups[group_id] == 'New Group Name'

	# Test adding a participant
	assert group_service.add_participant(1, group_id, 2) == True
	assert 2 in group_service.group_members[group_id]

	# Test removing a participant
	assert group_service.remove_participant(1, group_id, 2) == True
	assert 2 not in group_service.group_members[group_id]

	# Test assigning an admin
	assert group_service.assign_admin(1, group_id, 2) == True
	assert 2 in group_service.group_admins[group_id]

	# Test changing admin permissions
	assert group_service.change_admin_permissions(1, group_id, 'Add members') == True
