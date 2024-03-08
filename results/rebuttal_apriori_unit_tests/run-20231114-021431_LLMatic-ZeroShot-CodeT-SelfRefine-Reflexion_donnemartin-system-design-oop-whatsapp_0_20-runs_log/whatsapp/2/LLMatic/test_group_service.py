import pytest
from group_service import GroupService

@pytest.fixture
def group_service():
	return GroupService()

@pytest.fixture
def group_id(group_service):
	return group_service.create_group(1, 'Test Group', '/path/to/group_picture.jpg')

@pytest.fixture
def user_ids():
	return list(range(2, 11))  # 10 users

def test_create_group(group_service):
	group_id = group_service.create_group(1, 'Test Group', '/path/to/group_picture.jpg')
	assert group_id is not None

def test_add_remove_participants(group_service, group_id, user_ids):
	participant_to_add = user_ids[0]
	participant_to_remove = user_ids[1]
	group_service.add_participant(group_id, participant_to_add)
	group_service.add_participant(group_id, participant_to_remove)
	assert group_service.remove_participant(group_id, participant_to_remove) == True

def test_admin_roles_permissions(group_service, group_id, user_ids):
	user_id = user_ids[0]
	group_service.add_participant(group_id, user_id)
	assert group_service.assign_admin(group_id, user_id) == True
	assert group_service.change_admin_permissions(group_id, user_id, 'Add members') == True
