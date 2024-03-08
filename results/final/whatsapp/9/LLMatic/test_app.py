import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200

def test_recover_password(client):
	response = client.post('/recover_password', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200

def test_profile(client):
	response = client.post('/profile', json={'email': 'test@test.com', 'password': 'test123', 'picture': 'test.jpg', 'message': 'Hello', 'settings': {'last_seen': 'everyone'}})
	assert response.status_code == 200

def test_block_contact(client):
	response = client.post('/block_contact', json={'email': 'test@test.com', 'password': 'test123', 'block_email': 'block@test.com', 'block_password': 'block123'})
	assert response.status_code == 200

def test_send_message(client):
	response = client.post('/message', json={'sender': 'test@test.com', 'password': 'test123', 'receiver': 'recv@test.com', 'content': 'Hello', 'text': 'Hello'})
	assert response.status_code == 200

def test_create_group(client):
	response = client.post('/create_group', json={'name': 'Test Group', 'picture': 'group.jpg', 'participants': ['test@test.com'], 'admins': ['test@test.com'], 'messages': []})
	assert response.status_code == 200

def test_post_status(client):
	response = client.post('/post_status', json={'email': 'test@test.com', 'password': 'test123', 'image': 'status.jpg', 'visibility': 'everyone', 'expiry_time': 24})
	assert response.status_code == 200
