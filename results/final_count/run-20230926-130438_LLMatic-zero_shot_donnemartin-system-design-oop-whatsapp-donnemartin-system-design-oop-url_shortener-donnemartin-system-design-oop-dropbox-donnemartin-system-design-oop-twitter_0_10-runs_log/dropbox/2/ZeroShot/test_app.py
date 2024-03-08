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


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client):
	response = client.get('/profile', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert 'name' in response.get_json()
	assert 'email' in response.get_json()
	assert 'storage_used' in response.get_json()


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'size': 100, 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download', json={'name': 'file1'})
	assert response.status_code == 200
	assert 'file' in response.get_json()
	assert 'message' in response.get_json()
