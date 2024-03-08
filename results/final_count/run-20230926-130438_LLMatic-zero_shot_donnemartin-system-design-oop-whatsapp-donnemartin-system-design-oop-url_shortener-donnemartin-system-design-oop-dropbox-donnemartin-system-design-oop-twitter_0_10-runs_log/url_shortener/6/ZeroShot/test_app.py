import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'shortened': 'ggl', 'user': 'test', 'expiration': '2022-12-31T23:59:59'}), content_type='application/json')
	assert response.status_code == 200
	assert b'URL shortened successfully.' in response.data

	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'shortened': 'ggl', 'user': 'test', 'expiration': '2022-12-31T23:59:59'}), content_type='application/json')
	assert response.status_code == 400
	assert b'Shortened URL already in use.' in response.data


def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302

	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert b'URL not found.' in response.data


def test_get_analytics(client):
	response = client.get('/analytics', data=json.dumps({'shortened': 'ggl'}), content_type='application/json')
	assert response.status_code == 200
	assert b'clicks' in response.data
	assert b'click_data' in response.data

	response = client.get('/analytics', data=json.dumps({'shortened': 'nonexistent'}), content_type='application/json')
	assert response.status_code == 404
	assert b'URL not found.' in response.data
