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
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()


def test_redirect_url(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test'}), content_type='application/json')
	shortened_url = list(app.urls.keys())[0]
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test'}), content_type='application/json')
	response = client.get('/analytics', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert len(response.get_json()) == 1


def test_create_user(client):
	response = client.post('/users', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()


def test_get_user_urls(client):
	client.post('/users', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.get('/users/test/urls')
	assert response.status_code == 200


def test_get_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_get_all_users(client):
	response = client.get('/admin/users')
	assert response.status_code == 200


def test_delete_user(client):
	client.post('/users', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.delete('/admin/users/test')
	assert response.status_code == 200
	assert 'message' in response.get_json()


def test_delete_url(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test'}), content_type='application/json')
	shortened_url = list(app.urls.keys())[0]
	response = client.delete(f'/admin/urls/{shortened_url}')
	assert response.status_code == 200
	assert 'message' in response.get_json()
