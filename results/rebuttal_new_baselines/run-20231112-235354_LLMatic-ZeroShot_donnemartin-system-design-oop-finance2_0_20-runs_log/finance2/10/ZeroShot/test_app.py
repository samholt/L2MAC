import pytest
import app
import user
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_data():
	user.users = {}

@pytest.mark.usefixtures('init_data')
def test_create_user(client):
	response = client.post('/user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'username': 'test', 'password': 'test'}

@pytest.mark.usefixtures('init_data')
def test_get_user(client):
	client.post('/user', json={'username': 'test', 'password': 'test'})
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json() == {'username': 'test', 'password': 'test'}

@pytest.mark.usefixtures('init_data')
def test_get_user_not_found(client):
	response = client.get('/user/test')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'User not found'}
