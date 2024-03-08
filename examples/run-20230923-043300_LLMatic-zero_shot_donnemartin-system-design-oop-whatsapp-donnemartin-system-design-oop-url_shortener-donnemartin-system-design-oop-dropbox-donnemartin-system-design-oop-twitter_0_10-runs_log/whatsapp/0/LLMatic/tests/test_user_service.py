import pytest
from services.user_service import UserService

def test_user_service():
	user_service = UserService()

	# Test creating a group
	group = user_service.create_group('Test Group', 'test.jpg', [1, 2], [1])
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'
	assert group.participants == [1, 2]
	assert group.admins == [1]

	# Test editing a group
	group = user_service.edit_group('Test Group', name='New Test Group', picture='new_test.jpg', participants=[1, 2, 3], admins=[1, 2])
	assert group.name == 'New Test Group'
	assert group.picture == 'new_test.jpg'
	assert group.participants == [1, 2, 3]
	assert group.admins == [1, 2]

	# Test getting online status
	assert user_service.get_online_status(1) == True
