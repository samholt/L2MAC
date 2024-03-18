import pytest
import app
import user

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	user.users_db = {}

def test_register(client, init_db):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

	response = client.post('/register', json={'email': '', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': ''})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}

	response = client.post('/register', json={'email': '', 'password': ''})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid email or password'}

	response = client.post('/register', json={'email': 'test2@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	assert len(user.users_db) == 2

	assert user.users_db['test@test.com'].email == 'test@test.com'
	assert user.users_db['test@test.com'].password == 'test123'

	assert user.users_db['test2@test.com'].email == 'test2@test.com'
	assert user.users_db['test2@test.com'].password == 'test123'

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}

	response = client.post('/login', json={'email': 'nonexistent@test.com', 'password': 'test123'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}
