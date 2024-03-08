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
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_profile(client):
	response = client.get('/profile', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_upload(client):
	response = client.post('/upload', json={'file': {'name': 'test.txt', 'content': 'Hello, World!'}, 'user_email': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'file': {'name': 'test.txt', 'content': 'Hello, World!'}, 'user_email': 'test@example.com'}


def test_download(client):
	response = client.get('/download', json={'file_name': 'test.txt'})
	assert response.status_code == 200
	assert response.get_json() == {'file': {'name': 'test.txt', 'content': 'Hello, World!'}, 'user_email': 'test@example.com'}
