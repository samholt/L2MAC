import pytest
from flask import Flask
from app import app as flask_app
from datetime import datetime, timedelta

@pytest.fixture
def app():
	return flask_app

@pytest.fixture
def client(app):
	return app.test_client()

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

	response = client.post('/shorten', json={'url': 'invalid_url'})
	assert response.status_code == 400

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_alias': 'google', 'username': 'test_user'})
	assert response.status_code == 200
	assert response.get_json()['short_url'] == 'google'

	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_alias': 'google'})
	assert response.status_code == 400

	# Test URL expiration
	expiration_date = (datetime.now() + timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': expiration_date, 'username': 'test_user'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

def test_redirect_url(client):
	# Test redirection with a valid short URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 302

	# Test redirection with an invalid short URL
	response = client.get('/invalid_short_url')
	assert response.status_code == 404

	# Test redirection with an expired short URL
	expiration_date = (datetime.now() - timedelta(minutes=1)).isoformat()
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': expiration_date, 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/' + short_url)
	assert response.status_code == 400

def test_view_analytics(client):
	# Test viewing analytics with a valid short URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.get('/analytics/' + short_url)
	assert response.status_code == 200

	# Test viewing analytics with an invalid short URL
	response = client.get('/analytics/invalid_short_url')
	assert response.status_code == 404

def test_manage_account(client):
	# Test creating account
	response = client.post('/account', json={'username': 'new_test_user'})
	assert response.status_code == 200

	# Test creating account with existing username
	response = client.post('/account', json={'username': 'new_test_user'})
	assert response.status_code == 400

	# Test editing account
	response = client.put('/account', json={'username': 'new_test_user', 'new_username': 'updated_test_user'})
	assert response.status_code == 200

	# Test editing account with non-existing username
	response = client.put('/account', json={'username': 'non_existing_user', 'new_username': 'new_test_user'})
	assert response.status_code == 404

	# Test editing account with existing new username
	response = client.put('/account', json={'username': 'updated_test_user', 'new_username': 'new_test_user'})
	assert response.status_code == 200

	# Test deleting account
	response = client.delete('/account', json={'username': 'new_test_user'})
	assert response.status_code == 200

	# Test deleting account with non-existing username
	response = client.delete('/account', json={'username': 'non_existing_user'})
	assert response.status_code == 404

def test_admin_dashboard(client):
	# Test viewing all shortened URLs and users
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()

	# Test deleting a user
	response = client.delete('/admin', json={'username': 'test_user'})
	assert response.status_code == 200

	# Test deleting a non-existing user
	response = client.delete('/admin', json={'username': 'non_existing_user'})
	assert response.status_code == 404

	# Test deleting a URL
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test_user'})
	short_url = response.get_json()['short_url']
	response = client.delete('/admin', json={'short_url': short_url})
	assert response.status_code == 200

	# Test deleting a non-existing URL
	response = client.delete('/admin', json={'short_url': 'non_existing_url'})
	assert response.status_code == 404
