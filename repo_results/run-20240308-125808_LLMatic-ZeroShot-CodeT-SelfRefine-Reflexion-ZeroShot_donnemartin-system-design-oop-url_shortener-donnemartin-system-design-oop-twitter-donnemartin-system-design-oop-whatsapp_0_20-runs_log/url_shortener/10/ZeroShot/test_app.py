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
	assert 'user_id' in response.get_json()


def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'user_id' in response.get_json()


def test_shorten_url(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id})
	short_url = response.get_json()['short_url']
	url_id = short_url.split('/')[-1]
	response = client.get(f'/{url_id}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id})
	short_url = response.get_json()['short_url']
	url_id = short_url.split('/')[-1]
	client.get(f'/{url_id}')
	response = client.get(f'/analytics/{url_id}')
	assert response.status_code == 200
	assert len(response.get_json()['clicks']) == 1


def test_get_user_urls(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = response.get_json()['user_id']
	client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id})
	response = client.get(f'/user_urls/{user_id}')
	assert response.status_code == 200
	assert len(response.get_json()['urls']) == 1


def test_delete_url(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id})
	short_url = response.get_json()['short_url']
	url_id = short_url.split('/')[-1]
	response = client.delete(f'/delete_url/{url_id}')
	assert response.status_code == 200
	response = client.get(f'/user_urls/{user_id}')
	assert len(response.get_json()['urls']) == 0
