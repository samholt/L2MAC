import pytest
from flask import Flask, json
from app import app as flask_app, user_accounts, short_links_db


def test_shorten_url():
	response = flask_app.test_client().post('/shorten_url', json={'url': 'https://example.com'})
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'short_url' in data
	assert data['short_url'] in short_links_db


def test_analytics():
	short_url = list(short_links_db.keys())[0]
	response = flask_app.test_client().get(f'/analytics/{short_url}')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert isinstance(data, list)


def test_register():
	response = flask_app.test_client().post('/register', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'Registration successful'


def test_login():
	response = flask_app.test_client().post('/login', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'Login successful'


def test_add_url():
	response = flask_app.test_client().post('/add_url', json={'username': 'test', 'url': 'https://example.com'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'URL added successfully'


def test_get_urls():
	response = flask_app.test_client().get('/get_urls/test')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'https://example.com' in data


def test_admin_dashboard():
	response = flask_app.test_client().get('/admin/dashboard')
	data = json.loads(response.get_data(as_text=True))
	assert response.status_code == 200
	assert 'users' in data
	assert 'short_links' in data


def test_delete_url():
	user_accounts.register('test2', 'password')
	user_accounts.add_url('test2', 'url')
	response = flask_app.test_client().get('/admin/delete_url/test2/url')
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'URL deleted successfully'


def test_delete_user():
	user_accounts.register('test3', 'password')
	response = flask_app.test_client().get('/admin/delete_user/test3')
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'User deleted successfully'

