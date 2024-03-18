import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	# Try to register the same user again
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}


def test_login(client):
	# Register a user
	client.post('/register', json={'email': 'test@test.com', 'password': 'test'})

	# Login with correct credentials
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	# Login with incorrect credentials
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}


def test_forgot_password(client):
	# Register a user
	client.post('/register', json={'email': 'test@test.com', 'password': 'test'})

	# Request password reset for existing user
	response = client.post('/forgot_password', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset link sent'}

	# Request password reset for non-existing user
	response = client.post('/forgot_password', json={'email': 'nonexistent@test.com'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
