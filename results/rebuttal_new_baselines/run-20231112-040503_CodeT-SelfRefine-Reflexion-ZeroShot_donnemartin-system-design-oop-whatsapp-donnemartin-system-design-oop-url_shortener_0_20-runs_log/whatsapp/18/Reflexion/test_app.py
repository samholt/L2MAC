import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': {}})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_forgot_password(client):
	response = client.post('/forgot_password', json={'id': '1', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset link sent to email'}
