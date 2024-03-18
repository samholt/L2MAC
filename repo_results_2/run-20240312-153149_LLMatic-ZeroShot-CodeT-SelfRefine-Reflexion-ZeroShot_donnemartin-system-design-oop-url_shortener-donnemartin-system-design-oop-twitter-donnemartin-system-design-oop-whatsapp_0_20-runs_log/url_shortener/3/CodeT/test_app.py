import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'user_id' in json.loads(response.data)


def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'user_id' in json.loads(response.data)


def test_shorten(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten', json={'original_url': 'http://example.com', 'user_id': user_id})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)


def test_redirect_to_original(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten', json={'original_url': 'http://example.com', 'user_id': user_id})
	short_url = json.loads(response.data)['short_url']
	url_id = short_url.split('/')[-1]
	response = client.get(f'/{url_id}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten', json={'original_url': 'http://example.com', 'user_id': user_id})
	short_url = json.loads(response.data)['short_url']
	url_id = short_url.split('/')[-1]
	client.get(f'/{url_id}')
	response = client.get(f'/analytics/{url_id}')
	assert response.status_code == 200
	assert len(json.loads(response.data)['clicks']) == 1


def test_user_urls(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	client.post('/shorten', json={'original_url': 'http://example.com', 'user_id': user_id})
	response = client.get(f'/user/{user_id}')
	assert response.status_code == 200
	assert len(json.loads(response.data)['urls']) == 1
