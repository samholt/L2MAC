import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already registered'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}


def test_forgot_password(client):
	response = client.post('/forgot_password', json={'email': 'test@test.com', 'new_password': 'newpassword'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password updated successfully'}

	response = client.post('/forgot_password', json={'email': 'notregistered@test.com', 'new_password': 'newpassword'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email not registered'}
