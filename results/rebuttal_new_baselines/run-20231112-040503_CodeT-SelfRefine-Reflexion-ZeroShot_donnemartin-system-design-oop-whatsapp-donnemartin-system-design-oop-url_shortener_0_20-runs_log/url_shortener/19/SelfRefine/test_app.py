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
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL shortened successfully'}

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Shortened URL already in use'}

	response = client.post('/shorten', json={'url': 'invalid_url', 'shortened': 'invalid', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid URL'}


def test_redirect_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/goog')
	assert response.status_code == 302

	response = client.get('/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}


def test_get_analytics(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/analytics/goog')
	assert response.status_code == 200
	assert 'clicks' in json.loads(response.data)
	assert 'click_data' in json.loads(response.data)

	response = client.get('/analytics/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}
