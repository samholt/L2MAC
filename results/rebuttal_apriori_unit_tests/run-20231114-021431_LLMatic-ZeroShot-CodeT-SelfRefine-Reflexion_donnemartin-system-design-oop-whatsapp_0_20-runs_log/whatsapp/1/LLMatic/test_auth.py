import pytest
from auth import AuthService

@pytest.fixture

def auth_service():
	service = AuthService()
	service.sign_up('test@example.com', 'Test@1234')
	service.sign_up('test2@example.com', 'Test@1234')
	return service


def test_signup_with_email(auth_service):
	email = 'test3@example.com'
	password = 'Test@1234'
	assert auth_service.sign_up(email, password) == True


def test_forgotten_password_recovery(auth_service):
	email = 'test@example.com'
	assert auth_service.recover_password(email) == 'https://recoverpassword.com/' + email
	email = 'test2@example.com'
	assert auth_service.recover_password(email) == 'https://recoverpassword.com/' + email
