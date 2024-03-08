import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_profile(client):
	response = client.get('/profile?email=test@test.com')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test', 'email': 'test@test.com', 'password': 'test123', 'storage_used': 0}


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'size': 100, 'owner': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download?file_name=file1')
	assert response.status_code == 200
	assert response.get_json() == {'name': 'file1', 'size': 100, 'owner': 'test@test.com', 'versions': None}
