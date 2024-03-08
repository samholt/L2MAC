import pytest
from app import app, db
from models import User, Post


@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

	with app.test_client() as client:
		yield client

	with app.app_context():
		db.drop_all()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']

	response = client.post('/post', json={'content': 'Hello, World!'}, headers={'Authorization': 'Bearer ' + access_token})
	assert response.status_code == 201
