import pytest
import app
import json
from datetime import datetime, timedelta

@pytest.fixture
# This fixture sets up a test client for the Flask application.
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# This test checks the URL shortening functionality.
def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 200

# This test checks the URL validation.
def test_invalid_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'invalid_url', 'username': 'test'}), content_type='application/json')
	assert response.status_code == 400

# This test checks the URL expiration functionality.
def test_url_expiration(client):
	# Test URL that has not expired
	expiration_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test', 'expiration_date': expiration_date}), content_type='application/json')
	short_url = json.loads(response.data)['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 302

	# Test URL that has expired
	expiration_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'username': 'test', 'expiration_date': expiration_date}), content_type='application/json')
	short_url = json.loads(response.data)['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 400
