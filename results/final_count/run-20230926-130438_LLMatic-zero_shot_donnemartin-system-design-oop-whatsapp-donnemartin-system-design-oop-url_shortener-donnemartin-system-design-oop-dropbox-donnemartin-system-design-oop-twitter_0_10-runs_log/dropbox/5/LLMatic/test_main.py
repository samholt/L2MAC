import pytest
from flask import url_for
from main import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		with app.app_context():
			yield client

def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Home'

def test_register(client):
	response = client.get('/register')
	assert response.status_code == 200
	assert response.data == b'Register'

def test_login(client):
	response = client.get('/login')
	assert response.status_code == 200
	assert response.data == b'Login'

def test_upload(client):
	response = client.get('/upload')
	assert response.status_code == 200
	assert response.data == b'Upload'

def test_download(client):
	response = client.get('/download/test')
	assert response.status_code == 200

def test_share(client):
	response = client.get('/share')
	assert response.status_code == 200
	assert response.data == b'Share'

def test_encrypt(client):
	response = client.get('/encrypt')
	assert response.status_code == 200
	assert response.data == b'Encrypt'

def test_log(client):
	response = client.get('/log')
	assert response.status_code == 200

