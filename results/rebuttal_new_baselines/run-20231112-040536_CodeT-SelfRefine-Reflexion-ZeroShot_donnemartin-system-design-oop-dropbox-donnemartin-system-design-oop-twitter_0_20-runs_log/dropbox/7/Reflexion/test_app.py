import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'john@example.com' in app.users


def test_login(client):
	app.users['john@example.com'] = User('John', 'john@example.com', 'password')
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'content': 'Hello, World!', 'owner': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert 'file1' in app.files


def test_download(client):
	app.files['file1'] = File('file1', 'Hello, World!', 'john@example.com')
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json() == {'file_content': 'Hello, World!'}
