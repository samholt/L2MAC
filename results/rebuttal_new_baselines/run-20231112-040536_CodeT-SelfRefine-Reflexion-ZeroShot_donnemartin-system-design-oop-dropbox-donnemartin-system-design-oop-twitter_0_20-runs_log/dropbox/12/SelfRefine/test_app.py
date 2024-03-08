import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_profile(client):
	response = client.get('/profile?email=test@example.com')
	assert response.status_code == 200
	user = json.loads(response.data)
	assert user['name'] == 'Test User'
	assert user['email'] == 'test@example.com'
	assert user['password'] == 'password'
	assert user['storage_used'] == 0


def test_change_password(client):
	response = client.post('/change_password', json={'email': 'test@example.com', 'old_password': 'password', 'new_password': 'new_password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Password changed successfully'}


def test_upload_file(client):
	response = client.post('/upload_file', json={'name': 'file.txt', 'size': 100, 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'File uploaded successfully'}


def test_download_file(client):
	response = client.get('/download_file?file_name=file.txt')
	assert response.status_code == 200
	file = json.loads(response.data)
	assert file['name'] == 'file.txt'
	assert file['size'] == 100
	assert file['owner'] == 'test@example.com'


def test_delete_file(client):
	response = client.delete('/delete_file?file_name=file.txt')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'File deleted successfully'}
