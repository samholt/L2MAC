import pytest
import app
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url, shortened, user, expiration', [
	('http://example.com', 'exmpl', 'user1', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', 'goog', 'user2', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://invalid.com', 'inval', 'user3', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://example.com', 'exmpl', 'user4', (datetime.now() + timedelta(days=1)).isoformat()),
])
def test_shorten_url(client, reset_db, url, shortened, user, expiration):
	response = client.post('/shorten', json={'url': url, 'shortened': shortened, 'user': user, 'expiration': expiration})
	json_data = response.get_json()

	if 'http' not in url:
		assert response.status_code == 400
		assert 'error' in json_data
	elif shortened in app.DB:
		assert response.status_code == 400
		assert 'error' in json_data
	else:
		assert response.status_code == 200
		assert 'data' in json_data

@pytest.mark.parametrize('shortened', ['exmpl', 'goog', 'inval'])
def test_redirect_to_url(client, reset_db, shortened):
	response = client.get(f'/{shortened}')
	json_data = response.get_json()

	if shortened not in app.DB or datetime.now() > app.DB[shortened].expiration:
		assert response.status_code == 404
		assert 'error' in json_data
	else:
		assert response.status_code == 302

@pytest.mark.parametrize('user', ['user1', 'user2', 'user3'])
def test_get_analytics(client, reset_db, user):
	response = client.get(f'/analytics?user={user}')
	json_data = response.get_json()

	assert response.status_code == 200
	assert 'data' in json_data
	assert all(url['user'] == user for url in json_data['data'])
