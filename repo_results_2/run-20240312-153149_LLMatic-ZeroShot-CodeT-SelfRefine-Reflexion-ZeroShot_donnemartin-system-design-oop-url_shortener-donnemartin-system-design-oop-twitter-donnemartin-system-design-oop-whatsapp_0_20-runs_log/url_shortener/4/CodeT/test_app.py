import pytest
import app
import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Cleanup
	app.urls = {}
	app.users = {}


def test_shorten_url(client):
	# Test invalid URL
	response = client.post('/shorten', data=json.dumps({'url': 'invalid'}), content_type='application/json')
	assert response.status_code == 400

	# Test valid URL
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com'}), content_type='application/json')
	assert response.status_code == 200
	short_url = response.get_json()['short_url']
	assert short_url in app.urls


def test_redirect_url(client):
	# Test non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404

	# Test existent URL
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 302


def test_get_analytics(client):
	# Test non-existent user
	response = client.get('/analytics', data=json.dumps({'user': 'nonexistent'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['urls'] == []

	# Test existent user
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'user': 'test'}), content_type='application/json')
	response = client.get('/analytics', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert len(response.get_json()['urls']) == 1


def test_create_user(client):
	# Test creating user
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'test' in app.users


def test_get_user(client):
	# Test non-existent user
	response = client.get('/user', data=json.dumps({'username': 'nonexistent'}), content_type='application/json')
	assert response.status_code == 404

	# Test existent user
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.get('/user', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200


def test_get_admin(client):
	# Test getting all data
	response = client.get('/admin')
	assert response.status_code == 200


def test_delete_admin(client):
	# Test deleting URL
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', data=json.dumps({'url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert short_url not in app.urls

	# Test deleting user
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.delete('/admin', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'test' not in app.users
