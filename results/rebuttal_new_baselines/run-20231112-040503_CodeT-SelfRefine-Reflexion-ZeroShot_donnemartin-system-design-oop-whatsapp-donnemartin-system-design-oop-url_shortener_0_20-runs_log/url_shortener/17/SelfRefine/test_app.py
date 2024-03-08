import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return {
		'url': 'https://www.google.com',
		'user_id': 'user1',
		'expires_at': (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
	}


def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_redirect_url_not_found_or_expired(client):
	response = client.get('/invalid_url')
	assert response.status_code == 404
	assert 'error' in response.get_json()


def test_shorten_url_without_url(client, sample_url):
	del sample_url['url']
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_shorten_url_without_user_id(client, sample_url):
	del sample_url['user_id']
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 400
	assert 'error' in response.get_json()
