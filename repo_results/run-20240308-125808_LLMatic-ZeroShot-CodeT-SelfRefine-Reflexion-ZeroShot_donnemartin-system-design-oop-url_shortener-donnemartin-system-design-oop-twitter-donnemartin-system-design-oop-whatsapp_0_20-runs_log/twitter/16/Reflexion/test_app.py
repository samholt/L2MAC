import pytest
from app import app, users, User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def setup_data():
	users['testuser'] = User('testuser', generate_password_hash('testpass'), 'testuser@test.com')

def test_register(client, setup_data):
	# Test registering user with existing username
	response = client.post('/register', json={'username': 'testuser', 'password': 'testpass', 'email': 'testuser@test.com'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

	# Test registering new user
	response = client.post('/register', json={'username': 'newuser', 'password': 'newpass', 'email': 'newuser@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	# Test registering user with missing data
	response = client.post('/register', json={'username': 'missingdata'})
	assert response.status_code == 400

def test_login(client, setup_data):
	# Test logging in with correct credentials
	response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()

	# Test logging in with incorrect password
	response = client.post('/login', json={'username': 'testuser', 'password': 'wrongpass'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	# Test logging in with non-existent user
	response = client.post('/login', json={'username': 'nouser', 'password': 'nopass'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}
