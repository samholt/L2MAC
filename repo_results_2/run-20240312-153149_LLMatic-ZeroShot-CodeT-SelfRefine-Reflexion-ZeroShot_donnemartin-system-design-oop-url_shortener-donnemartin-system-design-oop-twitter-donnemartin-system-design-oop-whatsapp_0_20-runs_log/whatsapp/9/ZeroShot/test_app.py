import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User logged in successfully'}


def test_update_profile(client):
	response = client.post('/update_profile', json={'email': 'test@test.com', 'profile': {'picture': 'pic.jpg', 'status': 'Hello'}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Profile updated successfully'}


def test_add_contact(client):
	response = client.post('/add_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Contact added successfully'}


def test_send_message(client):
	response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'contact@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Message sent successfully'}
