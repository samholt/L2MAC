import pytest
import app
from flask import url_for
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_url():
	return {
		'original': 'https://www.google.com',
		'user': 'test_user',
		'expires_at': (datetime.now() + timedelta(days=1)).isoformat()
	}


def test_shorten_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 201
	assert 'shortened' in response.get_json()


def test_redirect_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	shortened = response.get_json()['shortened']
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert response.location == sample_url['original']


def test_expired_url(client, sample_url):
	sample_url['expires_at'] = (datetime.now() - timedelta(days=1)).isoformat()
	response = client.post('/shorten', json=sample_url)
	shortened = response.get_json()['shortened']
	response = client.get(f'/{shortened}')
	assert response.status_code == 404


def test_existing_url(client, sample_url):
	response = client.post('/shorten', json=sample_url)
	shortened = response.get_json()['shortened']
	response = client.post('/shorten', json=sample_url)
	assert response.status_code == 200
	assert response.get_json()['shortened'] == shortened
