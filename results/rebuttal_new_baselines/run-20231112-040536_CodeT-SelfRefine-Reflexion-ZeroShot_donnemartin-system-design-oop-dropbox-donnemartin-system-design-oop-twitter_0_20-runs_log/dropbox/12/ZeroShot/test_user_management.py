import pytest
import user_management

def test_register():
	data = {'name': 'Test', 'email': 'test@test.com', 'password': 'test', 'storage_used': 0, 'storage_remaining': 100}
	response = user_management.register(data)
	assert response['status'] == 'success'

def test_login():
	data = {'email': 'test@test.com', 'password': 'test'}
	response = user_management.login(data)
	assert response['status'] == 'success'

def test_forgot_password():
	data = {'email': 'test@test.com', 'new_password': 'new_test'}
	response = user_management.forgot_password(data)
	assert response['status'] == 'success'

def test_profile():
	data = {'email': 'test@test.com'}
	response = user_management.profile(data)
	assert response['status'] == 'success'

def test_change_password():
	data = {'email': 'test@test.com', 'old_password': 'new_test', 'new_password': 'test'}
	response = user_management.change_password(data)
	assert response['status'] == 'success'
