import pytest
import app
from user import User
from post import Post

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', '_password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test'}


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', '_password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'test'}


def test_create_post(client):
	client.post('/register', json={'email': 'test@test.com', 'username': 'test', '_password': 'test'})
	response = client.post('/post', json={'user_email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert data['user_email'] == 'test@test.com'
	assert data['content'] == 'Hello, world!'