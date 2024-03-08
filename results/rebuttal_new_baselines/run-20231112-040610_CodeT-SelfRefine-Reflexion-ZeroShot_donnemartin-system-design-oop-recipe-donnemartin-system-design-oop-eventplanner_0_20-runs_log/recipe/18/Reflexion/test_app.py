import pytest
from app import app, User

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/user', json={'id': 1, 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1}


def test_get_user(client):
	client.post('/user', json={'id': 1, 'username': 'test', 'password': 'test'})
	response = client.get('/user/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'username': 'test'}


def test_get_user_not_found(client):
	response = client.get('/user/1')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'User not found'}
