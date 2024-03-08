import pytest
from app import app
from user import users_db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def clear_data():
	users_db.clear()


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'msg': 'User created'}


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_login_fail(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'msg': 'Bad username or password'}
