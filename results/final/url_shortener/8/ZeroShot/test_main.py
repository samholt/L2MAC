import pytest
import main
from flask import json

@pytest.fixture
def client():
	main.app.config['TESTING'] = True
	with main.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_url(client):
	response = client.post('/shorten_url', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_register_user(client):
	response = client.post('/user/register', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
	assert response.status_code == 200
	assert response.data == b'User registered successfully'


def test_get_user_urls(client):
	response = client.post('/user/register', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
	response = client.get('/user/test_user/urls')
	assert response.status_code == 200


def test_register_admin(client):
	response = client.post('/admin/register', data=json.dumps({'admin_id': 'test_admin'}), content_type='application/json')
	assert response.status_code == 200
	assert response.data == b'Admin registered successfully'


def test_get_all_urls(client):
	response = client.post('/admin/register', data=json.dumps({'admin_id': 'test_admin'}), content_type='application/json')
	response = client.get('/admin/test_admin/urls')
	assert response.status_code == 200
