import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'wrong@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid credentials'}
