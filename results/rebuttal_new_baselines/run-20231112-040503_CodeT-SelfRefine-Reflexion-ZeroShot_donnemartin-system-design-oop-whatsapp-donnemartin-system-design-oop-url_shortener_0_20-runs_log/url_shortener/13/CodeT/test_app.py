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
	# Test valid URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	
	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'invalid', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	
	# Test duplicate shortened URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400


def test_redirect_url(client):
	# Test valid shortened URL
	response = client.get('/goog')
	assert response.status_code == 302
	
	# Test invalid shortened URL
	response = client.get('/invalid')
	assert response.status_code == 404
	
	# Test expired URL
	app.DB['expired'] = app.URL('https://www.google.com', 'expired', 0, [], datetime.now() - timedelta(days=1))
	response = client.get('/expired')
	assert response.status_code == 400
