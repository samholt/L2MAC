import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'User registered successfully'
	
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Username already exists'


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Logged in successfully'
	
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'wrong'}), content_type='application/json')
	assert response.status_code == 400
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Invalid username or password'


def test_manage_urls(client):
	response = client.post('/urls', data=json.dumps({'username': 'test', 'url': 'http://test.com', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()
	
	short_url = response.get_json()['short_url']
	
	response = client.get('/urls', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert short_url in response.get_json()
	
	response = client.put('/urls', data=json.dumps({'username': 'test', 'short_url': short_url, 'new_url': 'http://new.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL updated successfully'
	
	response = client.delete('/urls', data=json.dumps({'username': 'test', 'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL deleted successfully'


def test_shorten(client):
	response = client.post('/shorten', data=json.dumps({'username': 'test', 'url': 'http://test.com', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect(client):
	response = client.post('/shorten', data=json.dumps({'username': 'test', 'url': 'http://test.com', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()
	
	short_url = response.get_json()['short_url']
	
	response = client.get('/' + short_url, content_type='application/json')
	assert response.status_code == 302


def test_view_user_analytics(client):
	response = client.post('/urls', data=json.dumps({'username': 'test', 'url': 'http://test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()
	
	short_url = response.get_json()['short_url']
	
	response = client.get('/analytics', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert short_url in response.get_json()


def test_admin_dashboard(client):
	response = client.get('/admin', content_type='application/json')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()
	
	response = client.delete('/admin', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'User deleted successfully'
	
	response = client.post('/urls', data=json.dumps({'username': 'test', 'url': 'http://test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()
	
	short_url = response.get_json()['short_url']
	
	response = client.delete('/admin', data=json.dumps({'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL deleted successfully'

