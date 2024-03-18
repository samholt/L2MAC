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

@pytest.mark.parametrize('url, shortened, user, expiration', [
	('http://example.com', 'exmpl', 'user1', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', 'goog', 'user2', (datetime.now() + timedelta(days=1)).isoformat()),
])
def test_shorten_url(client, reset_db, url, shortened, user, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'user': user, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 200
	assert app.DB[shortened].original == url

@pytest.mark.parametrize('shortened', ['exmpl', 'goog'])
def test_redirect_to_url(client, reset_db, shortened):
	app.DB[shortened] = app.URL('http://example.com', shortened, 'user1', [], datetime.now() + timedelta(days=1))
	response = client.get(f'/{shortened}')
	assert response.status_code == 302

@pytest.mark.parametrize('user', ['user1', 'user2'])
def test_get_analytics(client, reset_db, user):
	app.DB['exmpl'] = app.URL('http://example.com', 'exmpl', user, [], datetime.now() + timedelta(days=1))
	app.DB['goog'] = app.URL('http://google.com', 'goog', user, [], datetime.now() + timedelta(days=1))
	response = client.get(f'/analytics?user={user}')
	assert response.status_code == 200
	assert len(response.get_json()['data']) == 2
