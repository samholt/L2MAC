import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in json.loads(response.data)


def test_post(client):
	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Post created'}