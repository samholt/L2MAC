import pytest
import random
import string
from group_service import GroupService

group_service = GroupService()


def test_add_remove_participants():
	user_id = random.randint(1, 100)
	group_name = f"Group {random.randint(1, 100)}"
	group_id = group_service.create_group(user_id, group_name)
	assert group_id is not None

	participant_to_add = random.randint(1, 100)
	participant_to_remove = participant_to_add
	assert group_service.add_participant(group_id, participant_to_add) == True
	assert group_service.remove_participant(group_id, participant_to_remove) == True


def test_admin_roles_permissions():
	user_id = random.randint(1, 100)
	group_name = f"Group {random.randint(1, 100)}"
	group_id = group_service.create_group(user_id, group_name)
	assert group_id is not None

	assert group_service.assign_admin(group_id, user_id) == True
	new_permissions = random.choice(["Add members", "Remove members", "Edit group info"])
	assert group_service.change_admin_permissions(group_id, user_id, new_permissions) == True
