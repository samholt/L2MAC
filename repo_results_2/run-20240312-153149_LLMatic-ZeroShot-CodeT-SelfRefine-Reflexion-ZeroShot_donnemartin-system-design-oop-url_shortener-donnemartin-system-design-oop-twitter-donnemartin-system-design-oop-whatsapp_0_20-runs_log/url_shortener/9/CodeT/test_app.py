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
	assert len(user_id) == 5


def test_shorten_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	assert len(short_url) == 5


def test_redirect_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'user_id': user_id, 'expiration_date': '2022-12-31T23:59:59'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	response = client.get(f'/analytics?user_id={user_id}')
	assert response.status_code == 200
	clicks = json.loads(response.data)['clicks']
	assert clicks[short_url] == 1
