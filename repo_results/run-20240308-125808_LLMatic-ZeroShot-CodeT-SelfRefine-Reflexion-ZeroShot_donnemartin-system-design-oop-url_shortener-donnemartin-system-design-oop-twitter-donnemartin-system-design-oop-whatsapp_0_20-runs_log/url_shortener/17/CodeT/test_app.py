import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': None}), content_type='application/json')
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': None}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': None}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/analytics/{shortened_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert 'click_data' in response.get_json()
