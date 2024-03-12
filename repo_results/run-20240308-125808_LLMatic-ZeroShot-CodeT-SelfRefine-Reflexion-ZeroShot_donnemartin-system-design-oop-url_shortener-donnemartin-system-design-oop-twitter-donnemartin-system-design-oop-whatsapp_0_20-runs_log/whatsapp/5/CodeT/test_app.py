import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already exists'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}

	response = client.post('/login', json={'email': 'wrongemail@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}
