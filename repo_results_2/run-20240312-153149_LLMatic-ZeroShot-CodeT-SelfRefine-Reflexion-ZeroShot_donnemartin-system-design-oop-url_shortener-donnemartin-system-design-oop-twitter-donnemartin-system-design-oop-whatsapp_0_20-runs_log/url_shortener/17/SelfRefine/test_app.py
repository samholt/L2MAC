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
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl1', 'user': 'test1', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert json.loads(response.data)['data']['shortened'] == 'ggl1'

	# Test with invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'inv2', 'user': 'test2', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400

	# Test with already used shortened URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl1', 'user': 'test3', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400

def test_redirect_to_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl3', 'user': 'test4', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/ggl3')
	assert response.status_code == 302

	# Test with expired URL
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'exp4', 'user': 'test5', 'expiration': (datetime.now() - timedelta(days=1)).isoformat()})
	response = client.get('/exp4')
	assert response.status_code == 404

	# Test with non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404

def test_get_analytics(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl5', 'user': 'test6', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/analytics?user=test6')
	assert response.status_code == 200
	assert len(json.loads(response.data)['data']) == 1
