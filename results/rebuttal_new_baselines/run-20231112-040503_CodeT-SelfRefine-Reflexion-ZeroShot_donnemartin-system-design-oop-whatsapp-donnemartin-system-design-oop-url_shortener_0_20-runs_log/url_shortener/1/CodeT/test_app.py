import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	user_id = json.loads(response.data)['user_id']
	assert user_id in app.users


def test_create_url(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 201
	url_id = json.loads(response.data)['url_id']
	assert url_id in app.urls


def test_redirect_url(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	url_id = json.loads(response.data)['url_id']
	response = client.get('/goog')
	assert response.status_code == 302
	assert app.urls[url_id].clicks == 1


def test_get_user_urls(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	url_id = json.loads(response.data)['url_id']
	response = client.get(f'/user/{user_id}/urls')
	assert response.status_code == 200
	assert json.loads(response.data) == {url_id: 'https://www.google.com'}


def test_delete_url(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	url_id = json.loads(response.data)['url_id']
	response = client.delete(f'/user/{user_id}/url/{url_id}')
	assert response.status_code == 204
	assert url_id not in app.urls
	assert url_id not in app.users[user_id].urls
