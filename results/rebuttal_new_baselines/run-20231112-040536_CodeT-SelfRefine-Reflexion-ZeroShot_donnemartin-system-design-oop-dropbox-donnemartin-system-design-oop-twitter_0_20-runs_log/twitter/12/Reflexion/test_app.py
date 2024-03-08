import pytest
from app import app, users, posts

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert users['test'] is not None

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

def test_post(client):
	response = client.post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert len(posts) == 1

def test_delete_post(client):
	response = client.delete('/delete_post', json={'post_id': 0})
	assert response.status_code == 200
	assert len(posts) == 0
