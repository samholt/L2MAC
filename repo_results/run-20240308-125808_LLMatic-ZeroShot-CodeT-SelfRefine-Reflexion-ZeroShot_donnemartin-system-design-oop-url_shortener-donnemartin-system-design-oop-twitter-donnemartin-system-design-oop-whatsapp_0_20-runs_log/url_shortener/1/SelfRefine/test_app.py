import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com', 'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com', 'user_id': 'user1'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com', 'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.get('/analytics', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 200
	assert 'analytics' in response.get_json()


def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	assert 'user_id' in response.get_json()


def test_url_expiration(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com', 'user_id': 'user1'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	app.DB['urls'][short_url].expiration_date = datetime.now() - timedelta(days=1) # Set the URL to be expired
	response = client.get(f'/{short_url}')
	assert response.status_code == 410


def test_click_tracking(client):
	response = client.post('/create_user', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 201
	response = client.post('/shorten_url', data=json.dumps({'original_url': 'https://www.google.com', 'user_id': 'user1'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	for _ in range(5):
		client.get(f'/{short_url}')
	response = client.get('/analytics', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['analytics'][0]['clicks'] == 5
