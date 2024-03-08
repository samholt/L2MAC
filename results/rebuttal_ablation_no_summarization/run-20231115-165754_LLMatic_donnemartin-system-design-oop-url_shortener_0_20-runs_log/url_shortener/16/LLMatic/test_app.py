import pytest
import app
import hashlib
from datetime import datetime, timedelta

def test_create_user(client):
	# Test creating a new user
	response = client.post('/create_user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}
	assert 'test' in app.users
	assert app.users['test'] == hashlib.md5('password'.encode()).hexdigest()

	# Test creating a user with an existing username
	response = client.post('/create_user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Username already exists'}


def test_login(client):
	# Test logging in with invalid username
	response = client.post('/login', json={'username': 'invalid', 'password': 'password'})
	assert response.status_code == 401
	assert response.get_json() == {'error': 'Invalid username or password'}

	# Test logging in with invalid password
	response = client.post('/login', json={'username': 'test', 'password': 'invalid'})
	assert response.status_code == 401
	assert response.get_json() == {'error': 'Invalid username or password'}

	# Test logging in with valid username and password
	response = client.post('/login', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_manage_urls(client):
	# Test adding a new URL
	response = client.post('/test/urls', json={'short_url': 'short', 'long_url': 'long', 'expiration_date': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'URL added successfully'}
	assert 'short' in app.urls['test']
	assert app.urls['test']['short']['url'] == 'long'

	# Test updating an existing URL
	response = client.put('/test/urls', json={'short_url': 'short', 'new_long_url': 'new_long'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'URL updated successfully'}
	assert app.urls['test']['short']['url'] == 'new_long'

	# Test deleting an existing URL
	response = client.delete('/test/urls', json={'short_url': 'short'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'URL deleted successfully'}
	assert 'short' not in app.urls['test']

	# Test viewing all URLs
	response = client.get('/test/urls')
	assert response.status_code == 200
	assert response.get_json() == app.urls['test']


def test_record_access(client):
	# Create a URL for testing
	client.post('/test/urls', json={'short_url': 'short', 'long_url': 'long', 'expiration_date': (datetime.now() + timedelta(days=1)).isoformat()})

	# Test recording access for a non-existent URL
	response = client.post('/test/urls/non_existent/access', json={'location': 'USA'})
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found'}

	# Test recording access for an expired URL
	client.post('/test/urls', json={'short_url': 'expired', 'long_url': 'long', 'expiration_date': (datetime.now() - timedelta(days=1)).isoformat()})
	response = client.post('/test/urls/expired/access', json={'location': 'USA'})
	assert response.status_code == 403
	assert response.get_json() == {'error': 'URL has expired'}

	# Test recording access for an existing URL
	response = client.post('/test/urls/short/access', json={'location': 'USA'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Access recorded successfully'}
	assert len(app.urls['test']['short']['access_events']) == 1
	assert app.urls['test']['short']['access_events'][0]['location'] == 'USA'


def test_get_analytics(client):
	# Create a URL for testing
	client.post('/test/urls', json={'short_url': 'short', 'long_url': 'long', 'expiration_date': (datetime.now() + timedelta(days=1)).isoformat()})

	# Test getting analytics for a non-existent URL
	response = client.get('/test/urls/non_existent/analytics')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'URL not found'}

	# Test getting analytics for an existing URL
	response = client.get('/test/urls/short/analytics')
	assert response.status_code == 200
	assert response.get_json() == app.urls['test']['short']['access_events']


def test_admin_dashboard(client):
	# Test accessing the dashboard without admin privileges
	response = client.get('/admin/dashboard', json={'username': 'test'})
	assert response.status_code == 403
	assert response.get_json() == {'error': 'Access denied'}

	# Test accessing the dashboard with admin privileges
	response = client.get('/admin/dashboard', json={'username': 'admin'})
	assert response.status_code == 200
	assert response.get_json() == {'users': app.users, 'urls': app.urls}

	# Test deleting a user with admin privileges
	response = client.delete('/admin/dashboard', json={'username': 'admin', 'username_to_delete': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Deletion successful'}
	assert 'test' not in app.users
	assert 'test' not in app.urls

	# Test deleting a URL with admin privileges
	client.post('/admin/urls', json={'short_url': 'short', 'long_url': 'long', 'expiration_date': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.delete('/admin/dashboard', json={'username': 'admin', 'url_to_delete': 'short'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Deletion successful'}
	assert 'short' not in app.urls['admin']


def test_admin_analytics(client):
	# Test accessing the analytics without admin privileges
	response = client.get('/admin/analytics', json={'username': 'test'})
	assert response.status_code == 403
	assert response.get_json() == {'error': 'Access denied'}

	# Test accessing the analytics with admin privileges
	response = client.get('/admin/analytics', json={'username': 'admin'})
	assert response.status_code == 200
	assert 'total_urls' in response.get_json()
	assert 'most_accessed_urls' in response.get_json()

@pytest.fixture

def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client
