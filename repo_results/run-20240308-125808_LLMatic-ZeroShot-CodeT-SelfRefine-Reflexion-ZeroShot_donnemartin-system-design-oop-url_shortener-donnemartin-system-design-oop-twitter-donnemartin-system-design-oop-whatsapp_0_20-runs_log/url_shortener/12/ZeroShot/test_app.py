import pytest
import app
import json
from flask import Flask
from unittest.mock import patch

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@patch('requests.get')
def test_shorten_url(mock_get, client):
	mock_get.return_value.status_code = 200
	response = client.post('/shorten', data=json.dumps({'url': 'https://google.com', 'shortened': 'goog', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	assert response.status_code == 200
	assert b'URL shortened successfully' in response.data

@patch('requests.get')
def test_shorten_url_invalid(mock_get, client):
	mock_get.return_value.status_code = 404
	response = client.post('/shorten', data=json.dumps({'url': 'https://invalidurl.com', 'shortened': 'invalid', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	assert response.status_code == 400
	assert b'Invalid URL' in response.data

@patch('requests.get')
def test_shorten_url_duplicate(mock_get, client):
	mock_get.return_value.status_code = 200
	client.post('/shorten', data=json.dumps({'url': 'https://google.com', 'shortened': 'goog', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'https://google.com', 'shortened': 'goog', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	assert response.status_code == 400
	assert b'Shortened URL already in use' in response.data

def test_redirect_url(client):
	client.post('/shorten', data=json.dumps({'url': 'https://google.com', 'shortened': 'goog', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	response = client.get('/goog')
	assert response.status_code == 302


def test_redirect_url_not_found(client):
	response = client.get('/notfound')
	assert response.status_code == 404
	assert b'URL not found' in response.data


def test_get_analytics(client):
	client.post('/shorten', data=json.dumps({'url': 'https://google.com', 'shortened': 'goog', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	response = client.get('/analytics/goog')
	assert response.status_code == 200


def test_get_analytics_not_found(client):
	response = client.get('/analytics/notfound')
	assert response.status_code == 404
	assert b'URL not found' in response.data
