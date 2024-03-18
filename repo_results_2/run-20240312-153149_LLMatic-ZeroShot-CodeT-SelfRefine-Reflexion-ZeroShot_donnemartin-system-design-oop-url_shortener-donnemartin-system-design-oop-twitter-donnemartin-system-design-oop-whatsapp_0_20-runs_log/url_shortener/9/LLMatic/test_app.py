import pytest
import app
import datetime


def test_app():
	client = app.app.test_client()
	
	# Test home page
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'
	
	# Test URL shortening
	response = client.post('/shorten_url', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	
	# Test URL redirection
	response = client.get('/' + short_url)
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'
	
	# Test user creation
	response = client.post('/user', json={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User created successfully'}
	
	# Test URL management for user
	response = client.post('/user/test/urls', json={'original_url': 'https://www.example.com'})
	assert response.status_code == 404
	
	# Test analytics for user
	response = client.get('/user/test/analytics')
	assert response.status_code == 404
	
	# Test URL management for admin
	response = client.get('/admin/urls')
	assert response.status_code == 200
	response = client.delete('/admin/urls', json={'short_url': short_url})
	assert response.status_code == 200
	assert short_url not in response.get_json()
	
	# Test user deletion for admin
	response = client.delete('/admin/users/test')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User deleted'}
	
	# Test system monitoring for admin
	response = client.get('/admin/monitor')
	assert response.status_code == 404

