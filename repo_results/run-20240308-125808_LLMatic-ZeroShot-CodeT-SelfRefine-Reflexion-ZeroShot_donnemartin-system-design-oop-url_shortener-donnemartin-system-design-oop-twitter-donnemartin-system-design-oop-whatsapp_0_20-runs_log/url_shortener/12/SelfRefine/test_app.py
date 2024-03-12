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
	# Test valid URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(minutes=10)).isoformat()})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'URL shortened successfully'

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'invalid', 'expiration': (datetime.now() + timedelta(minutes=10)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'Invalid URL'

	# Test duplicate shortened URL
	response = client.post('/shorten', json={'url': 'https://www.duckduckgo.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(minutes=10)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'Shortened URL already in use'


def test_redirect_url(client):
	# Create shortened URL
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(minutes=10)).isoformat()})

	# Test valid shortened URL
	response = client.get('/goog')
	assert response.status_code == 302

	# Test invalid shortened URL
	response = client.get('/invalid')
	assert response.status_code == 404
	assert json.loads(response.data)['error'] == 'URL not found'

	# Test expired URL
	client.post('/shorten', json={'url': 'https://www.bing.com', 'shortened': 'bing', 'expiration': (datetime.now() - timedelta(minutes=10)).isoformat()})
	response = client.get('/bing')
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'URL has expired'
