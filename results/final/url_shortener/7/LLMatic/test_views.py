import pytest
from flask import Flask
from views import app


def test_redirect_url():
	client = app.test_client()
	response = client.get('/test')
	assert response.status_code == 404


def test_user_management():
	client = app.test_client()

	# Test user registration
	response = client.post('/register', data={'username': 'user1', 'password': 'password1'})
	assert response.data == b'User created successfully'

	# Test user registration with an existing username
	response = client.post('/register', data={'username': 'user1', 'password': 'password1'})
	assert response.data == b'Username already taken'

	# Test user login
	response = client.post('/login', data={'username': 'user1', 'password': 'password1'})
	assert response.data == b'Authentication successful'

	# Test user login with an invalid password
	response = client.post('/login', data={'username': 'user1', 'password': 'wrong_password'})
	assert response.data == b'Invalid username or password'

	# Test user login with a non-existent username
	response = client.post('/login', data={'username': 'non_existent_user', 'password': 'password1'})
	assert response.data == b'Invalid username or password'

	# Test retrieving a user's URLs
	response = client.post('/shorten', data={'original_url': 'https://www.google.com', 'user': 'user1'})
	short_url = response.data.decode('utf-8')
	response = client.get('/user/user1/urls')
	assert short_url in response.data.decode('utf-8')


def test_admin_features():
	client = app.test_client()

	# Test retrieving all URLs
	response = client.get('/admin/urls')
	assert response.status_code == 200
	assert 'urls' in response.data.decode('utf-8')

	# Test deleting a URL
	response = client.post('/shorten', data={'original_url': 'https://www.google.com', 'user': 'user1'})
	short_url = response.data.decode('utf-8')
	response = client.delete(f'/admin/delete_url/{short_url}')
	assert response.data == b'URL deleted successfully'

	# Test deleting a user
	response = client.delete('/admin/delete_user/user1')
	assert response.data == b'User deleted successfully'

