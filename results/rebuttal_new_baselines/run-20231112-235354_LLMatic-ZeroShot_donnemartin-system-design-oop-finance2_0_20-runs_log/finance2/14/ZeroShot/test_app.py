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
def new_user():
	return user.User('testuser', 'testpassword')


def test_create_user(client, new_user):
	response = client.post('/user', data=json.dumps(new_user.to_dict()), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == new_user.to_dict()


def test_get_user(client, new_user):
	user.users[new_user.username] = new_user
	response = client.get(f'/user/{new_user.username}')
	assert response.status_code == 200
	assert response.get_json() == new_user.to_dict()


def test_get_user_not_found(client):
	response = client.get('/user/nonexistentuser')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'User not found'}
