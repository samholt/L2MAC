import pytest
from flask import Flask
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


def test_redirect_to_url(client):
	response = client.get('/random_url')
	assert response.status_code == 404


def test_get_analytics(client):
	response = client.get('/analytics/random_url')
	assert response.status_code == 404


def test_create_account(client):
	response = client.post('/account/create', data={'username': 'test_user'})
	assert response.status_code == 200


def test_view_urls(client):
	response = client.get('/account/urls', query_string={'username': 'test_user'})
	assert response.status_code == 200


def test_edit_url(client):
	response = client.put('/account/edit_url', data={'username': 'test_user', 'old_url': 'old_url', 'new_url': 'new_url'})
	assert response.status_code == 200


def test_delete_url(client):
	response = client.delete('/account/delete_url', data={'username': 'test_user', 'url': 'url'})
	assert response.status_code == 200


def test_view_analytics(client):
	response = client.get('/account/analytics', query_string={'username': 'test_user'})
	assert response.status_code == 200


def test_view_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_admin_delete_url(client):
	response = client.delete('/admin/delete_url', data={'url': 'url'})
	assert response.status_code == 200


def test_delete_user(client):
	response = client.delete('/admin/delete_user', data={'user': 'user'})
	assert response.status_code == 200


def test_monitor_system(client):
	response = client.get('/admin/monitor')
	assert response.status_code == 200
