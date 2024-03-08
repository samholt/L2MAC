import pytest
import auth_service

def test_signup_with_email():
	email = 'test@example.com'
	password = 'Test@1234'
	assert auth_service.sign_up(email, password) == True
	assert auth_service.sign_up(email, password) == False

def test_forgotten_password_recovery():
	email = 'test@example.com'
	assert auth_service.recover_password(email) == 'Test@1234'
	email = 'nonexistent@example.com'
	assert auth_service.recover_password(email) == False
