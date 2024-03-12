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
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	assert short_url in app.urls

def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_get_analytics(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
