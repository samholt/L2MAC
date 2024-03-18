import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user')
	assert response.status_code == 201
	user_id = json.loads(response.data)['user_id']
	assert user_id in app.users


def test_create_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	url_data = json.loads(response.data)
	assert url_data['short_url'] in app.urls
	assert url_data['short_url'] in app.users[user_id].urls


def test_redirect_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	url_data = json.loads(response.data)
	response = client.get('/' + url_data['short_url'])
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	url_data = json.loads(response.data)
	response = client.get('/analytics/' + user_id)
	assert response.status_code == 200
	analytics_data = json.loads(response.data)
	assert url_data['id'] in analytics_data
