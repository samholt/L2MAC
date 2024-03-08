import pytest
import app
import uuid
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Clear DB after each test
	app.DB.clear()


def test_shorten_url(client):
	# Test valid URL
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	# Test invalid URL
	response = client.post('/shorten', json={'original_url': 'invalid_url'})
	assert response.status_code == 400
	assert 'error' in response.get_json()

	# Test custom URL
	custom_url = str(uuid.uuid4())[:8]
	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'custom_url': custom_url})
	assert response.status_code == 200
	assert response.get_json()['short_url'] == custom_url

	# Test duplicate custom URL
	response = client.post('/shorten', json={'original_url': 'https://www.google.com', 'custom_url': custom_url})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_redirect_url(client):
	# Test non-existent URL
	response = client.get('/non_existent_url')
	assert response.status_code == 404
	assert 'error' in response.get_json()

	# Test valid URL
	response = client.post('/shorten', json={'original_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 302


def test_get_analytics(client):
	# Test without user ID
	response = client.get('/analytics')
	assert response.status_code == 400
	assert 'error' in response.get_json()

	# Test with user ID
	user_id = str(uuid.uuid4())
	client.post('/shorten', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	response = client.get('/analytics', query_string={'user_id': user_id})
	assert response.status_code == 200
	assert len(response.get_json()) == 1
