import pytest
from app import app, DB, URL
from datetime import datetime, timedelta
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	DB.clear()

@pytest.fixture
def sample_url():
	return URL('http://example.com', '12345678', 'test_user', [], datetime.now() + timedelta(days=1))


def test_shorten_url(client, reset_db):
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'user': 'test_user', 'expiration': '2022-12-31T23:59:59'}), content_type='application/json')
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()


def test_redirect_to_original(client, reset_db, sample_url):
	DB[sample_url.shortened] = sample_url
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 302
	assert response.location == sample_url.original
	assert len(sample_url.clicks) == 1


def test_redirect_to_expired_url(client, reset_db, sample_url):
	sample_url.expiration = datetime.now() - timedelta(days=1)
	DB[sample_url.shortened] = sample_url
	response = client.get(f'/{sample_url.shortened}')
	assert response.status_code == 404
