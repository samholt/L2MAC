import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	client.get(f'/{short_url}')
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert response.get_json()['clicks'] == 1
