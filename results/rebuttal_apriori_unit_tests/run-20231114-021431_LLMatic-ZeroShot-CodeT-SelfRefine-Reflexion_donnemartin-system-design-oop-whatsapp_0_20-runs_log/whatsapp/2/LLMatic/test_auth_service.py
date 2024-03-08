import pytest
from auth_service import AuthService

@pytest.fixture
def auth_service():
	return AuthService()

@pytest.fixture
def user_emails():
	return ['user1@example.com', 'user2@example.com', 'user3@example.com']

def test_signup_with_email(auth_service):
	email = 'test@example.com'
	password = 'Test@1234'
	assert auth_service.sign_up(email, password) == True

def test_forgotten_password_recovery(auth_service, user_emails):
	for email in user_emails:
		auth_service.sign_up(email, 'password')
	assert auth_service.recover_password(user_emails[0]) == True
