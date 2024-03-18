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
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'shortened': 'ggl'})
	assert response.status_code == 200
	assert json.loads(response.data)['data']['original'] == 'https://www.google.com'
	assert json.loads(response.data)['data']['shortened'] == 'ggl'

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid', 'shortened': 'inv'})
	assert response.status_code == 400
	assert json.loads(response.data)['error'] == 'Invalid URL'

	# Test duplicate shortened URL
	response = client.post('/shorten', json={'url': 'https://www.yahoo.com', 'shortened': 'ggl'})
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
