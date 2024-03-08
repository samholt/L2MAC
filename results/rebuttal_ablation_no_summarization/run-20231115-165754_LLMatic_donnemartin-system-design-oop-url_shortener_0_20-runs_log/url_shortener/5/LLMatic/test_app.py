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


def test_custom_short_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'custom_short_url': 'custom', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['short_url'] == 'custom'


def test_invalid_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'invalid', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 400


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	# Check analytics
	response = client.get('/analytics')
	assert response.status_code == 200
	analytics = response.get_json()
	assert short_url in analytics
	assert analytics[short_url]['clicks'] == 1
	assert 'timestamp' in analytics[short_url]['click_details'][0]
	assert analytics[short_url]['click_details'][0]['location'] == 'Dummy Location'


def test_expired_url(client):
	expiration_date = (datetime.now() - timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test', 'expiration_date': expiration_date}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 410


def test_view_analytics(client):
	response = client.get('/analytics')
	assert response.status_code == 200


def test_manage_account(client):
	response = client.post('/account', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 201
	response = client.get('/account', query_string={'username': 'test'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()

	# Test updating a URL
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.put('/account', data=json.dumps({'username': 'test', 'short_url': short_url, 'new_url': 'https://www.example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE['urls'][short_url]['original_url'] == 'https://www.example.com'

	# Test deleting a URL
	response = client.delete('/account', data=json.dumps({'username': 'test', 'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert short_url not in app.DATABASE['users']['test']['urls']
	assert short_url not in app.DATABASE['urls']

	# Test analytics
	response = client.get('/account', query_string={'username': 'test'})
	assert response.status_code == 200
	assert 'analytics' in response.get_json()
	assert short_url not in response.get_json()['analytics']


def test_manage_admin(client):
	# Test viewing admin dashboard
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()

	# Test deleting a user
	response = client.post('/account', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 201
	response = client.delete('/admin', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'test' not in app.DATABASE['users']

	# Test deleting a URL
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', data=json.dumps({'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert short_url not in app.DATABASE['urls']
	assert short_url not in app.DATABASE['analytics']

