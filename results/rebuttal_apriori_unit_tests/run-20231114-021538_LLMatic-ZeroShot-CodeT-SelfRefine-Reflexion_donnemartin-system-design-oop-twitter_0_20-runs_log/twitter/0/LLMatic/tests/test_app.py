import pytest
import random
import string
from views import app
from models import User
from utils import hash_password

app.testing = True
client = app.test_client()


def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def test_user_registration():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	response = client.post('/register', json={'username': username, 'email': email, 'password': password})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}


def test_user_authentication():
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	client.post('/register', json={'username': username, 'email': email, 'password': password})
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert 'token' in response.get_json()
