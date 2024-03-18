import pytest
import app
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.usefixtures('reset_db')
def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://google.com', 'user': 'test_user', 'expiration': datetime.now() + timedelta(days=1)})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

@pytest.mark.usefixtures('reset_db')
def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://google.com', 'user': 'test_user', 'expiration': datetime.now() + timedelta(days=1)})
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://google.com'

@pytest.mark.usefixtures('reset_db')
def test_expired_url(client):
	response = client.post('/shorten', json={'url': 'https://google.com', 'user': 'test_user', 'expiration': datetime.now() - timedelta(days=1)})
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
