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
	assert isinstance(app.users['john@example.com'], User)


def test_login(client):
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client):
	response = client.get('/profile?email=john@example.com')
	assert response.status_code == 200
	user = response.get_json()
	assert user['name'] == 'John Doe'
	assert user['email'] == 'john@example.com'
	assert user['storage_used'] == 0


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'size': 100, 'owner': 'john@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	assert isinstance(app.files['file1'], File)
	assert app.users['john@example.com'].storage_used == 100


def test_download(client):
	response = client.get('/download?file_name=file1')
	assert response.status_code == 200
	file = response.get_json()
	assert file['name'] == 'file1'
	assert file['size'] == 100
	assert file['owner'] == 'john@example.com'
