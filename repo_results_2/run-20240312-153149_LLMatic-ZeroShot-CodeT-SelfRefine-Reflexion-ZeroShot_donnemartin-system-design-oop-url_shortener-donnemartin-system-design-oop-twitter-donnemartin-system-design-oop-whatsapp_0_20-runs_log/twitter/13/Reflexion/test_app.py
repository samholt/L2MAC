import pytest
from app import app, db, User, Post


@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	client = app.test_client()

	with app.app_context():
		db.create_all()

	yield client

	with app.app_context():
		db.drop_all()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Registered successfully'}


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	access_token = response.get_json()['access_token']
	response = client.post('/post', json={'content': 'Hello, World!', 'user_id': '1'}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created'}
