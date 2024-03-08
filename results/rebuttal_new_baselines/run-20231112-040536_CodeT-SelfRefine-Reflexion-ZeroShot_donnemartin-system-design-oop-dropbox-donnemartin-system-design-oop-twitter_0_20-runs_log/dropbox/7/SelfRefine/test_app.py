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


def test_change_password(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/change_password', json={'email': 'john@example.com', 'old_password': 'password', 'new_password': 'new_password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password changed successfully'}
	assert app.users['john@example.com'].password == 'new_password'


def test_upload_file(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	response = client.post('/upload_file', json={'name': 'file1', 'size': 100, 'owner': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert 'file1' in app.files
	assert app.users['john@example.com'].storage_used == 100


def test_download_file(client):
	app.users['john@example.com'] = User('John Doe', 'john@example.com', 'password')
	app.files['file1'] = File('file1', 100, 'john@example.com')
	response = client.get('/download_file', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'file1', 'size': 100, 'owner': 'john@example.com', 'versions': {}}
