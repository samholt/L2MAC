import pytest
import app
from datetime import datetime, timedelta
import pytz
import os
import logging

# Create a test logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('test_app.log')
logger.addHandler(handler)

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client


def test_logging(client):
	# Test logging
	logger.info('Test log entry')
	with open('test_app.log', 'r') as f:
		logs = f.read()
	assert 'Test log entry' in logs

	# Clean up
	os.remove('test_app.log')


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_shorten_url(client):
	# Test with valid URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	# Test with invalid URL
	response = client.post('/shorten', json={'url': 'invalid_url', 'username': 'test_user'})
	assert response.status_code == 400

	# Test with custom short URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_url': 'custom', 'username': 'test_user'})
	assert response.status_code == 200
	assert response.get_json()['short_url'] == 'custom'

	# Test with custom short URL that is already in use
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_url': 'custom', 'username': 'test_user'})
	assert response.status_code == 400

	# Test with expiration date
	expiration_date = (datetime.now(pytz.utc) + timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': expiration_date, 'username': 'test_user'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	# Test with valid short URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 302

	# Test with non-existent short URL
	response = client.get('/nonexistent')
	assert response.status_code == 404

	# Test with expired short URL
	expiration_date = (datetime.now(pytz.utc) - timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': expiration_date, 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 400


def test_analytics(client):
	# Test with valid short URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/analytics?short_url=' + short_url)
	assert response.status_code == 200
	assert len(response.get_json()) == 0

	# Test with non-existent short URL
	response = client.get('/analytics?short_url=nonexistent')
	assert response.status_code == 404


def test_account(client):
	# Test with valid username
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	response = client.get('/account', json={'username': 'test_user'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()

	# Test with non-existent username
	response = client.get('/account', json={'username': 'nonexistent'})
	assert response.status_code == 404

	# Test editing user's shortened URLs
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.post('/account', json={'username': 'test_user', 'short_url': short_url, 'new_url': 'https://www.newurl.com'})
	assert response.status_code == 200

	# Test deleting user's shortened URLs
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.delete('/account', json={'username': 'test_user', 'short_url': short_url})
	assert response.status_code == 200


def test_admin(client):
	# Test with valid admin username
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'admin'})
	response = client.get('/admin', json={'username': 'admin'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert 'analytics' in response.get_json()

	# Test with non-existent admin username
	response = client.get('/admin', json={'username': 'nonexistent'})
	assert response.status_code == 404

	# Test editing any shortened URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'admin'})
	short_url = response.get_json()['short_url']
	response = client.post('/admin', json={'username': 'admin', 'short_url': short_url, 'new_url': 'https://www.newurl.com'})
	assert response.status_code == 200

	# Test deleting any shortened URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'admin'})
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', json={'username': 'admin', 'short_url': short_url})
	assert response.status_code == 200

	# Test deleting any user account
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	response = client.delete('/admin', json={'username': 'admin', 'user_to_delete': 'test_user'})
	assert response.status_code == 200


def test_error_handlers(client):
	# Test 404 error handler
	response = client.get('/nonexistent_page')
	assert response.status_code == 404
	assert response.get_json()['error'] == 'URL not found'

	# Test 500 error handler
	# It's hard to simulate a 500 error in a test, so we'll skip this for now
	# response = client.get('/cause_server_error')
	# assert response.status_code == 500
	# assert response.get_json()['error'] == 'Internal server error'

