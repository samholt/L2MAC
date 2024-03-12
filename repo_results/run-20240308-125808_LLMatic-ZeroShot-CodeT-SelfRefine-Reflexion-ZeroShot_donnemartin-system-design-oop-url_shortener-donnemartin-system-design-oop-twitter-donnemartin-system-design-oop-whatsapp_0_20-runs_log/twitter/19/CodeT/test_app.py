import pytest
from app import app, db
from models import User, Post


@pytest.fixture

def client():
	app.config['TESTING'] = True
	client = app.test_client()
	
	with app.app_context():
		db.create_all()
		yield client
		db.session.remove()
		db.drop_all()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert b'User registered successfully' in response.data


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert b'access_token' in response.data


def test_create_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	login_response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = login_response.get_json()['access_token']
	response = client.post('/post', json={'content': 'Hello, World!'}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert b'Post created successfully' in response.data
