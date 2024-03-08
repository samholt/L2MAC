import pytest
import user_management

def test_register():
	data = {'name': 'Test', 'email': 'test@example.com', 'password': 'test'}
	response, status_code = user_management.register(data)
	assert status_code == 201
	assert response['message'] == 'User registered successfully'

def test_login():
	data = {'email': 'test@example.com', 'password': 'test'}
	response, status_code = user_management.login(data)
	assert status_code == 200
	assert response['message'] == 'Login successful'

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'new_test'}
	response, status_code = user_management.forgot_password(data)
	assert status_code == 200
	assert response['message'] == 'Password updated successfully'

def test_get_profile():
	response, status_code = user_management.get_profile()
	assert status_code == 200
	assert len(response) == 1

def test_update_profile():
	data = {'email': 'test@example.com', 'name': 'New Test'}
	response, status_code = user_management.update_profile(data)
	assert status_code == 200
	assert response['message'] == 'Profile updated successfully'
