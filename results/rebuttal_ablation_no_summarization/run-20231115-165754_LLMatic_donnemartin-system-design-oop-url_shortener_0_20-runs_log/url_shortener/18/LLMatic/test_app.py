import pytest
from flask import Flask, request
from app import app as flask_app

@pytest.fixture
def app():
	return flask_app

@pytest.fixture
def client(app):
	return app.test_client()


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_original(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_user(client):
	response = client.post('/user/create', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User created successfully'


def test_view_user_urls(client):
	response = client.get('/user/test/urls')
	assert response.status_code == 200


def test_view_user_analytics(client):
	response = client.get('/user/test/analytics')
	assert response.status_code == 200


def test_set_url_expiration(client):
	response = client.post('/user/test/set-expiration', data={'short_url': 'test', 'expiration_date': '2022-12-31'})
	assert response.status_code == 200


def test_create_admin(client):
	response = client.post('/admin/create', data={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Admin created successfully'


def test_view_admin_urls(client):
	response = client.get('/admin/admin/urls')
	assert response.status_code == 200


def test_delete_user(client):
	response = client.post('/admin/admin/delete-user', data={'user': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User deleted successfully'

