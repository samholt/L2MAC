import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	# Test valid URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL shortened successfully'}
	
	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'invalid', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid URL'}
	
	# Test duplicate shortened URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'goog', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Shortened URL already in use'}


def test_redirect_url(client):
	# Test valid shortened URL
	response = client.get('/goog')
	assert response.status_code == 302
	
	# Test invalid shortened URL
	response = client.get('/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}
	
	# Test expired URL
	response = client.get('/expired')
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'URL has expired'}


def test_get_analytics(client):
	# Test valid shortened URL
	response = client.get('/analytics/goog')
	assert response.status_code == 200
	assert 'clicks' in json.loads(response.data)
	assert 'click_data' in json.loads(response.data)
	
	# Test invalid shortened URL
	response = client.get('/analytics/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL not found'}
