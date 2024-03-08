import pytest
import app
from user import User
from file_manager import FileManager

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == User('John', 'john@example.com', 'password').to_dict()


def test_login(client):
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == User('John', 'john@example.com', 'password').to_dict()


def test_profile(client):
	response = client.get('/profile', query_string={'email': 'john@example.com'})
	assert response.status_code == 200
	assert response.get_json() == User('John', 'john@example.com', 'password').to_dict()


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'type': 'txt', 'size': 100, 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json() == FileManager('file1', 'txt', 100, 'Hello, World!').to_dict()


def test_download(client):
	response = client.get('/download', query_string={'name': 'file1'})
	assert response.status_code == 200
	assert response.get_json() == FileManager('file1', 'txt', 100, 'Hello, World!').to_dict()
