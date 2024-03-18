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
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert json.loads(response.data)['data']['original'] == 'https://www.google.com'
	assert json.loads(response.data)['data']['shortened'] == 'ggl'

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'inv', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'Invalid URL'

	# Test duplicate shortened URL
	response = client.post('/shorten', json={'url': 'https://www.duckduckgo.com', 'shortened': 'ggl', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'Shortened URL already in use'


def test_redirect_url(client):
	# Test valid shortened URL
	response = client.get('/ggl')
	assert response.status_code == 302

	# Test invalid shortened URL
	response = client.get('/inv')
	assert response.status_code == 404
	assert json.loads(response.data)['error'] == 'URL not found'

	# Test expired shortened URL
	response = client.post('/shorten', json={'url': 'https://www.bing.com', 'shortened': 'bng', 'expiration': (datetime.now() - timedelta(minutes=1)).isoformat()})
	response = client.get('/bng')
	assert response.status_code == 404
	assert json.loads(response.data)['error'] == 'URL not found'

	# Test click data
	response = client.get('/ggl')
	assert response.status_code == 302
	response = client.get('/ggl')
	assert response.status_code == 302
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl2', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	response = client.get('/ggl2')
	assert response.status_code == 302
	assert app.DB['ggl'].clicks == 2
	assert app.DB['ggl2'].clicks == 1
