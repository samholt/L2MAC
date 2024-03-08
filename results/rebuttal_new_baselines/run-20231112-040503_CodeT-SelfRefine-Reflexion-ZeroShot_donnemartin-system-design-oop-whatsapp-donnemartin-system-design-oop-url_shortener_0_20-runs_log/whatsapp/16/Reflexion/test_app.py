import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_login(client):
	client.post('/signup', json={'name': 'Test', 'email': 'test@example.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in'}


def test_login_invalid_credentials(client):
	client.post('/signup', json={'name': 'Test', 'email': 'test@example.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}
