import pytest
from services.user_service import UserService


def test_register_user():
	user_service = UserService()
	new_user = user_service.register_user('Test User', 'test@example.com', 'password')
	assert new_user == {'id': 1, 'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}
	assert user_service.get_users() == {1: new_user}
