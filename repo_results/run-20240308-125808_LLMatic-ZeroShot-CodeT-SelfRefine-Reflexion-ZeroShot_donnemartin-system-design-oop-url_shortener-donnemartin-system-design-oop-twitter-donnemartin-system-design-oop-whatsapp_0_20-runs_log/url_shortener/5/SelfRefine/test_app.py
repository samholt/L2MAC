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
def setup_data():
	app.users = {}
	app.urls = {}
	user_data = {'username': 'test', 'password': 'test'}
	url_data = {'original_url': 'https://www.google.com', 'short_url': 'test', 'username': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}
	return user_data, url_data


def test_create_user(client, setup_data):
	user_data, _ = setup_data
	response = client.post('/create_user', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'


def test_create_url(client, setup_data):
	user_data, url_data = setup_data
	client.post('/create_user', data=json.dumps(user_data), content_type='application/json')
	response = client.post('/create_url', data=json.dumps(url_data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'URL created successfully'


def test_redirect_url(client, setup_data):
	user_data, url_data = setup_data
	client.post('/create_user', data=json.dumps(user_data), content_type='application/json')
	client.post('/create_url', data=json.dumps(url_data), content_type='application/json')
	response = client.get('/' + url_data['short_url'])
	assert response.status_code == 302


def test_get_analytics(client, setup_data):
	user_data, url_data = setup_data
	client.post('/create_user', data=json.dumps(user_data), content_type='application/json')
	client.post('/create_url', data=json.dumps(url_data), content_type='application/json')
	client.get('/' + url_data['short_url'])
	response = client.get('/analytics', data=json.dumps(user_data), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()[url_data['short_url']]['clicks'] == 1
