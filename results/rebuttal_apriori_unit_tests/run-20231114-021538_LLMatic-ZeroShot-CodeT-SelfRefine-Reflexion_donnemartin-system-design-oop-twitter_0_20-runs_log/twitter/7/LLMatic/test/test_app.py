import pytest
import random
import string
import requests

base_url = 'http://localhost:5002'


def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def test_user_registration():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	response = requests.post(f'{base_url}/register', json={'username': username, 'email': email, 'password': password})
	assert response.status_code == 200


def test_user_authentication():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	requests.post(f'{base_url}/register', json={'username': username, 'email': email, 'password': password})
	response = requests.post(f'{base_url}/login', json={'email': email, 'password': password})
	assert response.status_code == 200

