import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Cleanup
	app.urls = {}
	app.users = {}

def test_shorten_url(client):
	response = client.post('/user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created'}

	expiration_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'alias': 'google', 'username': 'test', 'expiration': expiration_date})
	assert response.status_code == 201
	assert json.loads(response.data) == {'shortened_url': 'google'}

	response = client.get('/google')
	assert response.status_code == 302

	response = client.get('/analytics/google')
	assert response.status_code == 200
	assert json.loads(response.data) == {'clicks': 1, 'click_data': [{'timestamp': '2022-12-31T23:59:59'}]}

	response = client.get('/user/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'username': 'test', 'urls': ['google']}

	response = client.get('/admin')
	assert response.status_code == 200
	assert json.loads(response.data) == {'urls': ['google']}

	response = client.delete('/admin/google')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL deleted'}

	response = client.delete('/admin/user/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User deleted'}
