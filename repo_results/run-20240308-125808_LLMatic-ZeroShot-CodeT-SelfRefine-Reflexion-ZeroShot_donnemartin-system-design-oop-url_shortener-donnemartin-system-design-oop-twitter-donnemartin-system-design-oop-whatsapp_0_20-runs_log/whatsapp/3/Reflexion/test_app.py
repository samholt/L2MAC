import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}


def test_forgot_password(client):
	response = client.post('/forgot_password', json={'email': 'test@test.com', 'new_password': 'test1234'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password updated successfully'}
