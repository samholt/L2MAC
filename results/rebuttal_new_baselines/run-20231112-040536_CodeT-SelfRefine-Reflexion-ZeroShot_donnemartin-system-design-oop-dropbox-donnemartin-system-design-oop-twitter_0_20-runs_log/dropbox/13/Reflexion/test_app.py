import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return User('Test User', 'test@example.com', 'password')

@pytest.fixture
def sample_file():
	return File('test.txt', 100, [])


def test_register(client, sample_user):
	response = client.post('/register', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.post('/login', json={'email': sample_user.email, 'password': sample_user.password})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.get('/profile', query_string={'email': sample_user.email})
	assert response.status_code == 200
	assert response.get_json() == sample_user.__dict__


def test_upload(client, sample_user, sample_file):
	app.users[sample_user.email] = sample_user
	response = client.post('/upload', json={**sample_file.__dict__, 'email': sample_user.email})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client, sample_file):
	app.files[sample_file.name] = sample_file
	response = client.get('/download', query_string={'filename': sample_file.name})
	assert response.status_code == 200
	assert response.get_json() == sample_file.__dict__


def test_version(client, sample_file):
	app.files[sample_file.name] = sample_file
	response = client.post('/version', json={'filename': sample_file.name, 'version': 'v2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Version added successfully'}
