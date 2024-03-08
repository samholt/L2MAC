import pytest
import app

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
	response = client.get('/profile?email=test@example.com')
	assert response.status_code == 200
	user = response.get_json()
	assert user['name'] == 'Test User'
	assert user['email'] == 'test@example.com'
	assert user['storage_used'] == 0


def test_upload(client):
	response = client.post('/upload', json={'name': 'file.txt', 'size': 100, 'content': 'Hello, World!', 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download?file_name=file.txt')
	assert response.status_code == 200
	file = response.get_json()
	assert file['name'] == 'file.txt'
	assert file['size'] == 100
	assert file['content'] == 'Hello, World!'
	assert file['owner'] == 'test@example.com'
	assert len(file['versions']) == 0


def test_upload_new_version(client):
	response = client.post('/upload', json={'name': 'file.txt', 'size': 200, 'content': 'Hello, World! v2', 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}
	response = client.get('/download?file_name=file.txt')
	assert response.status_code == 200
	file = response.get_json()
	assert file['name'] == 'file.txt'
	assert file['size'] == 200
	assert file['content'] == 'Hello, World! v2'
	assert file['owner'] == 'test@example.com'
	assert len(file['versions']) == 1
	assert file['versions'][0]['size'] == 100
	assert file['versions'][0]['content'] == 'Hello, World!'
