import pytest
import app
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_data():
	app.users = {'testuser': {'username': 'testuser', 'email': 'testuser@test.com', 'password': generate_password_hash('testpassword', method='sha256')}}
	app.sessions = {}


def test_register(client, init_data):
	response = client.post('/register', json={'username': 'newuser', 'email': 'newuser@test.com', 'password': 'newpassword'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client, init_data):
	response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_login_invalid(client, init_data):
	response = client.post('/login', json={'username': 'invaliduser', 'password': 'invalidpassword'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}
