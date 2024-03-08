import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Login successful'}


def test_upload(client):
	response = client.post('/upload', json={'name': 'file1', 'content': 'Hello, World!', 'owner': 'test@test.com'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'File uploaded successfully'}


def test_download(client):
	response = client.get('/download', query_string={'file_name': 'file1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'file_content': 'Hello, World!'}
