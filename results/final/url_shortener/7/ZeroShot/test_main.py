import pytest
import main
from main import app
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
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


def test_shorten_url(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://example.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://example.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	short_url = json.loads(response.data)['short_url']
	url_id = short_url.split('/')[-1]
	response = client.get(f'/{url_id}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	client.post('/shorten_url', json={'original_url': 'http://example.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	response = client.get(f'/analytics/{user_id}')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1
