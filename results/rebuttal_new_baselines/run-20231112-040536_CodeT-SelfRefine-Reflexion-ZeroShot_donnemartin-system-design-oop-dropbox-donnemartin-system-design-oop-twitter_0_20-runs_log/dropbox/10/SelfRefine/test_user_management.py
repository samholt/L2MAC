import pytest
import user_management

def test_register():
	data = {'name': 'Test', 'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'storage_used': 0, 'storage_remaining': 100}
	response, status_code = user_management.register(data)
	assert status_code == 201
	assert response['message'] == 'User registered successfully'
	response, status_code = user_management.register(data)
	assert status_code == 400
	assert response['message'] == 'User with this email already exists'

def test_login():
	data = {'email': 'test@test.com', 'password': 'test'}
	response, status_code = user_management.login(data)
	assert status_code == 200
	assert response['message'] == 'Login successful'

def test_forgot_password():
	data = {'email': 'test@test.com', 'new_password': 'new_test'}
	response, status_code = user_management.forgot_password(data)
	assert status_code == 200
	assert response['message'] == 'Password updated successfully'

def test_get_profile():
	response, status_code = user_management.get_profile()
	assert status_code == 200
	assert len(response) == 1

def test_update_profile():
	data = {'email': 'test@test.com', 'name': 'New Test', 'profile_picture': 'new_pic.jpg'}
	response, status_code = user_management.update_profile(data)
	assert status_code == 200
	assert response['message'] == 'Profile updated successfully'
