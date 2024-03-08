import pytest
from services.user_service import UserService

user_service = UserService()

def test_authenticate_user():
	user_service.register_user('Test User', 'test@example.com', 'password')
	user = user_service.authenticate_user('test@example.com', 'password')
	assert user is not None
	assert user['email'] == 'test@example.com'
	assert user['password'] == 'password'

	invalid_user = user_service.authenticate_user('invalid@example.com', 'password')
	assert invalid_user is None

	invalid_password = user_service.authenticate_user('test@example.com', 'wrongpassword')
	assert invalid_password is None
