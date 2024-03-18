import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	app.urls = {}
	app.users = {}


def test_shorten_url(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'username': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_original(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'username': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}), content_type='application/json')
	short_url = response.get_json()['short_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User created successfully'


def test_get_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')

	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'


def test_get_all_urls(client):
	response = client.get('/admin')
	assert response.status_code == 200


def test_delete_url(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
	response = client.post('/shorten', data=json.dumps({'url': 'http://example.com', 'username': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}), content_type='application/json')
	short_url = response.get_json()['short_url']

	response = client.delete(f'/admin/{short_url}')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'URL deleted successfully'
