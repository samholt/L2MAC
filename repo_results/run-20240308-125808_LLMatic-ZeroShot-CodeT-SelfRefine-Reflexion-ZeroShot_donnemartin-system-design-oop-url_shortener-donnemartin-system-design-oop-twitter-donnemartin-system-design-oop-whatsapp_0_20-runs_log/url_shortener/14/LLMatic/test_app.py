import pytest
import app
from flask import json


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short.url' in response.get_json()['short_url']


def test_redirect_to_original(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url'].split('/')[-1]
	response = client.get('/' + short_url)
	assert response.status_code == 302


def test_create_user(client):
	response = client.post('/user/create', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'


def test_manage_urls(client):
	client.post('/user/create', data=json.dumps({'username': 'test'}), content_type='application/json')
	response = client.post('/user/test/urls', data=json.dumps({'short_url': 'test', 'original_url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['test'] == 'https://www.google.com'


def test_view_analytics(client):
	client.post('/user/create', data=json.dumps({'username': 'test'}), content_type='application/json')
	response = client.get('/user/test/analytics')
	assert response.status_code == 200


def test_admin_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200


def test_admin_users(client):
	response = client.get('/admin/users')
	assert response.status_code == 200


def test_admin_analytics(client):
	response = client.get('/admin/analytics')
	assert response.status_code == 200


@pytest.fixture

def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client
