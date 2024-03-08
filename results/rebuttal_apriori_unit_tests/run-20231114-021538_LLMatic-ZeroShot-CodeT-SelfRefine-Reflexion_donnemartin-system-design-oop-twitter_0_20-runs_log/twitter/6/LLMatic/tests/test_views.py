import pytest
import json
from views import app

@pytest.fixture

def client():
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'email': 'test@example.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201

def test_login(client):
	client.post('/register', data=json.dumps({'username': 'test', 'email': 'test@example.com', 'password': 'test'}), content_type='application/json')
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
