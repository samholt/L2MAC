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
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert 'data' in response.get_json()
	
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302
	
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert 'error' in response.get_json()


def test_expired_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'exp', 'expiration': (datetime.now() - timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	
	response = client.get('/exp')
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_auto_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.example.com', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	data = response.get_json().get('data')
	assert data
	assert data.get('shortened')
	
	response = client.get('/' + data.get('shortened'))
	assert response.status_code == 302
