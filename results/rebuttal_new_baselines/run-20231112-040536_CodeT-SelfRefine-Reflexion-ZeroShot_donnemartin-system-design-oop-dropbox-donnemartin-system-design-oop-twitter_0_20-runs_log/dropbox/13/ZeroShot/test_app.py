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


def test_upload(client):
	response = client.post('/upload', json={'name': 'file.txt', 'size': 100, 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download/file.txt')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'File downloaded successfully'
