import pytest
import app
import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup():
	app.users = {}
	app.urls = {}

@pytest.mark.usefixtures('setup')
def test_create_user(client):
	response = client.post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'

@pytest.mark.usefixtures('setup')
def test_create_url(client):
	client.post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/create_url', data=json.dumps({'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'URL created successfully'

@pytest.mark.usefixtures('setup')
def test_redirect_url(client):
	client.post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/create_url', data=json.dumps({'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.usefixtures('setup')
def test_get_analytics(client):
	client.post('/create_user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/create_url', data=json.dumps({'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['short_url']
	client.get(f'/{short_url}')
	response = client.get('/analytics', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()[short_url]['clicks'] == 1
