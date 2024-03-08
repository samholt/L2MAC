import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Logged in successfully'


def test_upload(client):
	response = client.post('/upload', json={'email': 'test@test.com', 'filename': 'test.txt', 'content': 'Hello, World!'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'File uploaded successfully'


def test_download(client):
	response = client.get('/download?filename=test.txt')
	assert response.status_code == 200
	assert json.loads(response.data)['content'] == 'Hello, World!'
