import pytest
import requests
import random
import string

base_url = 'http://localhost:5000'

@pytest.fixture
def random_user():
	return {'username': ''.join(random.choices(string.ascii_letters, k=10)), 'email': ''.join(random.choices(string.ascii_letters, k=5)) + '@test.com', 'password': ''.join(random.choices(string.ascii_letters, k=10))}


def test_register(random_user):
	response = requests.post(f'{base_url}/register', json=random_user)
	assert response.status_code == 200
	assert response.json()['message'] == 'User registered successfully'


def test_login(random_user):
	requests.post(f'{base_url}/register', json=random_user)
	response = requests.post(f'{base_url}/login', json={'email': random_user['email'], 'password': random_user['password']})
	assert response.status_code == 200
	assert 'token' in response.json()


def test_login_invalid_credentials(random_user):
	requests.post(f'{base_url}/register', json=random_user)
	response = requests.post(f'{base_url}/login', json={'email': random_user['email'], 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert response.json()['message'] == 'Invalid credentials'
