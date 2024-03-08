import pytest
import user_management

def test_register():
	data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}
	response, status_code = user_management.register(data)
	assert status_code == 201
	assert response['message'] == 'User registered successfully'

def test_login():
	data = {'email': 'test@example.com', 'password': 'password'}
	response, status_code = user_management.login(data)
	assert status_code == 200
	assert response['message'] == 'Login successful'

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'new_password'}
	response, status_code = user_management.forgot_password(data)
	assert status_code == 200
	assert response['message'] == 'Password reset successful'

def test_profile():
	data = {'email': 'test@example.com'}
	response, status_code = user_management.profile(data)
	assert status_code == 200
	assert 'name' in response
	assert 'email' in response
	assert 'storage_used' in response
	assert 'storage_remaining' in response

def test_change_password():
	data = {'email': 'test@example.com', 'old_password': 'new_password', 'new_password': 'password'}
	response, status_code = user_management.change_password(data)
	assert status_code == 200
	assert response['message'] == 'Password changed successfully'
