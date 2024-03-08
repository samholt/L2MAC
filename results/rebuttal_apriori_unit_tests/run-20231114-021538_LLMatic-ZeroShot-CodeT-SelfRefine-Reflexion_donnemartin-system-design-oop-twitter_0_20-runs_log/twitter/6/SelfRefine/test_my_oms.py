import pytest
import random
import string
import requests

base_url = 'http://localhost:5000'

@pytest.fixture
def random_user():
	return {
		'username': ''.join(random.choices(string.ascii_letters, k=10)),
		'email': f"{''.join(random.choices(string.ascii_letters, k=10))}@example.com",
		'password': ''.join(random.choices(string.ascii_letters, k=10))
	}

@pytest.fixture
def registered_user(random_user):
	requests.post(f'{base_url}/register', json=random_user)
	return random_user

@pytest.fixture
def logged_in_user(registered_user):
	response = requests.post(f'{base_url}/login', json=registered_user)
	return response.json()['token']

def test_register_user(random_user):
	response = requests.post(f'{base_url}/register', json=random_user)
	assert response.status_code == 200

def test_login_user(registered_user):
	response = requests.post(f'{base_url}/login', json=registered_user)
	assert response.status_code == 200

def test_login_invalid_user(random_user):
	response = requests.post(f'{base_url}/login', json=random_user)
	assert response.status_code == 400
