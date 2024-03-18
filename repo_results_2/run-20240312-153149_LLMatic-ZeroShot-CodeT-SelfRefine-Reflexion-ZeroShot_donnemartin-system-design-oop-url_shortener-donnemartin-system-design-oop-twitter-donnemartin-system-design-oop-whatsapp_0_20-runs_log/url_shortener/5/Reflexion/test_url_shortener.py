import pytest
import url_shortener
from flask import json

@pytest.fixture
def client():
	url_shortener.app.config['TESTING'] = True
	with url_shortener.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert response.get_json()['clicks'] == 0
	client.get(f'/{short_url}')
	response = client.get(f'/analytics/{short_url}')
	assert response.get_json()['clicks'] == 1
