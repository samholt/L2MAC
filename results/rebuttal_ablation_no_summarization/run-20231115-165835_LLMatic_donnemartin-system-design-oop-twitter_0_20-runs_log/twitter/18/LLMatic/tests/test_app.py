import pytest
import app
import jwt
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	token = response.get_json()['token']
	assert jwt.decode(token, 'secret', algorithms=['HS256']) == {'user': 'test@test.com'}


def test_invalid_login(client):
	response = client.post('/login', json={'email': 'invalid@test.com', 'password': 'invalid'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}


def test_password_reset(client):
	response = client.post('/password_reset', json={'email': 'test@test.com'})
	assert response.status_code == 200
	token = response.get_json()['token']
	decoded = jwt.decode(token, 'secret', algorithms=['HS256'], options={'verify_exp': False})
	assert decoded['user'] == 'test@test.com'


def test_confirm_password_reset(client):
	exp = datetime.utcnow() + timedelta(minutes=30)
	token = jwt.encode({'user': 'test@test.com', 'exp': exp}, 'secret', algorithm='HS256')
	response = client.post('/confirm_password_reset', json={'token': token, 'new_password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password updated successfully'}
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'new_test'})
	assert response.status_code == 200


def test_edit_profile(client):
	response = client.post('/register', json={'email': 'test2@test.com', 'username': 'test2', 'password': 'test2'})
	assert response.status_code == 200
	response = client.post('/login', json={'email': 'test2@test.com', 'password': 'test2'})
	assert response.status_code == 200
	token = response.get_json()['token']
	response = client.post('/edit_profile', json={'token': token, 'first_name': 'John', 'last_name': 'Doe', 'bio': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}

