import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_upload(client):
	response = client.post('/upload', json={'filename': 'test.txt', 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download', query_string={'filename': 'test.txt'})
	assert response.status_code == 200
	assert response.get_json() == {'content': 'Hello, World!'}
