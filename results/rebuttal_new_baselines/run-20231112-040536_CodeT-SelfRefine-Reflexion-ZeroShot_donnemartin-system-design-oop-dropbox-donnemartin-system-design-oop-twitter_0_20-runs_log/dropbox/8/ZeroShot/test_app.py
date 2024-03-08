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
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_profile(client):
	response = client.get('/profile?email=test@example.com')
	assert response.status_code == 200
	user = response.get_json()
	assert user['name'] == 'Test User'
	assert user['email'] == 'test@example.com'
	assert user['storage_used'] == 0


def test_upload(client):
	response = client.post('/upload', json={'name': 'file.txt', 'size': 100, 'owner': 'test@example.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download?filename=file.txt')
	assert response.status_code == 200
	file = response.get_json()
	assert file['name'] == 'file.txt'
	assert file['size'] == 100
	assert file['owner'] == 'test@example.com'


def test_share(client):
	response = client.post('/share', json={'filename': 'file.txt', 'recipient': 'test2@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'File shared successfully'}
