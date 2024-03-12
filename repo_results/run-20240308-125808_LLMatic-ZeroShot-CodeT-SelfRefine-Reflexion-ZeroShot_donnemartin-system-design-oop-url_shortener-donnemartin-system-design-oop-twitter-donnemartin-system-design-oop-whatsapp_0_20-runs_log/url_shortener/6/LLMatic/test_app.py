import pytest
from app import app


def test_home():
	response = app.test_client().get('/')
	assert response.status_code == 200


def test_shorten_url():
	response = app.test_client().post('/shorten', data={'url': 'https://www.google.com'})
	assert response.status_code == 200

	response = app.test_client().post('/shorten', data={'url': 'invalid_url'})
	assert response.status_code == 400


def test_create_user():
	response = app.test_client().post('/user/create', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

	response = app.test_client().post('/user/create', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 400


def test_create_admin():
	response = app.test_client().post('/admin/create', data={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 200

	response = app.test_client().post('/admin/create', data={'username': 'admin', 'password': 'admin'})
	assert response.status_code == 400


def test_404():
	response = app.test_client().get('/nonexistent_route')
	assert response.status_code == 404


def test_500():
	app.config['TESTING'] = False
	response = app.test_client().get('/nonexistent_route')
	assert response.status_code == 404
	app.config['TESTING'] = True
