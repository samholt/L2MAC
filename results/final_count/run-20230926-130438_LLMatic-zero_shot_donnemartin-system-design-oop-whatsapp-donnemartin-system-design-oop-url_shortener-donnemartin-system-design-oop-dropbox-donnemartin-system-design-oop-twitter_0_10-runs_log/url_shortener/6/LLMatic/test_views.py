import pytest
from views import app, DATABASE
from models import User, URL
from datetime import datetime, timedelta


@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_admin_stats(client):
	# Register a user
	client.post('/register', json={'username': 'test', 'password': 'test'})
	# Login as the user
	client.post('/login', json={'username': 'test', 'password': 'test'})
	# Create a URL
	url = URL('https://www.google.com', 'google', 'test', datetime.now(), datetime.now() + timedelta(days=1))
	DATABASE['google'] = url
	# Click the URL
	client.get('/google')
	# Logout
	client.post('/logout')
	# Login as admin
	client.post('/login', json={'username': 'admin', 'password': 'admin'})
	# Get stats
	response = client.get('/admin/stats')
	assert response.status_code == 200
	data = response.get_json()
	assert data['total_urls'] == 1
	assert data['total_users'] == 2
	assert data['total_clicks'] == 1
	# Logout
	client.post('/logout')
	# Try to get stats as a non-admin user
	client.post('/login', json={'username': 'test', 'password': 'test'})
	response = client.get('/admin/stats')
	assert response.status_code == 401
