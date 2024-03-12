import pytest
import app
from flask import Flask
from datetime import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': datetime.now()})
	assert response.status_code == 200
	assert 'data' in response.get_json()
	
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': datetime.now()})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_redirect_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': datetime.now()})
	response = client.get('/ggl')
	assert response.status_code == 302
	
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert 'error' in response.get_json()
