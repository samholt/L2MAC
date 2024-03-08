import pytest
import user_management

def test_register():
	data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}
	response = user_management.register(data)
	assert response == {'message': 'User registered successfully'}

def test_login():
	data = {'email': 'test@example.com', 'password': 'password'}
	response = user_management.login(data)
	assert response == {'message': 'Login successful'}

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'new_password'}
	response = user_management.forgot_password(data)
	assert response == {'message': 'Password reset successful'}

def test_profile():
	data = {'email': 'test@example.com'}
	response = user_management.profile(data)
	assert response == {'name': 'Test User', 'email': 'test@example.com'}

def test_change_password():
	data = {'email': 'test@example.com', 'old_password': 'new_password', 'new_password': 'password'}
	response = user_management.change_password(data)
	assert response == {'message': 'Password changed successfully'}
