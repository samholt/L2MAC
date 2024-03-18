import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expires_at': '2022-12-31T23:59:59'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expires_at': '2022-12-31T23:59:59'}), content_type='application/json')
	short_url = response.get_json().get('short_url')
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json().get('message') == 'User created successfully'


def test_get_user_urls(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expires_at': '2022-12-31T23:59:59'}), content_type='application/json')
	short_url = response.get_json().get('short_url')
	response = client.get('/user/test/urls')
	assert response.status_code == 200
	assert short_url in response.get_json().get('urls')
