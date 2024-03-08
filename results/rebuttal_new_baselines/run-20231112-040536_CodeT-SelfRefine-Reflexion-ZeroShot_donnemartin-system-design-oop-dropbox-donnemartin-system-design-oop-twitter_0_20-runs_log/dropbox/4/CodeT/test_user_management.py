import pytest
import user_management

def test_register():
	data = {'name': 'Test', 'email': 'test@test.com', 'password': 'test', 'storage_used': 0, 'storage_remaining': 100}
	response = user_management.register(data)
	assert response == {'message': 'User registered successfully'}


def test_login():
	data = {'email': 'test@test.com', 'password': 'test'}
	response = user_management.login(data)
	assert response == {'message': 'Login successful'}


def test_forgot_password():
	data = {'email': 'test@test.com', 'new_password': 'new_test'}
	response = user_management.forgot_password(data)
	assert response == {'message': 'Password updated successfully'}


def test_profile():
	data = {'email': 'test@test.com'}
	response = user_management.profile(data)
	assert 'name' in response
