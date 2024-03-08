import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'test@example.com' in app.users


def test_login(client):
	app.users['test@example.com'] = User('Test User', 'test@example.com', 'password')
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client):
	app.users['test@example.com'] = User('Test User', 'test@example.com', 'password')
	response = client.get('/profile', query_string={'email': 'test@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password', 'storage_used': 0}


def test_upload(client):
	app.users['test@example.com'] = User('Test User', 'test@example.com', 'password')
	response = client.post('/upload', json={'name': 'file.txt', 'size': 100, 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert 'file.txt' in app.files
	assert app.users['test@example.com'].storage_used == 100


def test_download(client):
	app.files['file.txt'] = File('file.txt', 100, 'test@example.com')
	response = client.get('/download', query_string={'file_name': 'file.txt'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'file.txt', 'size': 100, 'owner': 'test@example.com', 'versions': None}
