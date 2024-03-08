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


def test_shorten_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	assert short_url in app.urls
	assert short_url in app.users[user_id].urls


def test_redirect_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert app.urls[short_url].clicks == 1


def test_get_analytics(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'user_id': user_id, 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	client.get(f'/{short_url}')
	response = client.get('/analytics', json={'user_id': user_id})
	assert response.status_code == 200
	analytics = json.loads(response.data)
	assert analytics[short_url]['clicks'] == 1
