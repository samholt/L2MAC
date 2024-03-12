import pytest
import app
from flask import url_for
from datetime import datetime, timedelta
import pytz

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return {
		'url': 'https://www.google.com',
		'user': 'test_user'
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
	assert response.location == sample_url['url']


def test_expired_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	short_url = response.get_json()['short_url']
	app.DB[short_url].expires_at = datetime.now(pytz.utc) - timedelta(days=1)
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
