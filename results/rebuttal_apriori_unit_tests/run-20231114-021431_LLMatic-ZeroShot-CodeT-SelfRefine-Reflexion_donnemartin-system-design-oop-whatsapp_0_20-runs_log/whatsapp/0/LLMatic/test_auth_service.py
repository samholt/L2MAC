import pytest
from auth_service import AuthService

@pytest.fixture
def auth_service():
	service = AuthService()
	service.sign_up('user1@example.com', 'password1')
	service.sign_up('user2@example.com', 'password2')
	service.sign_up('user3@example.com', 'password3')
	return service

@pytest.fixture
def user_emails():
	return ['user1@example.com', 'user2@example.com', 'user3@example.com']

def test_signup_with_email(auth_service):
	email = 'test@example.com'
	password = 'Test@1234'
	assert auth_service.sign_up(email, password) == True

def test_forgotten_password_recovery(auth_service, user_emails):
	email = 'user1@example.com'
	assert auth_service.recover_password(email) == True
