import pytest
from users import UserManager


def test_user_creation():
	user_manager = UserManager()
	assert user_manager.create_user(1, 'John Doe', 'john.doe@example.com') == 'User created successfully'
	assert user_manager.create_user(1, 'John Doe', 'john.doe@example.com') == 'User already exists'


def test_user_retrieval():
	user_manager = UserManager()
	user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	user = user_manager.get_user(1)
	assert user.name == 'John Doe'
	assert user.email == 'john.doe@example.com'


def test_user_update():
	user_manager = UserManager()
	user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	assert user_manager.update_user(1, 'Jane Doe', 'jane.doe@example.com') == 'User updated successfully'
	user = user_manager.get_user(1)
	assert user.name == 'Jane Doe'
	assert user.email == 'jane.doe@example.com'


def test_user_deletion():
	user_manager = UserManager()
	user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	assert user_manager.delete_user(1) == 'User deleted successfully'
	assert user_manager.get_user(1) == 'User does not exist'


def test_user_following():
	user_manager = UserManager()
	user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	user_manager.create_user(2, 'Jane Doe', 'jane.doe@example.com')
	assert user_manager.follow_user(1, 2) == 'User followed successfully'
	assert user_manager.follow_user(1, 2) == 'User already followed'


def test_user_feed():
	user_manager = UserManager()
	user_manager.create_user(1, 'John Doe', 'john.doe@example.com')
	assert user_manager.view_user_feed(1) == []
