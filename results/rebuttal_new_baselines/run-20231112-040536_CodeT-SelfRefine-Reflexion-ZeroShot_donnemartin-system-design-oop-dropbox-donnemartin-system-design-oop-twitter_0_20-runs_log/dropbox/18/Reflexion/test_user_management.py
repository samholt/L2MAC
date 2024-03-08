import pytest
from user_management import UserManagement

user_management = UserManagement()

def test_register():
	response = user_management.register({'name': 'John Doe', 'email': 'john@example.com', 'password': 'password'})
	assert response['status'] == 'success'
	assert response['message'] == 'User registered successfully'

	response = user_management.register({'name': 'John Doe', 'email': 'john@example.com', 'password': 'password'})
	assert response['status'] == 'error'
	assert response['message'] == 'Email already exists'

def test_login():
	response = user_management.login({'email': 'john@example.com', 'password': 'password'})
	assert response['status'] == 'success'
	assert response['message'] == 'User logged in successfully'

	response = user_management.login({'email': 'john@example.com', 'password': 'wrong_password'})
	assert response['status'] == 'error'
	assert response['message'] == 'Invalid email or password'}
