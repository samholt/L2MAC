import pytest
import app
import base64

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_profile(client):
	response = client.get('/profile', query_string={'email': 'test@example.com'})
	assert response.status_code == 200
	user = response.get_json()
	assert user['name'] == 'Test User'
	assert user['email'] == 'test@example.com'
	assert user['storage_used'] == 0


def test_upload(client):
	file_data = base64.b64encode(b'Hello, World!').decode('utf-8')
	response = client.post('/upload', json={'name': 'file.txt', 'size': 100, 'owner': 'test@example.com', 'data': file_data})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download', query_string={'file_name': 'file.txt'})
	assert response.status_code == 200
	file = response.get_json()
	assert file['name'] == 'file.txt'
	assert file['size'] == 100
	assert file['owner'] == 'test@example.com'
	assert file['data'] == 'Hello, World!'
