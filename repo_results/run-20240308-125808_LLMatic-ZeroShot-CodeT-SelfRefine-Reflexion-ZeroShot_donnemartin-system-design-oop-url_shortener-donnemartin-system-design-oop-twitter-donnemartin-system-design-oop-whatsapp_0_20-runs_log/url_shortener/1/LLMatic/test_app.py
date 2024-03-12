import pytest
from app import app
from shortener import Shortener
from user import User, users
from admin import Admin
from analytics import Analytics
from flask import Flask


def test_shorten_url():
	with app.test_client() as client:
		response = client.post('/', json={'original_url': 'http://example.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_url():
	with app.test_client() as client:
		response = client.post('/', json={'original_url': 'http://example.com'})
		short_url = response.get_json()['short_url']
		response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_create_account():
	with app.test_client() as client:
		response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Account created successfully'


def test_view_urls():
	user = User('test', 'test')
	users['test'] = user
	with app.test_client() as client:
		response = client.get('/user/test/urls')
	assert response.status_code == 200


def test_add_url():
	user = User('test', 'test')
	users['test'] = user
	with app.test_client() as client:
		response = client.post('/user/test/urls', json={'original_url': 'http://example.com', 'shortened_url': 'example'})
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL added successfully'


def test_edit_url():
	user = User('test', 'test')
	users['test'] = user
	with app.test_client() as client:
		response = client.put('/user/test/urls/example', json={'new_url': 'http://newexample.com'})
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL edited successfully'


def test_delete_url():
	user = User('test', 'test')
	users['test'] = user
	with app.test_client() as client:
		response = client.delete('/user/test/urls/example')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL deleted successfully'


def test_view_analytics():
	user = User('test', 'test')
	users['test'] = user
	with app.test_client() as client:
		response = client.get('/user/test/analytics')
	assert response.status_code == 200

