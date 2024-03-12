import pytest
from flask import Flask
from werkzeug.exceptions import NotFound

import app
from url_shortener import set_expiration


def test_redirect_to_original():
	app.url_db = {'abc123': 'http://example.com'}
	set_expiration('abc123')

	with app.app.test_request_context():
		response = app.redirect_to_original('abc123')
		assert response.status_code == 302
		assert response.location == 'http://example.com'

	with pytest.raises(NotFound):
		app.redirect_to_original('invalid')


def test_create_short_url():
	with app.app.test_client() as client:
		response = client.post('/create_short_url', json={'url': 'http://example.com'})
		assert response.status_code == 200
		assert 'short_link' in response.get_json()

	with app.app.test_client() as client:
		response = client.post('/create_short_url', json={'url': 'invalid'})
		assert response.status_code == 400


def test_get_click_data():
	with app.app.test_client() as client:
		response = client.get('/get_click_data/abc123')
		assert response.status_code == 200


def test_create_account():
	with app.app.test_client() as client:
		response = client.post('/create_account', json={'username': 'test', 'password': 'password'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Account created successfully'}


def test_view_urls():
	with app.app.test_client() as client:
		response = client.get('/view_urls/test')
		assert response.status_code == 200


def test_add_url():
	with app.app.test_client() as client:
		response = client.post('/add_url', json={'username': 'test', 'url': 'http://example.com'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'URL added successfully'}


def test_delete_url():
	with app.app.test_client() as client:
		response = client.post('/delete_url', json={'username': 'test', 'url': 'http://example.com'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'URL removed successfully'}


def test_view_all_urls():
	with app.app.test_client() as client:
		response = client.get('/view_all_urls')
		assert response.status_code == 200


def test_delete_user():
	with app.app.test_client() as client:
		client.post('/create_account', json={'username': 'test', 'password': 'password'})
		response = client.post('/delete_user', json={'username': 'test'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Username does not exist'}


def test_view_system_performance():
	with app.app.test_client() as client:
		response = client.get('/view_system_performance')
		assert response.status_code == 200

