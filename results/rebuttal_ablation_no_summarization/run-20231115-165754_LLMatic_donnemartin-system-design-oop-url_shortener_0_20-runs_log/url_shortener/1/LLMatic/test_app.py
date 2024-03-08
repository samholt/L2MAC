import pytest
import app
import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_shorten_url_invalid(client):
	response = client.post('/shorten', data=json.dumps({'url': 'invalid_url', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 400


def test_shorten_url_custom(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'custom_url': 'custom', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['short_url'] == 'custom'


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get('/analytics', query_string={'username': 'test'})
	assert response.status_code == 200
	assert short_url in response.get_json()
	assert 'clicks' in response.get_json()[short_url]
	assert 'click_details' in response.get_json()[short_url]


def test_manage_account(client):
	response = client.post('/account', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 201
	response = client.get('/account', query_string={'username': 'test'})
	assert response.status_code == 200
	assert 'test' in [url_data['username'] for url_data in response.get_json().values()]


def test_update_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.put('/account', data=json.dumps({'short_url': short_url, 'new_url': 'https://www.example.com', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	response = client.get('/account', query_string={'username': 'test'})
	assert response.get_json()[short_url]['url'] == 'https://www.example.com'


def test_delete_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete('/account', data=json.dumps({'short_url': short_url, 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	response = client.get('/account', query_string={'username': 'test'})
	assert short_url not in response.get_json()


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200


def test_admin_delete_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', data=json.dumps({'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	response = client.get('/admin')
	assert short_url not in response.get_json()['urls']


def test_admin_delete_user(client):
	response = client.post('/account', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 201
	response = client.delete('/admin', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	response = client.get('/admin')
	assert 'test' not in response.get_json()['users']


def test_url_expiration(client):
	# Test URL before expiration
	expiration_date = (datetime.now() + timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test', 'expiration_date': expiration_date}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

	# Test URL after expiration
	expiration_date = (datetime.now() - timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test', 'expiration_date': expiration_date}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 410

