import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already registered'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}


def test_upload(client):
	response = client.post('/upload', json={'email': 'test@test.com', 'password': 'test', 'name': 'file.txt', 'size': 500})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'File uploaded successfully'}

	response = client.post('/upload', json={'email': 'test@test.com', 'password': 'test', 'name': 'file.txt', 'size': 1500})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'File size exceeds limit'}
