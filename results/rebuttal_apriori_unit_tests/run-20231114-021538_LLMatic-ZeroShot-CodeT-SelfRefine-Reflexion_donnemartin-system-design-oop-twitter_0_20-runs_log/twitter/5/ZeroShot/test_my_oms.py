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

@pytest.fixture
def random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@pytest.fixture
def random_email(random_string):
	return f'{random_string}@example.com'

@pytest.fixture
def random_password(random_string):
	return random_string

@pytest.fixture
def new_user(random_email, random_password):
	return {'email': random_email, 'password': random_password, 'username': 'testuser'}

def test_register(client, new_user):
	response = client.post('/register', data=json.dumps(new_user), content_type='application/json')
	assert response.status_code == 200
	assert b'Registered successfully' in response.data

def test_login(client, new_user):
	client.post('/register', data=json.dumps(new_user), content_type='application/json')
	response = client.post('/login', data=json.dumps(new_user), content_type='application/json')
	assert response.status_code == 200
	assert b'token' in response.data
