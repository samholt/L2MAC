import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'test@test.com' in app.users


def test_login(client):
	app.users['test@test.com'] = User('Test', 'test@test.com', 'test123')
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert 'file1' in app.files


def test_download(client):
	app.files['file1'] = File('file1', 'Hello, World!')
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'File downloaded successfully', 'file': 'Hello, World!'}
