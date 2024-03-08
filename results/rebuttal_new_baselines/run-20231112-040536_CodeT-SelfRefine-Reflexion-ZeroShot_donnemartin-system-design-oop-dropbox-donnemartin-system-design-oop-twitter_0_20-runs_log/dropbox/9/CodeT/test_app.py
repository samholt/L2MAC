import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'john@example.com' in app.users


def test_login(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.get('/profile', query_string={'email': 'john@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'John Doe', 'email': 'john@example.com', 'password': 'password', 'storage_used': 0}


def test_upload(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/upload', json={'name': 'file1', 'size': 100, 'owner': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert 'file1' in app.files


def test_download(client):
	app.files['file1'] = File('file1', 100, 'john@example.com')
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'file1', 'size': 100, 'owner': 'john@example.com', 'versions': []}
