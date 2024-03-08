import pytest
from services.user_service import UserService


def test_create_user():
	user_service = UserService()
	user = user_service.create_user('test', 'password')
	assert user == {'username': 'test'}

	existing_user = user_service.create_user('test', 'password')
	assert existing_user == 'Username already exists'

	urls = user_service.get_user_urls('test')
	assert urls == []

	invalid_user = user_service.get_user_urls('invalid')
	assert invalid_user == 'User not found'
