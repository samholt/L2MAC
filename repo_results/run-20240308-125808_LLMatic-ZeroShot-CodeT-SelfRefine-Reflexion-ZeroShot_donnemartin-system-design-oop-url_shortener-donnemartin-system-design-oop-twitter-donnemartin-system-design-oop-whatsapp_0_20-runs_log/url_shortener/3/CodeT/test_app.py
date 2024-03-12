import pytest
import app
from flask import Flask
from datetime import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def url():
	return {'url': 'https://www.google.com', 'shortened': 'ggl', 'expiration': datetime.now()}


def test_shorten_url(client, url):
	response = client.post('/shorten', json=url)
	assert response.status_code == 200
	assert response.get_json()['data']['original'] == url['url']
	assert response.get_json()['data']['shortened'] == url['shortened']


def test_redirect_url(client, url):
	client.post('/shorten', json=url)
	response = client.get('/' + url['shortened'])
	assert response.status_code == 302
	assert response.location == url['url']


def test_invalid_url(client, url):
	url['url'] = 'invalid'
	response = client.post('/shorten', json=url)
	assert response.status_code == 400
	assert response.get_json()['error'] == 'Invalid URL'


def test_url_not_found(client):
	response = client.get('/notfound')
	assert response.status_code == 404
	assert response.get_json()['error'] == 'URL not found'
