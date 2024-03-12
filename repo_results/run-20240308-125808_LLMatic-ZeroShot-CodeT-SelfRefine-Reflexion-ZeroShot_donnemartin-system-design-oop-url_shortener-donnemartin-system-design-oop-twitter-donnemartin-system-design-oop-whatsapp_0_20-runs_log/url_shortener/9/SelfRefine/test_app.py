import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User created successfully'


def test_get_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'


def test_invalid_url_format(client):
	response = client.post('/shorten', data=json.dumps({'url': 'not_a_url'}), content_type='application/json')
	assert response.status_code == 400
	assert 'error' in response.get_json()
	assert response.get_json()['error'] == 'Invalid URL format'
