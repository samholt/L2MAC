import pytest
from app import app, db
from models import User, Post


@pytest.fixture

def client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as client:
		yield client


@pytest.fixture

def init_database():
	db.create_all()
	user1 = User(username='user1', email='user1@example.com', password='password')
	user2 = User(username='user2', email='user2@example.com', password='password')
	db.session.add(user1)
	db.session.add(user2)
	db.session.commit()
	yield db
	db.drop_all()


def test_register(client, init_database):
	response = client.post('/register', json={'username': 'user3', 'email': 'user3@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client, init_database):
	response = client.post('/login', json={'username': 'user1', 'password': 'password'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_post(client, init_database):
	response = client.post('/login', json={'username': 'user1', 'password': 'password'})
	access_token = response.get_json()['access_token']
	response = client.post('/post', json={'content': 'Hello, World!'}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Post created successfully'
