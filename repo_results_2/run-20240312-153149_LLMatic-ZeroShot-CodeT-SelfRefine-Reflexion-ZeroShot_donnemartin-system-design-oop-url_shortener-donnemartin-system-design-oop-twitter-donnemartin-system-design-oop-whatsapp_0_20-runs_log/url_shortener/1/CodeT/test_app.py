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
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = list(app.urls.keys())[0]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test'}), content_type='application/json')
	response = client.get('/analytics', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert len(response.get_json()) == 1


def test_register_user(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()


def test_admin_dashboard(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	response = client.get('/admin')
	assert response.status_code == 200
	assert len(response.get_json()) == 1


def test_delete_url(client):
	client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = list(app.urls.keys())[0]
	response = client.delete('/delete', data=json.dumps({'short_url': short_url}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
