import pytest
import app
from app import User, Post

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert app.users['1'].username == 'test'


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

	response = client.post('/login', json={'id': '1', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json()['message'] == 'Invalid credentials'


def test_post(client):
	response = client.post('/post', json={'id': '1', 'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert app.posts['1'].content == 'Hello, world!'
