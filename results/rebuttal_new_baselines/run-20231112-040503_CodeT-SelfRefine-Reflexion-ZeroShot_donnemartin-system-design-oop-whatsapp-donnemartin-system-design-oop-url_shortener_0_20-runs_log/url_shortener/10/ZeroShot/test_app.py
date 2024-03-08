import pytest
import app
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def url():
	return {
		'url': 'https://www.google.com',
		'user': 'test_user',
		'expiration': (datetime.now() + timedelta(days=1)).isoformat()
	}

@pytest.fixture
def short_url(client, url):
	response = client.post('/shorten', json=url)
	return response.get_json()['shortened_url']


def test_shorten_url(client, url):
	response = client.post('/shorten', json=url)
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()


def test_redirect_url(client, short_url):
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_expired_url(client, url):
	url['expiration'] = (datetime.now() - timedelta(days=1)).isoformat()
	response = client.post('/shorten', json=url)
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
