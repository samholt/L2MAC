import pytest
from flask import Flask
from app import app as flask_app
from datetime import datetime, timedelta

@pytest.fixture
def app():
	return flask_app

@pytest.fixture
def client(app):
	return app.test_client()

def test_home(client):
	response = client.get('/')
	assert response.status_code == 404

	response = client.get('/?url=nonexistent')
	assert response.status_code == 404

	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/?url={short_url}')
	assert response.status_code == 302

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration': (datetime.now() - timedelta(minutes=1)).isoformat()})
	short_url = response.get_json()['short_url']
	response = client.get(f'/?url={short_url}')
	assert response.status_code == 410


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	response = client.post('/shorten', json={'url': 'invalid_url'})
	assert response.status_code == 400

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_alias': 'google'})
	assert response.status_code == 200
	assert response.get_json()['short_url'] == 'google'

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_alias': 'google'})
	assert response.status_code == 400

def test_analytics(client):
	response = client.get('/analytics?url=nonexistent')
	assert response.status_code == 200
	assert len(response.get_json()) == 0

	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics?url={short_url}')
	assert response.status_code == 200
	assert len(response.get_json()) == 0

	response = client.get(f'/?url={short_url}')
	response = client.get(f'/analytics?url={short_url}')
	assert response.status_code == 200
	assert len(response.get_json()) == 1

def test_account(client):
	response = client.post('/account', json={'username': 'testuser'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Account created'

	response = client.get('/account?username=testuser')
	assert response.status_code == 200
	assert 'urls' in response.get_json()

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'testuser'})
	short_url = response.get_json()['short_url']
	response = client.get('/account?username=testuser')
	assert response.status_code == 200
	assert short_url in response.get_json()['urls']

	response = client.put('/account', json={'username': 'testuser', 'old_url': short_url, 'new_url': 'newurl'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'URL updated'

	response = client.get('/account?username=testuser')
	assert response.status_code == 200
	assert 'newurl' in response.get_json()['urls']

	response = client.delete('/account', json={'username': 'testuser', 'url': 'newurl'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'URL deleted'

	response = client.get('/account?username=testuser')
	assert response.status_code == 200
	assert 'newurl' not in response.get_json()['urls']

def test_admin(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()

	response = client.delete('/admin', json={'username': 'testuser'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User deleted'

	response = client.get('/admin')
	assert response.status_code == 200
	assert 'testuser' not in response.get_json()['users']

	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', json={'url': short_url})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'URL deleted'

	response = client.get('/admin')
	assert response.status_code == 200
	assert short_url not in response.get_json()['urls']

