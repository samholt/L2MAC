import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('url, user, expiration, shortened', [
	('https://www.google.com', 'user1', '2022-12-31T23:59:59', 'googl'),
	('https://www.example.com', 'user2', '2022-12-31T23:59:59', 'exmpl')
])
def test_shorten_url(client, url, user, expiration, shortened):
	response = client.post('/shorten', data=json.dumps({'url': url, 'user': user, 'expiration': expiration, 'shortened': shortened}), content_type='application/json')
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

@pytest.mark.parametrize('short_url', [
	'nonexistent'
])
def test_redirect_url_not_found(client, short_url):
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
	assert 'error' in response.get_json()

@pytest.mark.parametrize('short_url', [
	'nonexistent'
])
def test_get_analytics_not_found(client, short_url):
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 404
	assert 'error' in response.get_json()
