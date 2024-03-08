import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 'test_user'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created'}


def test_delete_user(client):
	client.post('/user', json={'id': 'test_user'})
	response = client.delete('/user/test_user')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User deleted'}


def test_shorten_url(client):
	client.post('/user', json={'id': 'test_user'})
	response = client.post('/user/test_user/url', json={'url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short.ly/' in json.loads(response.data)['short_url']
