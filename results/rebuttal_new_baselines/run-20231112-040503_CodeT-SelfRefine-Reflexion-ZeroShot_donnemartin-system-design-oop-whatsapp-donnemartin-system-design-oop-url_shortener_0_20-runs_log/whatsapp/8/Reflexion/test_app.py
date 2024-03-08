import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'id': '1', 'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': {}, 'groups': {}})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_logout(client):
	response = client.post('/logout', json={'id': '1'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logout successful'}


def test_reset_password(client):
	response = client.post('/reset_password', json={'id': '1', 'new_password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset successful'}
