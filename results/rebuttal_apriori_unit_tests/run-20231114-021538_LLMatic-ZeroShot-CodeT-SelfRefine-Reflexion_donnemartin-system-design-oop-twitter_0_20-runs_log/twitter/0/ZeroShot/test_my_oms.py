import pytest
import random
import string
from my_oms import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.mark.parametrize('path', ['/register', '/login', '/post', '/posts'])

def test_endpoints(client, path):
	response = client.get(path)
	assert response.status_code != 404


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert b'Registered successfully' in response.data


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert b'token' in response.data


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/post', json={'email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert b'Posted successfully' in response.data


def test_get_posts(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	client.post('/post', json={'email': 'test@test.com', 'content': 'Hello, world!'})
	response = client.get('/posts', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert b'Hello, world!' in response.data
