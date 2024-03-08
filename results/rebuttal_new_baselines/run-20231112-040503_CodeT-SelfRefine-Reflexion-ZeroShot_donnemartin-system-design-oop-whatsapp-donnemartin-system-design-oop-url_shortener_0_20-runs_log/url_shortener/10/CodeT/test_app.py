import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	app.urls = {}
	app.users = {}


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com'}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']

	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'user': 'test'}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']

	response = client.get('/analytics', data=json.dumps({'url': shortened_url, 'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()


def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()


def test_get_user_urls(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'user': 'test'}), content_type='application/json')

	response = client.get('/user/urls', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
