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
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')}), content_type='application/json')
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()


def test_redirect_to_original(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics?user=test')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
