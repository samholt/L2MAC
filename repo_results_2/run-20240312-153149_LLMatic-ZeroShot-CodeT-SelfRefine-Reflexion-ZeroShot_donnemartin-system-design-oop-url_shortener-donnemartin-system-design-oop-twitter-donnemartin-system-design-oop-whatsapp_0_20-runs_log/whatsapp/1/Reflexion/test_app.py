import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': 1, 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': 1, 'email': 'test@test.com', 'password': 'test', 'profile_picture': None, 'status_message': None, 'privacy_settings': None, 'contacts': None, 'groups': None, 'messages': None, 'status': None}


def test_login(client):
	response = client.post('/login', json={'id': 1, 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'id': 1, 'email': 'test@test.com', 'password': 'test', 'profile_picture': None, 'status_message': None, 'privacy_settings': None, 'contacts': None, 'groups': None, 'messages': None, 'status': None}

	response = client.post('/login', json={'id': 1, 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid credentials'}
