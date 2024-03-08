import pytest
import app
import user

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'test@test.com' in user.users_db


def test_login(client):
	user.users_db['test@test.com'] = user.User('test@test.com', 'test123')
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_login_fail(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}
