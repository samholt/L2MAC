import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, user_id, expires_at', [
	('http://example.com', 'user1', '2022-12-31T23:59:59'),
	('http://google.com', 'user2', '2022-12-31T23:59:59')
])
def test_shorten_url(client, url, user_id, expires_at):
	response = client.post('/shorten', data=json.dumps({'url': url, 'user_id': user_id, 'expires_at': expires_at}), content_type='application/json')
	assert response.status_code == 201
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('short_url', [
	'ABCDE',
	'12345'
])
def test_redirect_url(client, short_url):
	response = client.get(f'/{short_url}')
	assert response.status_code in [302, 404]

@pytest.mark.parametrize('user_id', [
	'user1',
	'user2'
])
def test_get_analytics(client, user_id):
	response = client.get(f'/analytics?user_id={user_id}')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
