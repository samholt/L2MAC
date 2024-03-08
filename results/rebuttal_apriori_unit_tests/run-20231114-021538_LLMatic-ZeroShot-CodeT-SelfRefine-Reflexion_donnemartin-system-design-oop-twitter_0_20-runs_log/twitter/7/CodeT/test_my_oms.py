import pytest
import random
import string
from my_oms import app
from flask import json

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_register(client):
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	response = client.post('/register', json={'username': username, 'email': email, 'password': password})
	assert response.status_code == 200

def test_login(client):
	username = random_string()
	email = f'{random_string()}@example.com'
	password = random_string()
	client.post('/register', json={'username': username, 'email': email, 'password': password})
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
