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
	return File('test.txt', 100, 'test@example.com')


def test_register(client, sample_user):
	response = client.post('/register', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.post('/login', json={'email': sample_user.email, 'password': sample_user.password})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'


def test_forgot_password(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.post('/forgot_password', json={'email': sample_user.email})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset link sent'


def test_profile(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.get('/profile', json={'email': sample_user.email})
	assert response.status_code == 200
	assert response.get_json()['email'] == sample_user.email


def test_change_password(client, sample_user):
	app.users[sample_user.email] = sample_user
	response = client.post('/change_password', json={'email': sample_user.email, 'old_password': sample_user.password, 'new_password': 'new_password'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password changed successfully'


def test_upload_file(client, sample_user, sample_file):
	app.users[sample_user.email] = sample_user
	response = client.post('/upload_file', json=sample_file.__dict__)
	assert response.status_code == 201
	assert response.get_json()['message'] == 'File uploaded successfully'


def test_download_file(client, sample_user, sample_file):
	app.users[sample_user.email] = sample_user
	app.files[sample_file.name] = sample_file
	response = client.get('/download_file', json={'file_name': sample_file.name})
	assert response.status_code == 200
	assert response.get_json()['name'] == sample_file.name
