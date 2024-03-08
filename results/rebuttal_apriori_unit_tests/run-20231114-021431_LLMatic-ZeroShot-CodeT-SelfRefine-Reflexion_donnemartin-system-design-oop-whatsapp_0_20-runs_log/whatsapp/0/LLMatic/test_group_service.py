import pytest
from group_service import GroupService

def test_group_service():
	group_service = GroupService()
	user_id = 1
	group_name = 'Test Group'
	group_id = group_service.create_group(user_id, group_name)
	assert group_id is not None

	new_group_name = 'New Test Group'
	assert group_service.edit_group(user_id, group_id, new_group_name) == True

	participant_id = 2
	assert group_service.add_participant(group_id, participant_id) == True
	assert group_service.remove_participant(group_id, participant_id) == True

	new_admin_id = 3
	group_service.add_participant(group_id, new_admin_id)
	assert group_service.assign_admin(group_id, new_admin_id) == True

	new_permissions = 'limited'
	assert group_service.change_admin_permissions(group_id, new_admin_id, new_permissions) == True
