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
	yield db
	db.drop_all()


def test_register(client, init_database):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_create_post(client, init_database):
	user = User(username='test', email='test@test.com', password='test')
	init_database.session.add(user)
	init_database.session.commit()
	response = client.post('/post', json={'content': 'Hello, World!'}, headers={'Authorization': f'Bearer {user.get_token()}'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}
