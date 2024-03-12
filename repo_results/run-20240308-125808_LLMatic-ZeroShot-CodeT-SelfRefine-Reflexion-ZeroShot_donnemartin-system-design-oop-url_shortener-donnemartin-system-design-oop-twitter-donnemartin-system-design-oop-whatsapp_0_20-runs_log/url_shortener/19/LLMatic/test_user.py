import pytest
from user import User


def test_user_account_management():
	# Create a user object
	user = User()

	# Test account creation
	assert user.create_account('testuser', 'testpassword') == 'Account created successfully'
	assert user.create_account('testuser', 'testpassword') == 'User already exists'

	# Test retrieving user data
	user_data = user.get_user_data('testuser')
	assert user_data is not None
	assert user_data['password'] == 'testpassword'
	assert user_data['urls'] == []

	# Test updating user data
	user.update_user_data('testuser', {'password': 'newpassword', 'urls': ['testurl']})
	updated_user_data = user.get_user_data('testuser')
	assert updated_user_data['password'] == 'newpassword'
	assert updated_user_data['urls'] == ['testurl']

	# Test deleting user
	assert user.delete_user('testuser') == 'User deleted successfully'
	assert user.get_user_data('testuser') is None
