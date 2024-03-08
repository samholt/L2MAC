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
	assert app.users['john@example.com'].name == 'John Doe'


def test_login(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200


def test_profile(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.get('/profile', query_string={'email': 'john@example.com'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'John Doe'


def test_upload(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/upload', json={'name': 'file1', 'size': 100, 'owner': 'john@example.com'})
	assert response.status_code == 201
	assert app.files['file1'].name == 'file1'
	assert app.users['john@example.com'].storage_used == 100


def test_download(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	app.files['file1'] = File('file1', 100, 'john@example.com')
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'file1'
