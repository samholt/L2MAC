import pytest
from app import app, db
from models import User, Post


@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_create_post(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']
	response = client.post('/post', json={'content': 'Hello, world!'}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Post created successfully'
