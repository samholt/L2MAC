import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url, short, user, expiration', [
	('http://example.com', 'exmpl', 'user1', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', 'goog', 'user2', (datetime.now() + timedelta(days=1)).isoformat())
])
def test_shorten_url(client, reset_db, url, short, user, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'short': short, 'user': user, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['short_url'] == short

	# Test duplicate short URL
	response = client.post('/shorten', data=json.dumps({'url': url, 'short': short, 'user': user, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 400

	# Test invalid URL
	response = client.post('/shorten', data=json.dumps({'url': 'invalid', 'short': 'inv', 'user': user, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 400

@pytest.mark.parametrize('short, user', [
	('exmpl', 'user1'),
	('goog', 'user2')
])
def test_redirect_url(client, reset_db, short, user):
	# Shorten URL first
	client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'short': short, 'user': user, 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')

	response = client.get(f'/{short}')
	assert response.status_code == 302

	# Test expired URL
	client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'short': 'exp', 'user': user, 'expiration': (datetime.now() - timedelta(days=1)).isoformat()}), content_type='application/json')
	response = client.get('/exp')
	assert response.status_code == 404

	# Test non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404

@pytest.mark.parametrize('user', [
	'user1',
	'user2'
])
def test_get_analytics(client, reset_db, user):
	# Shorten URLs first
	client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'short': 'exmpl', 'user': user, 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')
	client.post('/shorten', data=json.dumps({'url': 'http://google.com', 'short': 'goog', 'user': user, 'expiration': (datetime.now() + timedelta(days=1)).isoformat()}), content_type='application/json')

	response = client.get('/analytics', data=json.dumps({'user': user}), content_type='application/json')
	assert response.status_code == 200
	assert len(response.get_json()) == 2
