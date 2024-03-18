import pytest
import app
import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup():
	app.users = {}
	app.urls = {}

@pytest.mark.parametrize('username, password, status_code', [
	('user1', 'pass1', 200),
	('user1', 'pass2', 200),
	('user2', 'pass2', 200),
])
def test_register(client, setup, username, password, status_code):
	response = client.post('/register', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
	assert response.status_code == status_code

@pytest.mark.parametrize('username, password, status_code', [
	('user1', 'pass1', 200),
	('user1', 'pass2', 400),
	('user2', 'pass2', 400),
])
def test_login(client, setup, username, password, status_code):
	app.users[username] = app.User(username, 'pass1', {})
	response = client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
	assert response.status_code == status_code

@pytest.mark.parametrize('original_url, short_url, username, expiration, status_code', [
	('https://www.google.com', 'goog', 'user1', None, 200),
	('https://www.google.com', 'goog', 'user1', None, 400),
	('https://www.google.com', 'goog2', 'user2', None, 400),
	('https://www.google.com', 'goog2', 'user1', (datetime.now() + timedelta(days=1)).isoformat(), 200),
])
def test_shorten(client, setup, original_url, short_url, username, expiration, status_code):
	app.users[username] = app.User(username, 'pass1', {})
	response = client.post('/shorten', data=json.dumps({'original_url': original_url, 'short_url': short_url, 'username': username, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == status_code

@pytest.mark.parametrize('short_url, status_code', [
	('goog', 302),
	('goog2', 410),
	('goog3', 404),
])
def test_redirect_to_original(client, setup, short_url, status_code):
	app.users['user1'] = app.User('user1', 'pass1', {})
	app.urls['goog'] = app.URL('https://www.google.com', 'goog', 'user1', [], None)
	app.urls['goog2'] = app.URL('https://www.google.com', 'goog2', 'user1', [], (datetime.now() - timedelta(days=1)))
	response = client.get('/' + short_url)
	assert response.status_code == status_code

@pytest.mark.parametrize('username, status_code', [
	('user1', 200),
	('user2', 400),
])
def test_analytics(client, setup, username, status_code):
	app.users['user1'] = app.User('user1', 'pass1', {})
	app.urls['goog'] = app.URL('https://www.google.com', 'goog', 'user1', [], None)
	app.users['user1'].urls['goog'] = app.urls['goog']
	response = client.get('/analytics?username=' + username)
	assert response.status_code == status_code

