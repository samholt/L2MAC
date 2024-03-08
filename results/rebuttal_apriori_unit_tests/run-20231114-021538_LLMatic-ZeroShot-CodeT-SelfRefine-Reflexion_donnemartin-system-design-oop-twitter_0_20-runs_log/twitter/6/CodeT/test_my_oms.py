import pytest
import random
import string
import requests
from my_oms import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_user_registration(client):
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	response = client.post('/register', json={'username': username, 'email': email, 'password': password})
	assert response.status_code == 200

def test_user_authentication(client):
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	client.post('/register', json={'username': username, 'email': email, 'password': password})
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
