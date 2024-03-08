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
	assert response.get_json()['message'] == 'User registered successfully'
	assert isinstance(app.users['test@example.com'], User)


def test_login(client):
	app.users['test@example.com'] = User('Test User', 'test@example.com', 'password')
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'


def test_upload(client):
	response = client.post('/upload', json={'name': 'file.txt', 'type': 'text/plain', 'size': 100, 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'File uploaded successfully'
	assert isinstance(app.files['file.txt'], FileManager)


def test_download(client):
	app.files['file.txt'] = FileManager('file.txt', 'text/plain', 100, 'Hello, World!')
	response = client.get('/download', query_string={'name': 'file.txt'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'File downloaded successfully'
	assert response.get_json()['file'] == {'name': 'file.txt', 'type': 'text/plain', 'size': 100, 'content': 'Hello, World!'}
