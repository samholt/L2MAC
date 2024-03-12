import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': 0}


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/post', json={'user_id': 0, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': 0}
