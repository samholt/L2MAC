import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'shortened_url' in json.loads(response.data)


def test_redirect_to_original(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	shortened_url = json.loads(response.data)['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_get_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	shortened_url = json.loads(response.data)['shortened_url']
	response = client.get(f'/analytics/{shortened_url}')
	assert response.status_code == 200
	assert json.loads(response.data)['clicks'] == 0
	client.get(f'/{shortened_url}')
	response = client.get(f'/analytics/{shortened_url}')
	assert json.loads(response.data)['clicks'] == 1
