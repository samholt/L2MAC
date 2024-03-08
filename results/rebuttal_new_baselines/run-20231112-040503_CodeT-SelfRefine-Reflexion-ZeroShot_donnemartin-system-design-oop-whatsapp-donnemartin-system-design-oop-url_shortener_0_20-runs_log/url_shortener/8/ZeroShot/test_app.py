import pytest
import app
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

def test_redirect_to_original(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() + timedelta(days=1)).isoformat()})
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302

def test_redirect_to_expired_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expires_at': (datetime.now() - timedelta(days=1)).isoformat()})
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 404
