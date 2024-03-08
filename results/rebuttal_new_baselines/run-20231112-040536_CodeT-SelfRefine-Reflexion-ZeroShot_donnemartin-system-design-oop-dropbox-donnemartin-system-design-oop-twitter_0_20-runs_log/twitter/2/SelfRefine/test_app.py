import pytest
from app import app
from models import User, Post

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 201
	assert User.query.get('test') is not None


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_get_user(client):
	response = client.get('/users/test')
	assert response.status_code == 200


def test_update_user(client):
	response = client.put('/users/test', json={'email': 'new@example.com'})
	assert response.status_code == 200
	assert User.query.get('test').email == 'new@example.com'


def test_create_post(client):
	response = client.post('/posts', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert Post.query.get(1) is not None


def test_get_post(client):
	response = client.get('/posts/1')
	assert response.status_code == 200


def test_delete_post(client):
	response = client.delete('/posts/1')
	assert response.status_code == 200
	assert Post.query.get(1) is None
