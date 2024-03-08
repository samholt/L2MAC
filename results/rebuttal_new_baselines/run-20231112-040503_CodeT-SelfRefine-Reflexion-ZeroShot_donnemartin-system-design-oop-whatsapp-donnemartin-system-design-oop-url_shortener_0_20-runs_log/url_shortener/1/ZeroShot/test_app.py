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
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test_user', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

def test_redirect_to_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test_user', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

	response = client.get(f'/{short_url}')
	assert response.status_code == 404
