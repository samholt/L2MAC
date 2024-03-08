import pytest
from user import User

def test_register():
	user = User()
	response = user.register({'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response['status'] == 'success'
	assert response['message'] == 'User registered successfully'

	response = user.register({'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response['status'] == 'error'
	assert response['message'] == 'User already exists'

	response = user.register({'name': 'Test', 'email': '', 'password': 'test123'})
	assert response['status'] == 'error'
	assert response['message'] == 'Missing required fields'

	response = user.register({'name': '', 'email': 'test@test.com', 'password': ''})
	assert response['status'] == 'error'
	assert response['message'] == 'Missing required fields'

def test_login():
	user = User()
	user.register({'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})

	response = user.login({'email': 'test@test.com', 'password': 'test123'})
	assert response['status'] == 'success'
	assert response['message'] == 'User logged in successfully'

	response = user.login({'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response['status'] == 'error'
	assert response['message'] == 'Invalid credentials'

	response = user.login({'email': '', 'password': 'test123'})
	assert response['status'] == 'error'
	assert response['message'] == 'Missing required fields'

	response = user.login({'email': 'test@test.com', 'password': ''})
	assert response['status'] == 'error'
	assert response['message'] == 'Missing required fields'}
