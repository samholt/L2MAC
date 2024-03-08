import pytest
import user_management

def test_register():
	data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'test123'}
	response = user_management.register(data)
	assert response['status'] == 'success'
	assert response['message'] == 'User registered successfully'

def test_login():
	data = {'email': 'test@example.com', 'password': 'test123'}
	response = user_management.login(data)
	assert response['status'] == 'success'
	assert response['message'] == 'User logged in successfully'

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'newtest123'}
	response = user_management.forgot_password(data)
	assert response['status'] == 'success'
	assert response['message'] == 'Password changed successfully'

def test_profile():
	data = {'email': 'test@example.com'}
	response = user_management.profile(data)
	assert response['status'] == 'success'
	assert response['data']['name'] == 'Test User'
	assert response['data']['email'] == 'test@example.com'
	assert response['data']['password'] == 'newtest123'

def test_change_password():
	data = {'email': 'test@example.com', 'old_password': 'newtest123', 'new_password': 'finaltest123'}
	response = user_management.change_password(data)
	assert response['status'] == 'success'
	assert response['message'] == 'Password changed successfully'
