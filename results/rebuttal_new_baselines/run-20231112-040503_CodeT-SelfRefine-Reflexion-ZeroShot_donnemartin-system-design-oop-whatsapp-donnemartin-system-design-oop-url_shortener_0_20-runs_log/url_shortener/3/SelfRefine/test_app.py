import pytest
import app
from flask import json
from datetime import datetime, timedelta
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['data']['original'] == 'https://www.google.com'
	assert data['data']['shortened'] == 'ggl'


def test_redirect_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/ggl')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_expired_url(client):
	client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(seconds=1)).isoformat()})
	time.sleep(2)
	response = client.get('/ggl')
	assert response.status_code == 404
	data = json.loads(response.data)
	assert data['error'] == 'URL has expired'
