from services.group_service import GroupService

def test_group_service():
	group_service = GroupService()

	# Test creating a group
	group = group_service.create_group('1', 'Test Group')
	assert group == {'name': 'Test Group', 'participants': [], 'admins': []}

	# Test adding a participant
	group = group_service.add_participant('1', 'user1')
	assert group == {'name': 'Test Group', 'participants': ['user1'], 'admins': []}

	# Test removing a participant
	group = group_service.remove_participant('1', 'user1')
	assert group == {'name': 'Test Group', 'participants': [], 'admins': []}

	# Test setting an admin
	group_service.add_participant('1', 'user1')
	group = group_service.set_admin('1', 'user1')
	assert group == {'name': 'Test Group', 'participants': ['user1'], 'admins': ['user1']}
