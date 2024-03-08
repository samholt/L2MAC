import pytest
import app
import utils
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	short_url = utils.generate_short_url()
	app.DB[short_url] = app.URL(original='https://www.google.com', shortened=short_url, user='test_user', clicks=[], expiration=None)
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	short_url = utils.generate_short_url()
	app.DB[short_url] = app.URL(original='https://www.google.com', shortened=short_url, user='test_user', clicks=[], expiration=None)
	response = client.get('/analytics', query_string={'user': 'test_user'})
	assert response.status_code == 200
	assert 'urls' in response.get_json()


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'urls' in response.get_json()


def test_delete_url(client):
	short_url = utils.generate_short_url()
	app.DB[short_url] = app.URL(original='https://www.google.com', shortened=short_url, user='test_user', clicks=[], expiration=None)
	response = client.delete('/admin', query_string={'url': short_url})
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert short_url not in app.DB


def test_url_expiration(client):
	short_url = utils.generate_short_url()
	app.DB[short_url] = app.URL(original='https://www.google.com', shortened=short_url, user='test_user', clicks=[], expiration=datetime.now() - timedelta(days=1))
	response = client.get(f'/{short_url}')
	assert response.status_code == 404
	assert 'error' in response.get_json()
