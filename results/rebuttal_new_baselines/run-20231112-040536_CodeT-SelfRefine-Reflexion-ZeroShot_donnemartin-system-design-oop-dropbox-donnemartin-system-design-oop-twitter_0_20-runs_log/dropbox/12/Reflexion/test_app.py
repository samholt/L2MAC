import pytest
import app
from app import User, File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert app.users['test@test.com'].name == 'Test'

def test_login(client):
	app.users['test@test.com'] = User('Test', 'test@test.com', 'test123')
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200

def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'content': 'Hello, world!', 'owner': 'test@test.com'})
	assert response.status_code == 201
	assert app.files['file1'].content == 'Hello, world!'

def test_download(client):
	app.files['file1'] = File('file1', 'Hello, world!', 'test@test.com')
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert response.get_json()['file_content'] == 'Hello, world!'

def test_share(client):
	app.files['file1'] = File('file1', 'Hello, world!', 'test@test.com')
	response = client.post('/share', json={'file_name': 'file1', 'owner': 'test@test.com'})
	assert response.status_code == 200
	assert '/download?file_name=file1' in response.get_json()['shareable_link']
