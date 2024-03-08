import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}


def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	token = response.get_json()['token']
	data = jwt.decode(token, app.app.config['SECRET_KEY'])
	assert data['user'] == 'test'

	response = client.post('/login', json={'username': 'wrong', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}
