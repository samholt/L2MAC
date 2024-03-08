import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'email': 'test@test.com', 'password': 'test'}


def test_login(client):
	client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'id': '1', 'email': 'test@test.com', 'password': 'test'}


def test_login_invalid_credentials(client):
	client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'id': '1', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}
