import pytest
import app
from flask import Flask

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert len(response.data) == 10


def test_view_statistics(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	short_url = response.data
	response = client.get(f'/statistics/{short_url}')
	assert response.status_code == 200


def test_view_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_delete_url(client):
	response = client.post('/shorten', data={'url': 'https://www.google.com'})
	short_url = response.data
	response = client.post('/admin/delete_url', data={'url': short_url})
	assert response.status_code == 200
	assert response.data == b'URL deleted'


def test_delete_user(client):
	response = client.post('/admin/delete_user', data={'username': 'test'})
	assert response.status_code == 200
	assert response.data == b'User not found'
